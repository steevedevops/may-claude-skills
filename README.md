# may-claude-skills

Skills pessoais para o Claude Code. Cada pasta na raiz é uma skill (`<nome>/SKILL.md`).

| Skill | Para que serve |
|---|---|
| [`store-screenshots`](store-screenshots/SKILL.md) | Cria as artes de screenshots da App Store e do Google Play num canvas do Claude Design, com prints reais, dados de demonstração e um padrão fixo de layout. |

---

## store-screenshots

Gera as artes das lojas de um app mobile seguindo sempre o mesmo padrão, em quatro
fases: entender o app → preparar dados de demonstração → capturar os prints →
montar o canvas.

### O que ela cobre

- **Dados de demonstração** — revisa cada tela antes de capturar (listas vazias,
  nomes técnicos, lorem ipsum, fotos de emulador, banners de pendência), cria dados
  realistas pela própria API do app (pedindo autorização antes de mexer em produção),
  cria contas extras com e-mail temporário (mail.tm) e troca fotos por imagens CC0 do
  Wikimedia Commons.
- **Captura** — as armadilhas de Maestro, emulador Android e simulador iOS já
  resolvidas: pasta de saída do Maestro 2.10+, rótulos combinados do Flutter no Android,
  GPS do emulador, app travado no splash, build do iOS no Xcode recente, nunca rodar
  dois devices ao mesmo tempo, barra de status limpa e revisão numa folha de contato.
- **Estrutura do canvas** — um panorama principal (`Main.dc.html`) e quadros por loja
  que importam esse panorama:

  | Quadro | Tamanho | Exportar |
  |---|---|---|
  | Panorama (N prints colados) | N×430 × 932 | — |
  | iOS (iPhone 6,9″) | 430 × 932 | 3× = 1290 × 2796 |
  | Google Play (celular) | 430 × 764 | 1080 × 1920 |
  | Recurso gráfico do Play | 1024 × 500 | 1× |
  | iPad 13″ (se o app aceita iPad) | 1032 × 1376 | 2× = 2064 × 2752 |

  O Android mostra só a faixa y = 84…848 do panorama, então tudo o que importa fica
  dentro dela.
- **Layout de cada print** — de cima para baixo: ícone ou eyebrow, título da legenda
  (com a parte final em destaque), subtítulo, device saindo pela base e uma ficha
  flutuante com um dado real do próprio print. Um elemento contínuo de fundo atravessa
  todos os prints e amarra o panorama.
- **Um conceito visual por app, tirado do domínio** — ex.: app de jogar → marcação de
  quadra; app de gestão → grade da agenda com as reservas reais nos horários. Dois apps
  do mesmo produto trocam fundo (claro × escuro), tipografia e metáfora; só as cores de
  marca se mantêm.
- **Regras fixas** — prints reais e limpos, nenhum número/nome/status inventado, sem
  emoji, sem gradiente, sem Inter/Roboto/Arial, legendas do projeto literais,
  contraste acessível.
- **Exemplos** — os dois conceitos já aprovados (app do jogador e app do parceiro do
  JoGame) e uma tabela de ideias de conceito para outros tipos de app.
- **Arquivos de apoio** — modelos dos arquivos do canvas (`templates/`) e os scripts
  `limpar_status.py` (apaga ícones de notificação da barra de status) e
  `folha_contato.py` (monta os prints lado a lado para revisão).

### Estrutura

```
store-screenshots/
├── SKILL.md                    # fluxo, estrutura do canvas e regras de layout
├── reference/
│   ├── dados-demo.md           # como popular dados de demonstração
│   ├── captura.md              # Maestro, emulador e simulador
│   ├── canvas-formato.md       # formato dos arquivos do canvas e ordem de publicação
│   └── exemplos.md             # conceitos já usados + tabela de ideias
├── templates/
│   ├── canvas.json
│   ├── Main.dc.html
│   ├── slide.dc.html
│   └── Tablet.dc.html
└── scripts/
    ├── limpar_status.py
    └── folha_contato.py
```

---

## Instalar num computador novo

```bash
git clone git@github.com:steevedevops/may-claude-skills.git ~/may-claude-skills
mkdir -p ~/.claude/skills
ln -s ~/may-claude-skills/store-screenshots ~/.claude/skills/store-screenshots
```

Com o link simbólico, um `git pull` em `~/may-claude-skills` já atualiza a skill.
Sem link, copie a pasta: `cp -R ~/may-claude-skills/store-screenshots ~/.claude/skills/`.

Para usar só num projeto, coloque a pasta em `<projeto>/.claude/skills/`.

## Usar

No Claude Code, peça normalmente — "cria os screenshots da loja para o app X",
"refaz as artes da Play Store" — que a skill entra sozinha. Ou chame direto com
`/store-screenshots`.
