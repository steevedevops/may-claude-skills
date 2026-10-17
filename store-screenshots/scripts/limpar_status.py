"""Apaga os ícones de notificação ao lado do relógio na barra de status (prints Android).

Pinta a faixa entre o relógio e o centro da barra com a cor da própria barra; o relógio
(9:41) e os ícones de sinal/bateria à direita ficam intactos. Medidas para 1080 px de
largura, escaladas para outras larguras.

Não use em telas com foto atrás da barra de status: o retângulo aparece. Para essas,
copie o original.

uso: python limpar_status.py <pasta originais> <pasta limpos>
"""
import glob
import os
import sys

from PIL import Image, ImageDraw

origem, destino = sys.argv[1], sys.argv[2]
os.makedirs(destino, exist_ok=True)
for caminho in sorted(glob.glob(os.path.join(origem, '*.png'))):
    im = Image.open(caminho).convert('RGB')
    escala = im.width / 1080
    # cor da barra num ponto vazio entre os ícones da esquerda e os da direita
    cor = im.getpixel((int(560 * escala), int(64 * escala)))
    ImageDraw.Draw(im).rectangle(
        (int(124 * escala), int(30 * escala), int(372 * escala), int(100 * escala)),
        fill=cor,
    )
    im.save(os.path.join(destino, os.path.basename(caminho)), optimize=True)
    print(os.path.basename(caminho), cor)
