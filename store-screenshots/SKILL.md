---
name: store-screenshots
description: Cria os screenshots/artes das lojas (App Store e Google Play) de um app mobile num canvas do Claude Design, seguindo um padrão fixo de layout — panorama contínuo + um quadro por tela e por loja, prints reais capturados do app com dados de demonstração realistas. Use quando o usuário pedir "screenshots da loja", "prints para a App Store/Play Store", "artes da loja", "design dos prints", "criar um design para o app na loja", "feature graphic", ou pedir para refazer/atualizar essas artes em qualquer projeto.
---

# Screenshots das lojas — padrão de design

Objetivo: entregar, para cada app, um canvas do Claude Design pronto para exportar,
com prints REAIS do app (nada de mock desenhado), dados de demonstração com cara de
produto em uso, e um conceito visual próprio de cada app — nunca o mesmo template
recolorido.

O trabalho tem quatro fases, nesta ordem. Não pule para o design antes de ter os
prints bons: arte bonita com print vazio não serve.

1. Entender o app e combinar o conjunto de telas
2. Preparar dados de demonstração realistas
3. Capturar e limpar os prints
4. Montar o canvas (padrão de layout abaixo)

Detalhes de cada fase estão em `reference/`. Leia o arquivo da fase antes de executá-la.

---

## Fase 1 — Entender o app

- Leia o que o projeto já tem: legendas/títulos das telas (ex.: `loja/legendas.json`),
  README de prints, flows de captura (Maestro, Fastlane, etc.), cores e fontes do tema
  do app, ícone do app, se o app aceita tablet (iOS: `TARGETED_DEVICE_FAMILY "1,2"` →
  iPad é obrigatório na App Store).
- Liste as telas do conjunto (normalmente 5–8; App Store aceita até 10, Play até 8) e
  o título/subtítulo de cada uma. Se o projeto já tem legendas, use-as literalmente.
- Se houver mais de um app (ex.: app do cliente e app do parceiro/admin), cada um ganha
  um conceito visual DIFERENTE (ver "Conceito" na Fase 4).

## Fase 2 — Dados de demonstração (`reference/dados-demo.md`)

Print com "Nenhum item encontrado", lorem ipsum, nome de usuário tipo `jeep-kite-123`,
foto de câmera de emulador ou contas de teste ("tester") é o erro mais comum. Antes de
capturar:

- Percorra cada tela do conjunto e anote o que está vazio, feio ou falso.
- Peça autorização antes de criar/alterar dados em produção; com ela, crie os dados
  pela própria API do app (mesmos endpoints que o app usa), nunca direto no banco.
- Nomes e sobrenomes brasileiros comuns, bios curtas, fotos de banco livre (CC0 /
  domínio público), descrições reais no lugar de lorem ipsum.
- Nunca use a foto ou o nome pessoal do usuário/dono do projeto nas artes.

## Fase 3 — Captura (`reference/captura.md`)

- Use um único device por vez (dois runs de Maestro em paralelo quebram ambos).
- Barra de status limpa (9:41, bateria e sinal cheios) e, depois, `scripts/limpar_status.py`
  para apagar ícones de notificação que sobraram — exceto em telas com foto atrás da
  barra (use o original).
- Revise SEMPRE os prints numa folha de contato antes de subir (montagem lado a lado
  com PIL) — procure: spinner/carregando, telas vazias, nomes feios, banners de
  pendência, avatar estranho, notificações antigas.
- Bugs do app que aparecem na captura (tela travada no splash, lista que nunca carrega)
  são bugs reais: corrija no código com comentário curto e avise o usuário.

## Fase 4 — Canvas (`reference/canvas-formato.md` + `templates/`)

### Estrutura fixa (sempre a mesma)

Um canvas por app, com:

| Quadro | Tamanho do quadro | Exportar |
|---|---|---|
| `Main.dc.html` — panorama de N prints colados (N×430 × 932) | N×430 × 932 | — |
| `iOS-k.dc.html` — um print, via `<dc-import name="Main" platform="ios" slide="k-1">` | 430 × 932 | 3× = 1290 × 2796 (iPhone 6,9″) |
| `Play-k.dc.html` — mesmo print, `platform="android"` (corta 84 px em cima e embaixo) | 430 × 764 | 1080 × 1920 |
| `Play-Feature.dc.html` — recurso gráfico do Google Play | 1024 × 500 | 1× |
| `Tablet.dc.html` + `iPad-k.dc.html` (só se o app aceita iPad) | 1032 × 1376 | 2× = 2064 × 2752 |

