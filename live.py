# This script will detect faces via your webcam.
# Tested with OpenCV3

import cv2
import sys
import os
import random


def merge_image(back, front, x,y):
    # convert to rgba
    if back.shape[2] == 3:
        back = cv2.cvtColor(back, cv2.COLOR_BGR2BGRA)
    if front.shape[2] == 3:
        front = cv2.cvtColor(front, cv2.COLOR_BGR2BGRA)

    # crop the overlay from both images
    bh,bw = back.shape[:2]
    fh,fw = front.shape[:2]
    x1, x2 = max(x, 0), min(x+fw, bw)
    y1, y2 = max(y, 0), min(y+fh, bh)
    front_cropped = front[y1-y:y2-y, x1-x:x2-x]
    back_cropped = back[y1:y2, x1:x2]

    alpha_front = front_cropped[:,:,3:4] / 255
    alpha_back = back_cropped[:,:,3:4] / 255
    
    # replace an area in result with overlay
    result = back.copy()
    result[y1:y2, x1:x2, :3] = alpha_front * front_cropped[:,:,:3] + (1-alpha_front) * back_cropped[:,:,:3]
    result[y1:y2, x1:x2, 3:4] = (alpha_front + alpha_back) / (1 + alpha_front*alpha_back) * 255

    return result




# Main Program

camera = cv2.VideoCapture(0) # Get webcam video capture
#camera = cv2.VideoCapture(1) # Get external camera video capture

outputPath = "."
if len(sys.argv) > 1:
	outputPath = sys.argv[1]
print('outputPath',outputPath)

# Count number of existing files in output path to generate new images 
files = os.listdir(outputPath)
counter = len(files)

# Get all available emojis on emojis folder
emojis = os.listdir("emojis")

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):
	# Capture frame-by-frame
	ret, frame = camera.read()

	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
		#flags = cv2.CV_HAAR_SCALE_IMAGE
	)

#	print("Found {0} faces!".format(len(faces)))

	listFaces = [] # Array with start point and end point of faces recogonized 

	blended = frame.copy()
	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		startPoint = (x,y)
		endPoint = (x+w, y+w)
		listFaces.append( (startPoint,endPoint, w,h) )
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

	if len(listFaces) > 0:
		for (startPoint, endPoint,width,height) in listFaces:
			selectedEmoji = emojis[random.randint(0, len(emojis)-1)]
			selectedEmoji = "./emojis/"+selectedEmoji
			emoji = cv2.imread(selectedEmoji,-1)
			foreground = cv2.resize(emoji,(width,height))
			blended = merge_image(blended, foreground,startPoint[0], startPoint[1])


	# Display the resulting frame
	cv2.imshow('#OPA2021', frame)

	keyPressed = cv2.waitKey(33) # Capture keyboard press
	if keyPressed == 27: # 'ESC' Key in ASCII
		print('ESC')
		break # Exit from loop and program
	elif keyPressed == 32: # Take a picture when space key is pressed
		print('SPACE')
		cv2.imwrite(outputPath+"/OPA2021-"+ str(counter)+".png",blended) # Write capture in a png file
		counter += 1


# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()
