from django.shortcuts import render
from django.http import JsonResponse
import base64
import json
from PIL import Image
from io import BytesIO
import pandas as pd
import numpy as np
import joblib
from django.middleware import csrf
from django.views.decorators.csrf import csrf_exempt
from .pre_processamento import *

def index(request):
    from pathlib import Path

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    return render(request,'index.html',{'teste':BASE_DIR})

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
        
        # Abrir a imagem RGBA
        img_rgba = Image.open(BytesIO(img_bytes))
        
        imagem = RGBAConverter(img_rgba)
        
        # Caso o quadro esteja vazio
        try:
            imagem = RemoverEspacosBrancos(imagem)
        except:
            data = {
            'digit':'Error',
            }
            return JsonResponse(data)
        
        # Preparando os dados para o modelo
        
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
        # Talves eu tire esse datafram Pandas, não há necessidade 
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
