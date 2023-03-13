"""
Funçães para o processamento de imagem
"""
from PIL import Image

def RGBAConverter(imageColored):
    """
    Função que converte pixels transparente em brancos e pretos
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