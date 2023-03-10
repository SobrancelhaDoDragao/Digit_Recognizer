<h1 align="center">Digit_Recognizer</h1>

<h3 align="center">Implementação do desafio digit recognizer em uma aplicação web</h3>

<div align="center">
  
<img width="70px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" /><img width="70px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain-wordmark.svg" /><img width="70px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original-wordmark.svg" />
  
</div>       
                   
<h4 align="center">Status: em progresso</h4>

## Sobre o projeto

Este é um projeto que tem como objetivo testar na prática o algoritmo de reconhecimento de dígitos desenvolvido durante o desafio do [Digit Recognizer MNIST](https://www.kaggle.com/c/digit-recognizer).

A aplicação web consiste em uma área de desenho onde é possível desenhar os dígitos de 0 a 9 manualmente. Em seguida, o algoritmo de IA treinado irá processar o desenho e retornar qual número foi desenhado.

## Como Funciona

1. Acesse o site e selecione a área de desenho.
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

Nesse projeto foi usado o algoritmo [random forest classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) que foi treinado no conjunto de dados [mnist](http://yann.lecun.com/exdb/mnist/), ele obteve 96% de precisão no conjunto de teste, porém na prática obteve muito erros. Acredito que os erros ocorreram devido a diferença de formato dos digitos que o algoritmo recebe, tentarei melhorar o pré-processamento dos digitos.

O motivo da escolha do algoritmo de IA

## Infraestrutura do projeto/fluxo

Canvas vue.js manda em json para o django api, python pré processamento, predict retorno json

## Layout

## Licença

The scripts in this project are released under the [MIT License](./LICENSE.md) 
