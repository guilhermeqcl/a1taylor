import pandas as pd
import numpy as np

########################################### FUNÇÕES INTERNAS ##################################################

# Retorna as n linhas do dataframe com os maiores valores (ordenados do maior para o menor) do parâmetro passado
def get_bottom(df, parameter, n):
    return df.sort_values(by=parameter).head(n)

# Retorna as n linhas do dataframe com os menores valores (ordenados do menor para o maior) do parâmetro passado
def get_top(df, parameter, n):
    return df.sort_values(by=parameter, ascending=False).head(n)

# Recebe uma coluna de um dataframe composta por strings ("df"), quebra-a em "elementos" de acordo com o separador ("delimiter")
# passado e retorna um dataframe com uma coluna, onde cada linha é um elemento 
def get_elements(df, delimiter):
    set = []
    for row in df:
        for element in row.split(delimiter):
            # Remove caracteres indesejados da string
            element = element.strip('[],.;!"?()- ').capitalize()
            if len(element) > 0:
                set.append(element)
    return pd.DataFrame(set)[0]

# Retorna as n palavras que mais ocorrem nas entradas (strings) de um dataframe composto por uma coluna
def count_words(df): 
    words_df = get_elements(df, " ")
    return words_df.value_counts().head(5)

# Conta quantas vezes uma string ("title" - o titulo da musica ou album) ocorre nas letras ("df["Lyrics"]) e em quantas 
# musicas ocorre ao menos uma vez
def count_repetitions(df, title):
    freq = 0
    count = 0
    real_title = " " + remove_useless(title.lower()) + " "
    for track_lyrics in df["Lyrics"]:
        low = clean_string(track_lyrics)
        freq += low.count(real_title)
        if real_title in low:
            count += 1
            
    return [freq, count]

# Recebe uma string e retorna uma nova string onde todas as palavras que continham "(" ou ")" foram removidas
# Ex.: Red (Deluxe Edition) --> Red 
def remove_useless(string):
    new_str = ""
    for k in string.split(" "):
        if "(" not in k and ")" not in k:
            new_str += k + " "

    return new_str.strip(" ")

# Recebe uma string, deixa-a toda em letras minusculas e remove um conjunto de caracteres
def clean_string(string):
    string = string.lower()
    for k in '"!?-.,:;()[]/':
        string = string.replace(k, "")
    string = " " + string + " "
    return string

######################################## FUNÇÕES PARA RESPONDER AS QUESTÕES #########################################

# Printa uma tabela com as musicas mais longas e mais curtas de cada album
def length_by_album(df, album):
    top = get_top(df.loc[df["Album"] == album], "Length", 3)
    bottom = get_bottom(df.loc[df["Album"] == album], "Length", 3)
    print(f"{album} - músicas mais longas:\n", top[["Title", "Length"]], "\n")
    print(f"{album} - músicas mais curtas:\n", bottom[["Title", "Length"]], "\n\n")

# Printa uma tabela com as musicas mais populares e menos populares de cada album 
def streams_by_album(df, album):
    top = get_top(df.loc[df["Album"] == album], "Streams", 3)
    bottom = get_bottom(df.loc[df["Album"] == album], "Streams", 3)
    print(f"{album} - músicas mais ouvidas:\n", top[["Title", "Streams"]], "\n")
    print(f"{album} - músicas menos ouvidas:\n", bottom[["Title", "Streams"]], "\n\n")

# Printa uma tabela com as musicas mais longas e mais curtas dentre toda a discografia
def length_all(df):
    top = get_top(df, "Length", 3)
    bottom = get_bottom(df, "Length", 3)
    print("Músicas mais longas:\n", top[["Title", "Album", "Length"]], "\n")
    print("Músicas mais curtas:\n", bottom[["Title", "Album", "Length"]], "\n\n")

# Printa uma tabela com as musicas com mais streams e menos streams dentre toda a discografia
def streams_all(df):
    top = get_top(df, "Streams", 3)
    bottom = get_bottom(df, "Streams", 3)
    print("Músicas mais ouvidas:\n", top[["Title", "Album", "Streams"]], "\n")
    print("Músicas menos ouvidas:\n", bottom[["Title", "Album", "Streams"]], "\n\n")

# Printa uma tabela com os albuns com mais premios
def prizes_by_album(df):
    col_list = ["Grammy", "American Music Awards", "Billboard Music Awards", "MTV Video Music Awards", "World Music Awards", "Brit Awards"]
    df["Total Prizes"] = df[col_list].sum(axis=1)  
    print("Albuns mais premiados:\n", get_top(df, "Total Prizes", 4)[["Album", "Total Prizes"]])
  
# Printa o Coeficiente de Correlação de Pearlson e define o grau de correlação
def correlation_test(df, var1, var2):
    correlation_coef = np.corrcoef(df[var1].to_numpy(), df[var2].to_numpy())[0][1]
    print(f"Coeficiente de correlação de Pearlson ({var1} e {var2}): {correlation_coef}")

  
# Printa as 5 palavras mais comuns nos titulos dos álbuns
def words_album(df): 
    print("Palavras mais comuns nos titulos dos álbuns: ", count_words(df["Album"].unique()))

# Printa as 5 palavras mais comuns nos titulos das músicas
def words_title(df):
    print("Palavras mais comuns nos titulos das músicas: ", count_words(df["Title"]))

# Printa, para cada álbum, as 5 palavras mais comuns nas letras das musicas
def words_lyrics_by_album(df, album):
    lyrics = get_elements(df.loc[df["Album"] == album]["Lyrics"], " // ")
    print(f"{album} - palavras mais comuns")
    print(count_words(lyrics), "\n")

# Printa as 5 palavras mais comuns nas letras das musicas de toda a discografia
def words_lyrics_all(df):
    lyrics = get_elements(df["Lyrics"], " // ")
    print("Toda a discografia - palavras mais comuns")
    print(count_words(lyrics), "\n")

# Printa, para cada album, quantas vezes o titulo do album ocorre nas letras das musicas e em quantas musicas ele ocorre.
def album_title_in_lyrics(df):
    for album in df["Album"].unique():
        album_tracks = df.loc[df["Album"] == album]
        tracks_number = len(album_tracks.index)
        info = count_repetitions(album_tracks, album)
        print(f"{album}: \nNumero total de vezes que o titulo ocorre nas letras: {info[0]}\nQuantidade de músicas que contem o titulo do álbum: {info[1]} de {tracks_number}\n")

# Printa o numero médio de vezes que o titulo de uma música ocorre nas letras e a porcentagem de músicas que contém seu título na letra
def track_title_in_lyrics(df):
    appearances_list = [count_repetitions(df.loc[df["Title"] == track], track.split(" - ")[0])[0] for track in df["Title"]]
    tracks_with_appearence = sum([1 for x in appearances_list if x != 0])
    print("Número médio de vezes que o titulo de uma música ocorre nas letras:", round(sum(appearances_list)/df["Title"].size, 2))
    print("Porcentagem de músicas que contém o título na letra:", round(100*tracks_with_appearence/df["Title"].size, 2))