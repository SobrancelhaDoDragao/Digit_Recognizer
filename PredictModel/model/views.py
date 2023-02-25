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
    Função que converte pixels transparente em pretos e pretos em brancos
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
                imagePretoBranco.putpixel((x,y),(255,255,255))
            # Se não então branco
            else:
                imagePretoBranco.putpixel((x,y),(0,0,0))

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

      if pxl == (0,0,0):
        colunaTotalmenteBranca += 1
        if colunaTotalmenteBranca == h:

          listaDeColunasVazias.append(x)
      else:
        listaDeColunasComPixel.append(x)
        
 

  primeiroValor = listaDeColunasComPixel[0]
  ultimoValor = listaDeColunasComPixel[-1]
  
  # Primeiro (0) depois o Ultimo (h) (178,0,452,h)
  img_cortada = imageColored.crop((primeiroValor - 5,0,ultimoValor + 5,h))

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
        # Converte a imagem para escala de cinza e redimensiona para 28x28 pixels
        # .convert('L')
        imagem = imagem.resize((28, 28)).convert('L')

        # Converte a imagem em um array unidimensional
        img_array = np.array(imagem).reshape(1,784)
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

@csrf_exempt
def SalvarImagem(request):

    if request.method == 'POST':
        
        # Recebendo os dados em json e convertendo
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

        return JsonResponse({'success': True})
    
    else:

        return JsonResponse({'erro': False})


def get_csrf(request):

    csrf_token = csrf.get_token(request)
    
    return JsonResponse({'csrf_token': csrf_token})
