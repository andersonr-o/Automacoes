# Automações

Esse repositório tem como objetivo expor o meu conhecimento em automações utilizando linguagens de programação como Python e Visual Basic, por exemplo.

## Automações em Python:

  1. IMDbMovies_py - Extraindo informações de filmes do site IMDb:

       Nessa automação feita com python, utilizando selenium e pandas, entramos no site do IMDb e extraímos informações como:
     
       * Nome do filme;
       * Ano de lançamento;
       * Duração;
       * Avaliação;
       * Descrição.
  
     Após jogar esses dados para um array, utilizamos o pandas para tabulação e conversão dos dados em excel.
     Dentro da pasta, há um exemplo da planilha que é gerada ao final de todo o processo.

## Automações em VB:

  1. arrumaImagens_VB - Posicionando imagens em um documento Word:

  Essa automação feita em VB tem como propósito definir duas imagens por página no documento Word, cada uma delas ocupando metade da folha.
  
  (Se quiser saber a história por trás da criação dessa automação, navegue até a página que contém seu script e leia a descrição.)

  O seu funcionamento é simples. O código irá pegar as proporções da folha do Word (altura e largura) e depois multiplicará cada uma das imagens existentes na folha e multiplicar por 0,5 em relação ao tamanho da página, fazendo com que fique duas imagens por folha.
