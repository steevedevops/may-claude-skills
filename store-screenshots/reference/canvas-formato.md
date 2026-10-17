# Formato do canvas (Claude Design)

O canvas é um Artifact do tipo Design. As instruções do próprio tipo (que vêm ao criar
ou ler o canvas) mandam sobre detalhes de formato; este arquivo resume o que o padrão
usa. Se algo aqui conflitar com as instruções do tipo, siga o tipo.

## Criar

1. `Artifact` `action: "quickstart"` com `intent: "design"` e depois publicar com o
   `type_url` do tipo Design e um `title` (ex.: "<App> — Screenshots das lojas").
   Um canvas por app.
2. Subir os prints e o ícone como assets (`publish` com `url`, `asset: true`,
   `file_paths`): até 25 por chamada. Use as URLs `/_blob/<id>` devolvidas, literais.
3. Pasta local `<root>/project/` no scratchpad. Escrever `project/canvas.json` COMPLETO
   (todos os quadros que virão) e `project/Main.dc.html`; publicar os dois juntos
   (`url`, `root`, `file_path` = canvas.json, `files` = Main).
4. Depois, um quadro por vez: escrever o arquivo e publicar (`file_path` = ele).
5. Não verificar renderizando/screenshotando o canvas, a menos que o usuário peça.

Atualizar prints depois: subir os novos assets, trocar os ids nos arquivos (sed), e
publicar só os arquivos mudados. Se a publicação disser que há versão mais nova, leia
os arquivos (`action: "read"`, `paths`) e aplique a mudança sobre eles.

## canvas.json (posições usadas no padrão)

- `Main.dc.html` em (0, 0), w = N×430, h = 932.
- Linha iOS em y = 1312, linha Play em y = 2624, x = k×510 (430 + 80 de espaço).
- `Play-Feature.dc.html` em (0, 3708), 1024 × 500.
- Tablet (se houver): `Tablet.dc.html` em (0, 4611) 1032 × 1376; `iPad-k` em
  y = 6107, x = k×1112.
- Notas `title1` ≥ 223 px acima de cada linha, com o tamanho de exportação no texto:
  "App Store · iPhone 6,9″ · exportar 3× = 1290 × 2796",
  "Google Play · telefone · exportar 1080 × 1920",
  "Google Play · Recurso gráfico · exportar 1024 × 500",
  "App Store · iPad 13″ · exportar 2× = 2064 × 2752".
- `createdOnFiles: {"v":1,"at":"<agora RFC 3339>"}` ao criar.

Ver `templates/canvas.json`.

## Main.dc.html (panorama)

- Raiz `position: relative; width: {{rootW}}px; height: {{rootH}}px; overflow: hidden`
  com a cor de fundo; dentro, uma faixa `position: absolute; top: {{stripY}}px;
  left: {{stripX}}px; width: N×430px; height: 932px` com tudo posicionado em absoluto
  em coordenadas do panorama (print k ocupa x = k×430 … k×430+430).
- Props: `platform` (ios | android) e `slide` (-1 = panorama inteiro).
- `renderVals`: `rootW = whole ? 430*N : 430`, `rootH = android ? 764 : 932`,
  `stripX = whole ? 0 : -slide*430`, `stripY = android ? -84 : 0`.
- Ordem de camadas: fundo contínuo (SVG) → números/eyebrows → títulos → devices →
  fichas por cima.
- Fontes via `<link>` do Google Fonts no `<helmet>`; manter
  `<script src="./support.js"></script>` exatamente no `<head>`.
- `data-props` com aspas simples; classe `Component extends DCLogic`.

## Quadros por print

Cada `iOS-k.dc.html` / `Play-k.dc.html` / `iPad-k.dc.html` é só um invólucro com o mesmo
`<helmet>` de fontes do Main e:

```html
<div style="width: 430px; height: 932px; overflow: hidden">
<dc-import name="Main" platform="ios" slide="0" hint-size="430px,932px"></dc-import>
</div>
```

(Play: `platform="android"`, 430 × 764. iPad: `name="Tablet"`, 1032 × 1376.)

## Tablet.dc.html

Mesma ideia do Main em escala ~2,4×: faixa de N×1032 × 1376, prop `slide` com
default 0 e `$preview` 1032 × 1376 (o panorama inteiro passaria de 8000 px).
Device: moldura 676 de largura (padding 18), print 640 × 853, top ≈ 480.
Títulos 70 px, subtítulos 28 px, eyebrow 22 px, fichas ~2,4× maiores.
