from django.shortcuts import render
from django.http import JsonResponse
import base64
import json
from PIL import Image
import pandas as pd
import numpy as np
import joblib
from django.middleware import csrf
from django.views.decorators.csrf import csrf_exempt


def RGBAConverter(imageColored):
    """
    Função que converte pixels transparente em brancos
    """

    w, h = imageColored.size

    # Nova imagem rgb
    imagePretoBranco = Image.new("RGB",(w,h))
         
    for x in range(w):
        for y in range(h):
            pxl = imageColored.getpixel((x,y))
        
            #Inverter valores
            # Se possuir tranparencia, então deverá ser preto
            if pxl[3]:
                imagePretoBranco.putpixel((x,y),(0,0,0))
            # Se não então branco
            else:
                imagePretoBranco.putpixel((x,y),(255,255,255))

    return imagePretoBranco

def RemoverEspacosBrancos(imageColored):
  """
  Cortar os espaços em brancos em volta do numero
  """
  w, h = imageColored.size
  
  listaDeColunasVazias = []
  listaDeColunasComPixel = []

  for x in range(w):
    colunaTotalmenteBranca = 0
    for y in range(h):

      pxl = imageColored.getpixel((x,y))

      if pxl == (255,255,255):
        colunaTotalmenteBranca += 1
        if colunaTotalmenteBranca == h:

          listaDeColunasVazias.append(x)
      else:
        listaDeColunasComPixel.append(x)
        
 

  primeiroValor = listaDeColunasComPixel[0]
  ultimoValor = listaDeColunasComPixel[-1]
   

  listaDeLinhasVazias = []
  listaDeLinhasComPixel = []

  for x in range(h):
    LinhaTotalmenteBranca = 0
    for y in range(w):
      pxl = imageColored.getpixel((y,x))
        
      if pxl == (255,255,255):
        LinhaTotalmenteBranca += 1
        if LinhaTotalmenteBranca == w:
          listaDeLinhasVazias.append(x)
      else:
          listaDeLinhasComPixel.append(x)
       
  
  primeiroValorHorizontal = listaDeLinhasComPixel[0]
  ultimoValorHorizontal = listaDeLinhasComPixel[-1]
    
  # Para cortar uma imagem é preciso fornecer as coordenadas de um rentângulo
  # (left,top,right,bottom)
  left = primeiroValor
  top = primeiroValorHorizontal
  right = ultimoValor
  bottom = ultimoValorHorizontal
  # Somando + 5 subtraindo - 5 para ter uma margem do numero até a borda 
  img_cortada = imageColored.crop((left-5,top-5,right+5,bottom+5))
    
  return img_cortada


def index(request):
    return render(request,'index.html')

@csrf_exempt
def PredictDigit(request):
    
    if request.method == 'POST':
        
        # Recebendo os dados em json e convertendo
        # Esse comando é aparentemente inutil 
        body_unicode = request.body.decode('utf-8')
        # Convertendo uma string json em dicionario python
        body = json.loads(body_unicode)
        # Salvando dados
        data_url = body.get('data_url')

        # Removendo informções iniciais
        data_url = data_url.split(',')[1]
        # Decodificando
        img_bytes = base64.b64decode(data_url)
        
        # Criando a imagem
        with open('imagem.png', 'wb') as file:
            file.write(img_bytes)
        
        # Abrir a imagem RGBA
        img_rgba = Image.open('imagem.png')
     
        imagem = RGBAConverter(img_rgba)
        imagem = RemoverEspacosBrancos(imagem)
        # Preparando os dados para o modelo
        imagem.save('teste.png')
        # redimensiona para 28x28 pixels
        imagem = imagem.resize((28, 28))
        # Converte a imagem para escala de cinza
        imagem = imagem.convert('L')
        
        # Converte a imagem em um array unidimensional
        img_array = np.array(imagem)
        # Deixado o fundo preto e o digito branco, o scitlearn funciona melhor assim
        img_array = np.invert(img_array)

        # Convertendo no formato adequado
        img_array = img_array.reshape(1,784)
        
        # Criando lista com o nome dos pixels
        lista = [f'pixel{n}' for n in range(784)]
        # Salvando em um dataframe
        data = pd.DataFrame(img_array, index=[0], columns=lista)
        
        # Carregando modelo treinado
        rf_model = joblib.load('random_forest_model.joblib')
        # usar o modelo para fazer previsões
        prediction = rf_model.predict(data) 
     
        print(f"Previsão do modelo: {prediction}")

        data = {
            'digit':int(prediction),
        }
        
        return JsonResponse(data)

    else:

        return JsonResponse({'erro': False})


def get_csrf(request):

    csrf_token = csrf.get_token(request)
    
    return JsonResponse({'csrf_token': csrf_token})
