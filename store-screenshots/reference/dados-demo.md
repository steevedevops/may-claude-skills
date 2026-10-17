# Dados de demonstração

Objetivo: cada tela do conjunto mostra o produto em uso, com gente de verdade, sem
nada vazio, falso ou constrangedor.

## 1. Auditoria antes de mexer

Abra cada tela do conjunto no device e anote:

- listas vazias ("Nenhuma partida encontrada", "Nenhum grupo ainda")
- pendências e banners que cobrem a tela ("Ação necessária", "Cadastro em análise")
- nomes técnicos (`jeep-kite-scenic`, `tester`, `user123`), e-mail no lugar do nome
- lorem ipsum em descrições, regras, bios
- fotos ruins: câmera do emulador (sala virtual com xadrez), parede, foto pessoal do dono
- números que contradizem outras telas

Se o projeto usa produção, peça autorização explícita antes de criar ou alterar dados.

## 2. Criar dados pela API do app

- Leia as rotas do backend (ex.: `urls.py`, `routes/`) e os serializers de payload;
  use os mesmos endpoints que o app chama, com o token de login da conta demo.
- `curl` funciona; `urllib` do Python pode levar 403 do proxy/WAF: mande um
  `User-Agent` próprio. Python do macOS sem certificados: use
  `SSL_CERT_FILE=$(python -c 'import certifi;print(certifi.where())')`.
- No zsh, arrays começam em 1 (`T=($(cat tokens)); ${T[1]}`).
- Ordem que costuma resolver:
  1. Resolver pendências que geram banner (encerrar partida antiga, aprovar cadastro — se
     só o admin aprova, peça ao usuário).
  2. Renomear as contas demo (nome + sobrenome reais), bio curta, cidade.
  3. Criar os itens principais (partidas, reservas, pedidos…) em datas futuras próximas
     (hoje, amanhã, próximos dias) e em horários plausíveis.
  4. Do lado parceiro/admin, confirmar parte deles e deixar parte pendente — os dois
     estados aparecem nas telas.
  5. Conversas: mandar 2–5 mensagens curtas e naturais entre as contas.
  6. Fotos: trocar as fotos de câmera de emulador por fotos CC0.

## 3. Contas extras de demonstração (outros usuários)

Listas como "pessoas perto de você" costumam mostrar contas reais (inclusive a do dono).
Não edite contas de terceiros. Crie 2–3 contas novas — listas ordenadas por
`criado_em desc` passam a mostrá-las primeiro:

- E-mail temporário com API: mail.tm (`GET /domains`, `POST /accounts`, `POST /token`,
  `GET /messages`, `GET /messages/{id}`). O mail.tm REMOVE pontos do endereço: use o
  `address` devolvido pelo `POST /accounts`.
- Cadastro → ler o código de 6 dígitos do e-mail → verificar → atualizar perfil.
- Faça essas contas participarem dos itens (entrar nas partidas, reservar): os cards
  passam de "1/14" para "4/14", fica vivo.
- Guarde as credenciais num arquivo do scratchpad e informe o caminho ao usuário.

## 4. Fotos

- Wikimedia Commons API, filtrando licença CC0 / domínio público (dispensam crédito):
  `action=query&generator=search&gsrnamespace=6&prop=imageinfo&iiprop=url|size|extmetadata&iiurlwidth=1600`
  e checar `extmetadata.LicenseShortName`. Mande `User-Agent` com contato.
- Unsplash bloqueia busca automática; Commons tem muitas fotos "(Unsplash)" em CC0.
- Evite marcas visíveis (bola com logo) e rostos de desconhecidos como se fossem usuários.
- Avatar sem foto boa: gere um avatar de iniciais na cor da marca (PIL, 600×600,
  fonte do app) — fica profissional e coerente com os avatares de inicial do app.
- Monte uma folha de contato das candidatas e escolha olhando.

## 5. Notificações antigas com nomes feios

Se a API não deixa apagar notificações, empurre-as para fora da tela gerando
notificações novas e reais (reservas e mensagens das contas demo). Atenção:
- notificações do mesmo chat costumam ser agrupadas (uma por conversa);
- a tela do tablet mostra ~25 itens; conte a posição da primeira notificação ruim
  pela API até ela passar disso.