- O panorama é a fonte única: os quadros por tela só importam o `Main` com `slide`, então
  mudar o `Main` atualiza todos. Nunca duplique o conteúdo em cada quadro.
- O Android mostra só a faixa y = 84…848 do panorama: título, fichas e tudo que importa
  ficam dentro dela; o celular pode sangrar para fora embaixo.
- Tablet não cabe em panorama (largura máxima de quadro = 8000 px): `Tablet.dc.html`
  tem `slide` com default 0 e preview de um quadro só.

### Padrão de layout de cada print (430 × 932)

De cima para baixo:

1. **Topo (y ≈ 96–130):** no 1º print, ícone do app + wordmark; nos demais, um
   "eyebrow" curto (rótulo do conceito, ex.: dia da agenda, número 01–07).
2. **Título (y ≈ 130–300):** 2–3 linhas, 40–50 px, peso forte, a parte final em cor de
   destaque (`<span>`). Texto = legenda do projeto, literal.
3. **Subtítulo:** 16–17 px, uma ou duas linhas, cor de contraste médio.
4. **Device (y ≈ 380–420 até sangrar embaixo):** print 300 × 667 dentro de uma moldura
   (padding 9, raio 46/38), centrado (left 56). Nada de moldura falsa de iPhone com
   notch desenhado.
5. **Fichas flutuantes:** 1 por print, metade sobre a borda do device, mostrando um dado
   QUE APARECE NO PRÓPRIO PRINT (ex.: "10 vagas · R$ 17,14 por pessoa", "Local
   confirmado", "R$ 240,00 receita semanal"). Nunca invente números.
6. **Elemento contínuo de fundo:** algo que atravessa os N prints e amarra o panorama
   (linhas de uma quadra, grade de agenda, trajetória pontilhada, faixa) — é o que faz
   os prints parecerem uma peça só na vitrine da loja.

### Conceito: um por app, tirado do domínio

Antes de escrever o `Main`, decida e diga ao usuário em uma linha:

- **Metáfora do domínio** que vira o fundo contínuo (ex.: app de jogar → marcação de
  quadra; app de gestão → grade da agenda com reservas reais nos horários; app de
  finanças → linha de gráfico; app de entrega → rota).
- **Fundo:** claro OU escuro, cor da marca (tint ou a cor escura do tema), sem gradiente.
- **Par tipográfico** do Google Fonts que combine com o conceito (ex.: Barlow Condensed
  itálico + Barlow para esporte; Space Grotesk + Manrope para painel). Proibido Inter,
  Roboto e Arial, mesmo que o app use.
- **Destaque:** a cor de ação da marca, usada no fim dos títulos e nas fichas.

Dois apps do mesmo produto: troque fundo (claro × escuro), tipografia, metáfora e
ângulo do device; mantenha só as cores de marca. Ver exemplos em
`reference/exemplos.md`.

### Regras que não se negociam

- Prints reais, limpos, com dados realistas. Nenhum número, nome ou status inventado.
- Sem emoji, sem gradiente de fundo, sem cards com borda lateral colorida.
- Ícones em SVG de traço inline, `aria-hidden="true"`.
- Contraste de texto ≥ 4.5:1 (3:1 acima de 24 px).
- Legendas literais do projeto; não reescreva copy sem pedirem.
- Ao terminar, entregue: links dos canvas, o que mudou nos dados, bugs corrigidos
  (arquivo por arquivo) e o que ainda precisa de deploy/commit.

## Arquivos desta skill

- `reference/dados-demo.md` — como popular dados de demonstração pela API (contas,
  fotos CC0, e-mails temporários para cadastro, notificações).
- `reference/captura.md` — Maestro/emulador/simulador: armadilhas e correções.
- `reference/canvas-formato.md` — formato exato dos arquivos do canvas e ordem de publicação.
- `reference/exemplos.md` — dois conceitos completos já usados (app do jogador e app do parceiro).
- `templates/Main.dc.html`, `templates/slide.dc.html`, `templates/Tablet.dc.html`,
  `templates/canvas.json` — esqueletos para copiar.
- `scripts/limpar_status.py` — apaga ícones de notificação ao lado do relógio.
- `scripts/folha_contato.py` — monta a folha de contato para revisar os prints.
