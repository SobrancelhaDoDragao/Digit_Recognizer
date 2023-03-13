<h1 align="center">Digit Recognizer</h1>

<h3 align="center">Implementação do desafio digit recognizer em uma aplicação web</h3>

<div align="center">
  
<img width="70px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" /><img width="70px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain-wordmark.svg" /><img width="70px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original-wordmark.svg" /> <img width="70px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original-wordmark.svg" />  <img width="70px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original-wordmark.svg" />
          
</div>       
  
<div align="center">

<h4>Status: em progresso</h4>

[![Deploy on railway](https://railway.app/button.svg)](https://digitrecognizer.up.railway.app/)

</div>



## Tópicos

1. [Sobre o projeto](#sobre-o-projeto)
2. [Como funciona](#como-funciona)
3. [Tecnologias usadas](#tecnologias-usadas)
4. [Inteligência artificial](#inteligência-artificial)
5. [Infraestrutura do projeto/fluxo](#infraestrutura-do-projetofluxo)
6. [Telas](#telas)
7. [Instalar o projeto localmente](#instalar-o-projeto-localmente)
8. [Licença](#licença)

## Sobre o projeto

Este é um projeto que tem como objetivo testar na prática o algoritmo de reconhecimento de dígitos desenvolvido durante o desafio do [Digit Recognizer MNIST](https://www.kaggle.com/c/digit-recognizer).

A aplicação web consiste em uma área de desenho onde é possível desenhar os dígitos de 0 a 9 manualmente. Em seguida, o algoritmo de IA treinado irá processar o desenho e retornar qual número foi desenhado.

## Como Funciona

1. Acesse o [site](https://digitrecognizer.up.railway.app/) e selecione a área de desenho.
2. Desenhe o dígito que deseja reconhecer.
3. Clique em "Pronto" para que o algoritmo de IA analise o desenho.
4. O número reconhecido será exibido na tela.

## Tecnologias usadas

- **Back-end**
   - Python
   - Django
   - Scikit learn
   - Pandas
   - Numpy
- **Front-end**
  - Vue.js
  - Javascript
  - Html
  - Css

## Inteligência artificial

Para este projeto, eu utilizei o algoritmo [Random Forest Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html), treinado com os dados do conjunto [MNIST](http://yann.lecun.com/exdb/mnist/), que contém 70 mil dígitos manuscritos. O modelo alcançou uma precisão de 96% no conjunto de teste, no entanto, na prática, encontrei muitos erros. Acredito que isso ocorreu devido às diferenças de formato dos dígitos que o algoritmo recebeu. Para melhorar a precisão, planejo aprimorar o pré-processamento dos dígitos. 

Escolhi o Random Forest Classifier por sua simplicidade e eficácia. Considerei usar o TensorFlow em conjunto com o Keras, mas não foi possível devido à incompatibilidade da CPU do meu computador com o TensorFlow.

## Infraestrutura do projeto/fluxo

### Estrutura de pastas

- [digit_recoginizer] Pasta onde estão os arquivos vue.js
- [DjangoIA] Pasta onde estão os arquivos do django, aqui são administrados os arquivos estáticos gerados pelo vue.js. Aqui onde o projeto funciona.

### Fluxo do programa

Primeiramente, o usuário desenha um dígito de 0 a 9 no canvas e envia os dados. Durante o processo de envio, os dados do canvas são convertidos em formato de imagem usando a função <code>toDataURL()</code>. Em seguida, os dados são enviados para a view <code>PredictDigit()</code>, do Django. Essa função converte a imagem para o espaço de cores RGB, remove espaços em branco ao redor do dígito, redimensiona a imagem para 28 x 28 pixels, converte-a em escala de cinza e transforma-a em um array de números. Então, o modelo faz uma previsão com base nos dados do array e retorna um JSON com o dígito previsto.

## Telas

### Tela de desenho

<img width="60%" src="https://github.com/SobrancelhaDoDragao/Digit_Recognizer/blob/main/digitRecognizerPrint.png"  />

### Tela do predict

<img width="60%" src="https://github.com/SobrancelhaDoDragao/Digit_Recognizer/blob/main/DigitRecognizerPredictPrint.png" />

## Instalar o projeto localmente

### Pré-requisitos

- [Python 3.8.10](https://www.python.org/downloads/)
- [Venv](https://docs.python.org/pt-br/3/library/venv.html)

### Execute os seguintes comandos

1. Baixe o repositório no seu computador
2. Agora abra a pasta DjangoIA pelo terminal
3. Digite: <code>python -m venv env</code>, para criar um ambiente virtual para instalar as bibliotecas
4. Ative o ambiente virtual: <code>source env/bin/activate</code>
5. Agora digite: <code>pip install -r requirements.txt</code>, para instalar as bibliotecas
6. E finalmente rode o projeto:<code>python manage.py runserver</code>

## Licença

The scripts in this project are released under the [MIT License](./LICENSE.md) 
