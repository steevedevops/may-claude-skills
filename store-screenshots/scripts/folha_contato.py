"""Monta uma folha de contato (prints lado a lado) para revisar o conjunto de uma vez.

uso: python folha_contato.py <pasta com PNGs> <saida.png> [largura de cada print, padrão 300]
"""
import glob
import os
import sys

from PIL import Image

pasta, saida = sys.argv[1], sys.argv[2]
largura = int(sys.argv[3]) if len(sys.argv) > 3 else 300
arquivos = sorted(glob.glob(os.path.join(pasta, '*.png')))
if not arquivos:
    sys.exit('nenhum PNG em ' + pasta)

imagens = []
for caminho in arquivos:
    im = Image.open(caminho).convert('RGB')
    imagens.append(im.resize((largura, round(im.height * largura / im.width))))

altura = max(im.height for im in imagens)
folha = Image.new('RGB', (largura * len(imagens) + 10 * (len(imagens) - 1), altura), 'black')
for k, im in enumerate(imagens):
    folha.paste(im, (k * (largura + 10), 0))
folha.save(saida)
print(saida, [os.path.basename(c) for c in arquivos])
