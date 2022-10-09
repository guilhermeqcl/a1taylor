Nesse projeto, realizamos uma análise da discografia da cantora americana Taylor Swift. Os códigos feitos avaliam as durações, popularidades, dançabilidade, positividade das músicas;  Utilizamos as bibliotecas Seaborn, Matplotlib, WordCloud para codificar as partes de visualização gráfica das perguntas.
## Instalando as bibliotecas:
Abra o terminal da IDE que você está utilizando
- Digite “pip install seaborn” para instalar o Seaborn
- Digite “pip install matplotlib” para instalar o Matplotlib
- Digite “pip install wordcloud” para instalar o WordCloud
## DataFrame:

Para construir o DF, utilizamos o API do Spotify que possuía informações diversas sobre as músicas. Para as letras das músicas, conseguimos um arquivo .csv que contém as letras de todas as músicas da artista, corrigimos alguns detalhes como:
Um álbum estava fora de ordem pois estava contado como Taylor’s Version, uma versão regravada do álbum que a Taylor Swift anda fazendo recentemente com seus álbuns, desconsideramos essas regravações.

Consideramos somente as versões originais dos álbuns, exceto de Fearless e Red que só haviam as versões Platinum e Deluxe, respectivamente.

Além disso, os versos das músicas estavam separadas por cédulas, então fizemos um script para juntar todos os versos de cada música e então adicionamos ao DF como a coluna Lyrics

Há dois arquivos que constituem o dataset, que está na pasta data: def.csv e albuns.csv.
## Código:
O projeto é dividido em 4 arquivos:

O arquivo main.py é o que deve ser rodado para a ver as respostas das perguntas. O mod.py é o arquivo onde todas as funções foram definidas para que pudéssemos responder as perguntas. O arquivo graficos.py constrói a visualização das perguntas do Grupo 1 de perguntas com o auxílio das bibliotecas Seaborn e Matplotlib. Por último, o arquivo cloud.py constrói as nuvens de palavras da segunda, terceira e quarta pergunta do Grupo 2 de perguntas com o uso da biblioteca WordCloud e Matplotlib. 

As imagens geradas pelos arquivos de visualização gráfica estão numa pasta chamada images, separadas por: comparisons, length, popularity, wordclouds
