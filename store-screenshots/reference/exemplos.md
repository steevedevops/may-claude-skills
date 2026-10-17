# Exemplos de conceito (já aprovados)

Dois apps do mesmo produto (JoGame: app do jogador e app do parceiro/dono de quadra),
mesmas cores de marca (índigo #383BB4, laranja #ED5B23, navy #1A2B5E), conceitos
opostos.

## A. App do jogador — "quadra"

- Fundo claro #F1F2FF. Fundo contínuo: a marcação de um campo inteiro (retângulo,
  linha do meio, círculo central no print do meio, áreas nas pontas) em #D6DAFB, 5 px,
  atravessando os 7 prints.
- Trajetória de bola pontilhada laranja (`stroke-dasharray="2 14"`) passando por trás
  dos devices, terminando numa bola no último print.
- Números 01–07 enormes vazados (168 px, `color: transparent;
  -webkit-text-stroke: 2px` laranja claro) no canto superior direito de cada print.
- Barlow Condensed 800 itálico MAIÚSCULO nos títulos (46–50 px, line-height .95),
  Barlow 500 no subtítulo.
- Devices em pé, moldura #15173F, sangrando pela base.
- Fichas: brancas com ícone em círculo (status), pílula índigo (cidade), bloco laranja
  com número grande em Barlow Condensed ("10 VAGAS / R$ 17,14 por pessoa"), balão de
  chat com uma mensagem real, selo verde "Verificado".
- Recurso gráfico: meia quadra + título + dois devices à direita + ficha laranja.

## B. App do parceiro — "agenda da semana"

- Fundo escuro navy #1A2B5E. Fundo contínuo: grade de agenda — linhas de hora
  (14h…22h, 56 px por hora, rótulos 11 px a 40 % de opacidade) e uma coluna por print.
- Cada print é um DIA (eyebrow "SÁB · 17 OUT" em Space Grotesk 13 px, espaçado,
  laranja) e mostra a reserva real daquele dia como bloco posicionado no horário certo,
  metade sobre o device: laranja sólido = confirmado, tracejado laranja sobre azul =
  pendente; dia sem expediente = bloco tracejado "Local fechado".
- Space Grotesk 700 nos títulos (40–42 px), Manrope no corpo, #B9C3E6 no subtítulo.
- Devices retos, moldura #0B1533 com borda branca a 14 %.
- KPIs só com números do print (receita semanal, avaliação, nº de reservas) em
  cartões brancos com texto navy.
- Hero: ícone + "JoGame" com "Jo" laranja + "PARCEIRO" espaçado embaixo.

## Como derivar um conceito novo

Pergunte "qual objeto do dia a dia do usuário representa esse app?" e transforme-o em
fundo contínuo + um dado real por print encaixado nesse objeto:

| Tipo de app | Fundo contínuo | Dado por print |
|---|---|---|
| Agenda / reservas | grade de horários | reserva real no horário |
| Esporte / jogo | marcação de quadra/campo | placar, vagas, status |
| Finanças | linha de gráfico atravessando | saldo/valor real da tela |
| Entrega / mobilidade | rota pontilhada com paradas | ETA, status do pedido |
| Saúde / treino | linha de batimento / trilha | série, minutos, meta |
| Educação | linhas de caderno / trilha de módulos | progresso, nota |
| Vistoria / checklist | papel quadriculado / planta baixa | item vistoriado, foto |
