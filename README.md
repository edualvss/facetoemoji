# facetoemoji
Reconhecimento facial com OpenCV em python para gerar fotos com emojis no lugar dos rostos reconhecidos

## Dependências
* Python
* NumPy
* OpenCV 3

## Forma de uso
```
python live.py <diretório de saída>
Exemplo: "python live.py /home/eas/output"
```

Enquanto o programa executar, pressione `ESPAÇO` para registrar a foto quando rostos estiverem sendo reconhecidos e `ESC` para sair.
As fotos serão armazenadas no <diretório de saída>.

Garanta que o diretório "emojis" esteja no mesmo nível no script "live.py"
Se desejar alterar o conjunto de emojis, basta trocar as figuras do diretório "emojis" (use o formato PNG com transparência)

## Recursos utilizados:
* Código fonte base para o reconhecimento facial extraído de: https://realpython.com/face-detection-in-python-using-a-webcam/
* Função para unir 2 imagens com OpenCV: https://stackoverflow.com/questions/14063070/overlay-a-smaller-image-on-a-larger-image-python-opencv
* Emoji pack de "Adrian Garza" (https://vetoresdmg.blogspot.com/2018/11/emojis-de-whatsapp-free-download-pack.html)

