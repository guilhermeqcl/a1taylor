import pandas as pd
import numpy as np

class InexistentAlbum(Exception):
    """Raised when the input 'album' argument is not an album in dataset"""
    pass

class InexistentColumn(Exception):
    """Raised when a input argument is not an column in the dataset"""
    pass

class NonPositiveValue(Exception):
    """Raised when the input value is not a positive integer"""
    pass

########################################### FUNÇÕES INTERNAS ##################################################

# Retorna as n linhas do dataframe com os maiores valores (ordenados do maior para o menor) do parâmetro passado
def get_bottom(df, parameter, n):
    """Retorna as n linhas do dataframe com os maiores valores (ordenados do maior para o menor) do parâmetro passado
    :param df: Dataframe
    :type df: pd.Dataframe
    :param parameter: Nome da coluna do Dataframe
    :type parameter: string
    :param n: Número de linhas retornado
    :type n: int
    :return: Dataframe ordenado
    :rtype: pd.Dataframe
    """  
    return df.sort_values(by=parameter).head(n)

# Retorna as n linhas do dataframe com os menores valores (ordenados do menor para o maior) do parâmetro passado
def get_top(df, parameter, n):
    """Função que retorna as n linhas do dataframe com os menores valores (ordenados do menor para o maior) do parâmetro passado.
    :param df: Dataframe
    :type df: pd.Dataframe
    :param parameter: Nome da coluna do Dataframe
    :type parameter: string
    :param n: Número de linhas retornado
    :type n: int
    :return: Dataframe ordenado
    :rtype: pd.Dataframe
    """ 
    return df.sort_values(by=parameter, ascending=False).head(n)

# Recebe uma coluna de um dataframe composta por strings ("df"), quebra-a em "elementos" de acordo com o separador ("delimiter")
# passado e retorna um dataframe com uma coluna, onde cada linha é um elemento 
def get_elements(df, delimiter):
    """Função que recebe uma coluna de um dataframe composta por strings ("df"), quebra-a em "elementos" de acordo com o separador ("delimiter") passado e retorna um dataframe com uma coluna, onde cada linha é um elemento. 
    :return: Dataframe com uma coluna
    :rtype: pandas.core.series.Series
    """    
    set = []
    ignore = ['I', 'i', 'The', 'the', 'And', 'and', 'To', 'to', 'Me', 'me', 'feat', 'Feat',
              'A', 'a', 'It', 'it', 'In', 'in', 'My', 'my', 'Of', 'of', 'That', 'that', 'This', '&',
              'this','All', 'all', "I'm", "i'm", 'But', 'but', 'On', 'on', 'Be', 'be', 'Is', 'is', 'demo',
              'So', 'so','Oh', 'oh', 'Was', 'was', "It's", "it's", 'When', 'when', 'Just', 'just', 'Demo',
              "You're", "you're", 'For', 'for', 'With', 'with', 'What', 'what', "Don't", "don't", 'Up', 
              'up', 'Back', 'back', 'If', 'if', 'Out', 'out', "'Cause","'cause", 'At', 'at', 'Are', 'are', 
              'Deluxe', 'Edition', 'Platinum', 'Di', 'di', 'Edition', 'edition', 'deluxe', 'Deluxe']

    for row in df:
        for element in row.split(delimiter):
            # Remove caracteres indesejados da string
            element = element.strip('[],.;!"?()- ').capitalize()
            if len(element) > 0 and element not in ignore:
                set.append(element)

    return pd.DataFrame(set)[0]

# Retorna as n palavras que mais ocorrem nas entradas (strings) de um dataframe composto por uma coluna
def count_words(df, n):
    """Função que retorna as n palavras que mais ocorrem nas entradas (strings) de um dataframe composto por uma coluna.

    :param df: Dataframe
    :type df: pd.Dataframe
    :param n: Número de linhas
    :type n: int
    :return: Dataframe com o número de palavras
    :rtype: pd.Dataframe
    """
    words_df = get_elements(df, " ")
    return words_df.value_counts().head(n)

# Conta quantas vezes uma string ("title" - o titulo da musica ou album) ocorre nas letras ("df["Lyrics"]) e em quantas 
# musicas ocorre ao menos uma vez
def count_repetitions(df, title):
    """Função que conta quantas vezes uma string ("title" - o titulo da musica ou album) ocorre nas letras ("df["Lyrics"]) e em quantas musicas ocorre ao menos uma vez.
    :param df: Dataframe   
    :type df: pd.Dataframe
    :param title: Título das músicas
    :type title: string
    :return: Retorna uma Lista
    :rtype: list
    """    
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
    """Função que recebe uma string e retorna uma nova string onde todas as palavras que continham "(" ou ")" foram removidas.

    :return: Palavras filtradas
    :rtype: String
    """ 
    new_str = ""
    for k in string.split(" "):
        if "(" not in k and ")" not in k:
            new_str += k + " "

    return new_str.strip(" ")

# Recebe uma string, deixa-a toda em letras minusculas e remove um conjunto de caracteres
def clean_string(string):
    """Função que recebe uma string, deixa-a toda em letras minusculas e remove um conjunto de caracteres.

    :return: Conjunto de letras
    :rtype: string
    """    
    string = string.lower()
    for k in '"!?-.,:;()[]/':
        string = string.replace(k, "")
    string = " " + string + " "
    return string

######################################## FUNÇÕES PARA RESPONDER AS QUESTÕES #########################################

# Printa uma tabela com as musicas mais longas e mais curtas de um album especifico
def length_by_album(df, album, n):
    """Função que printa uma tabela com as músicas mais longas e mais curtas de cada álbum.

    :param df: Dataframe
    :type df: pd.Dataframe
    :param album: Álbum de músicas
    :type album: string
    :param n: Número de linhas
    :type n: int
    :raises InexistentAlbum: exceção  
    :raises NonPositiveValue: exceção
    """
    try:
        if album not in df["Album"].unique():
            raise InexistentAlbum
        if n <= 0:
            raise NonPositiveValue

        top = get_top(df.loc[df["Album"] == album], "Length", n)
        bottom = get_bottom(df.loc[df["Album"] == album], "Length", n)
        print(f"{album} - músicas mais longas:\n", top[["Title", "Length"]], "\n")
        print(f"{album} - músicas mais curtas:\n", bottom[["Title", "Length"]], "\n\n")
    except InexistentAlbum:
        print("Erro: album inexistente")
    except NonPositiveValue:
        print("Erro: inteiro passado não é positivo")
    except KeyError:
        print("Erro: dataframe passado não é o correto")

# Printa uma tabela com as n musicas mais populares e menos populares de um album especifico 
def streams_by_album(df, album, n):
    """Função que printa uma tabela com as músicas mais populares e menos populares de cada album.

    :param df: Dataframe
    :type df: pd.Dataframe
    :param album: Album de músicas 
    :type album: String
    :param n: Número de linhas
    :type n: int
    :raises InexistentAlbum: exceção
    :raises NonPositiveValue: exceção
    """
    try:
        if album not in df["Album"].unique():
            raise InexistentAlbum
        if n <= 0:
            raise NonPositiveValue

        top = get_top(df.loc[df["Album"] == album], "Streams", n)
        bottom = get_bottom(df.loc[df["Album"] == album], "Streams", n)
        print(f"{album} - músicas mais ouvidas:\n", top[["Title", "Streams"]], "\n")
        print(f"{album} - músicas menos ouvidas:\n", bottom[["Title", "Streams"]], "\n\n")
    except InexistentAlbum:
        print("Erro: album inexistente")
    except NonPositiveValue:
        print("Erro: inteiro passado não é positivo")
    except KeyError:
        print("Erro: dataframe passado não é o correto")

# Printa uma tabela com as n musicas mais longas e mais curtas dentre toda a discografia
def length_all(df, n):
    """Função que printa uma tabela com as músicas mais longas e mais curtas dentre toda a discografia

    :param df: Dataframe
    :type df: pd.Dataframe
    :param n: mnúmero de linhas
    :type n: int
    :raises NonPositiveValue: exceção
    """
    try:
        if n <= 0:
            raise NonPositiveValue
        top = get_top(df, "Length", n)
        bottom = get_bottom(df, "Length", n)
        print("Músicas mais longas:\n", top[["Title", "Album", "Length"]], "\n")
        print("Músicas mais curtas:\n", bottom[["Title", "Album", "Length"]], "\n\n")

    except NonPositiveValue:
        print("Erro: inteiro passado não é positivo")
    except KeyError:
        print("Erro: dataframe passado não é o correto")

# Printa uma tabela com as n musicas com mais streams e menos streams dentre toda a discografia
def streams_all(df, n):
    """Função que printa uma tabela com as músicas com mais streams e menos streams dentre toda a discografia

    :param df: Dataframe
    :type df: pd.Dataframe
    :param n: número de linhas
    :type n: int
    :raises NonPositiveValue: exceção
    """
    try:
        if n <= 0:
            raise NonPositiveValue
        top = get_top(df, "Streams", n)
        bottom = get_bottom(df, "Streams", n)
        print("Músicas mais ouvidas:\n", top[["Title", "Album", "Streams"]], "\n")
        print("Músicas menos ouvidas:\n", bottom[["Title", "Album", "Streams"]], "\n\n")

    except NonPositiveValue:
        print("Erro: inteiro passado não é positivo")
    except KeyError:
        print("Erro: dataframe passado não é o correto")

# Printa uma tabela com os albuns com mais premios
def albums_prizes(df, n):
    """Função que printa uma tabela com os albuns com mais premios.

    :param df: Dataframe
    :type df: pd.Dataframe
    :param n: número de linhas
    :type n: int
    :raises NonPositiveValue: exceção
    """
    try:
        if n <= 0:
            raise NonPositiveValue
        col_list = ["Grammy", "American Music Awards", "Billboard Music Awards", "MTV Video Music Awards", "World Music Awards", "Brit Awards"]
        df["Total Prizes"] = df[col_list].sum(axis=1)  
        print("Albuns mais premiados:\n", get_top(df, "Total Prizes", n)[["Album", "Total Prizes", "Grammy", "American Music Awards", "Billboard Music Awards", "MTV Video Music Awards", "World Music Awards", "Brit Awards"]])
    except NonPositiveValue:
        print("Erro: inteiro passado não é positivo")
    except KeyError:
        print("Erro: dataframe passado não é o correto")
  
# Printa o Coeficiente de Correlação de Pearlson e define o grau de correlação, dado um dataframe e duas de suas colunas, compostas de valores numéricos
def correlation_test(df, var1, var2):
    """Função que printa o coeficiente de correlação de pearlson e define o grau de correlação 

    :param df: Dataframe
    :type df: pd.Dataframe
    :param var1: Nome de colunas do Dataframe composta de valores
    :type var1: Strings
    :param var2: Nome de colunas do Dataframe composta de valores
    :type var2: Strings
    :raises InexistentColumn: exceção
    """
    try:
        if var1 not in list(df) or var2 not in list(df):
            raise InexistentColumn
        correlation_coef = np.corrcoef(df[var1].to_numpy(), df[var2].to_numpy())[0][1]
        print(f"Coeficiente de correlação de Pearlson ({var1} e {var2}): {correlation_coef}")
        modl = abs(correlation_coef)
        if modl < 0.3:
            print("Correlação desprezível\n")
        elif modl < 0.5:
            print("Correlação fraca\n")
        elif modl < 0.7:
            print("Correlação média\n")
        elif modl < 0.9:
            print("Correlação forte\n")
        else:
            print("Correlação muito forte\n")

    except InexistentColumn:
        print("Erro: coluna passada não existe no dataframe passado")
    except TypeError:
        print("Erro: coluna passada não é composta estritamente de valores numéricos")
  
# Printa as n palavras mais comuns nos titulos dos álbuns
def words_album(df, n): 
    """Função que printa as 5 palavras mais comuns nos títulos dos albuns.

    :param df: Dataframe
    :type df: pd.Dataframe
    :param n: número de linhas
    :type n: int
    :raises NonPositiveValue: exceção
    """
    try:
        if n <= 0:
            raise NonPositiveValue
        print(f"Palavras mais comuns nos titulos dos álbuns:\n")
        print(count_words(df["Album"].unique(), n))
    except NonPositiveValue:
        print("Erro: inteiro passado não é positivo")
    except KeyError:
        print("Erro: dataframe passado não é o correto")

# Printa as n palavras mais comuns nos titulos das músicas
def words_title(df, n):
    """Função que printa as 5 paalvras mais comuns nos títulos das músicas.

    :param df: Dataframe
    :type df: pd.Dataframe
    :param n: número de linhas
    :type n: int
    :raises NonPositiveValue: exeção
    """
    try:
        if n <= 0:
            raise NonPositiveValue
        print("Palavras mais comuns nos titulos das músicas:")
        print(count_words(df["Title"], n))
    except NonPositiveValue:
        print("Erro: inteiro passado não é positivo")
    except KeyError:
        print("Erro: dataframe passado não é o correto")

# Printa, dado certo álbum, as n palavras mais comuns nas letras das musicas
def words_lyrics_by_album(df, album, n):
    """Função que printa, para cada álbum, as n palavras mais comuns nas letras das musicas. 

    :param df: Dataframe
    :type df: pd.Dataframe
    :param album: Album de músicas
    :type album: String
    :param n: número de palavras
    :type n: int
    :raises InexistentAlbum: exceção
    :raises NonPositiveValue: exceção
    """    
    try:
        if album not in df["Album"].unique():
            raise InexistentAlbum
        if n <= 0:
            raise NonPositiveValue
        lyrics = get_elements(df.loc[df["Album"] == album]["Lyrics"], " // ")
        print(f"{album} - palavras mais comuns")
        print(count_words(lyrics, n), "\n")

    except NonPositiveValue:
        print("Erro: inteiro passado não é positivo")
    except KeyError:
        print("Erro: dataframe passado não é o correto")
    except InexistentAlbum:
        print("Erro: album inexistente")

# Printa as n palavras mais comuns nas letras das musicas de toda a discografia
def words_lyrics_all(df, n):
    """Função que printa as n palavras mais comuns nas letras das músicas de toda a discografia

    :param df: Dataframe
    :type df: pd.Dataframe
    :param n: número de palavras
    :type n: int
    :raises NonPositiveValue: exceção
    """    
    try:
        if n <= 0:
            raise NonPositiveValue
        lyrics = get_elements(df["Lyrics"], " // ")
        print("Toda a discografia - palavras mais comuns")
        print(count_words(lyrics, n), "\n")
    except NonPositiveValue:
        print("Erro: inteiro passado não é positivo")
    except KeyError:
        print("Erro: dataframe passado não é o correto")
    
# Printa, para cada album, quantas vezes o titulo do album ocorre nas letras das musicas e em quantas musicas ele ocorre, e diz se é recorrente ou não.
def album_title_in_lyrics(df, album):
    """Função que printa, para cada album, quantas vezes o título do album ocorre nas letras das músicas e em quantas músicas ele ocorre.

    :param df: Dataframe
    :type df: pd.Dataframe
    :param album: Album de músicas
    :type album: String
    :raises InexistentAlbum: execeção
    """    
    try:
        if album not in df["Album"].unique():
            raise InexistentAlbum
        album_tracks = df.loc[df["Album"] == album]
        tracks_number = len(album_tracks.index)
        info = count_repetitions(album_tracks, album)
        print(f"{album}: \nNumero total de vezes que o titulo ocorre nas letras: {info[0]}\nQuantidade de músicas que contem o titulo do álbum: {info[1]} de {tracks_number}")
        if info[0] > tracks_number*5 and info[1] > tracks_number/2:
            print("Titulo do album recorrente nas letras\n")
        else:
            print("Titulo do album NÃO recorrente nas letras\n")
    except InexistentAlbum:
        print("Erro: album inexistente")
    except KeyError:
        print("Erro: dataframe passado não é o correto")

# Printa o numero médio de vezes que o titulo de uma música ocorre nas letras e a porcentagem de músicas que contém seu título na letra
def track_title_in_lyrics(df):
    """Função que printa o numero médio de vezes que o titulo de uma música ocorre nas letras e a porcentagem de músicas que contém seu título na letra.

    :param df: Dataframe
    :type df: pd.Dataframe
    """
    try: 
        appearances_list = [count_repetitions(df.loc[df["Title"] == track], track.split(" - ")[0])[0] for track in df["Title"]]
        tracks_with_appearence = sum([1 for x in appearances_list if x != 0])
        print("Número médio de vezes que o titulo de uma música ocorre nas letras:", round(sum(appearances_list)/df["Title"].size, 2))
        print("Porcentagem de músicas que contém o título na letra:", round(100*tracks_with_appearence/df["Title"].size, 2))
        if sum(appearances_list)/df["Title"].size > 5 and 100*tracks_with_appearence/df["Title"].size > 50:
            print("O titulo das músicas é recorrente nas letras\n")
        else:
            print("O titulo das musicas não é recorrente nas letras\n")

    except KeyError:
        print("Erro: dataframe passado não é o correto")

# Printa uma tabela com as n musicas mais e menos 'dançáveis' dentre toda a discografia
def danceability_all(df, n):
    """Função que printa uma tabela com as n musicas mais e menos 'dançáveis' dentre toda a discografia.

    :param df: Dataframe
    :type df: pd.Dataframe
    :param n: Número de músicas
    :type n: int
    :raises NonPositiveValue: exceção
    """    
    try:
        if n <= 0:
            raise NonPositiveValue
        top = get_top(df, "Danceability", n)
        bottom = get_bottom(df, "Danceability", n)
        print("Músicas mais 'dançáveis':\n", top[["Title", "Album", "Danceability"]], "\n")
        print("Músicas menos 'dançáveis':\n", bottom[["Title", "Album", "Danceability"]], "\n\n")

    except NonPositiveValue:
        print("Erro: inteiro passado não é positivo")
    except KeyError:
        print("Erro: dataframe passado não é o correto")

# Printa uma tabela com as n musicas mais e menos 'positivas' dentre toda a discografia
def valence_all(df, n):
    """Printa uma tabela com as n musicas mais e menos 'positivas' dentre toda a discografia    

    :param df: Dataframe    
    :type df: pd.Dataframe
    :param n: Número de músicas
    :type n: int
    :raises NonPositiveValue: exeção
    """    
    try:
        if n <= 0:
            raise NonPositiveValue
        top = get_top(df, "Valence", n)
        bottom = get_bottom(df, "Valence", n)
        print("Músicas mais 'positivas':\n", top[["Title", "Album", "Valence"]], "\n")
        print("Músicas menos 'positivas':\n", bottom[["Title", "Album", "Valence"]], "\n\n")

    except NonPositiveValue:
        print("Erro: inteiro passado não é positivo")
    except KeyError:
        print("Erro: dataframe passado não é o correto")

# Printa uma tabela com as n musicas mais e menos 'dançáveis' de um album especifico
def danceability_by_album(df, album, n):
    """Printa uma tabela com as n musicas mais e menos 'dançáveis' de um album especifico

    :param df: Dataframe
    :type df: pd.Dataframe
    :param album: Album de músicas
    :type album: String
    :param n: Número de músicas
    :type n: int
    :raises InexistentAlbum: Exceção
    :raises NonPositiveValue: _description_
    """    
    try:
        if album not in df["Album"].unique():
            raise InexistentAlbum
        if n <= 0:
            raise NonPositiveValue

        top = get_top(df.loc[df["Album"] == album], "Danceability", n)
        bottom = get_bottom(df.loc[df["Album"] == album], "Danceability", n)
        print(f"{album} - músicas mais 'dançáveis':\n", top[["Title", "Danceability"]], "\n")
        print(f"{album} - músicas menos 'dançáveis':\n", bottom[["Title", "Danceability"]], "\n\n")
    except InexistentAlbum:
        print("Erro: album inexistente")
    except NonPositiveValue:
        print("Erro: inteiro passado não é positivo")
    except KeyError:
        print("Erro: dataframe passado não é o correto")

# Printa uma tabela com as n musicas mais e menos 'positivas' de um album especifico
def valence_by_album(df, album, n):
    """Printa uma tabela com as n musicas mais e menos 'positivas' de um album especifico.

    :param df: Datafrmae
    :type df: pd.Dataframe
    :param album: Album de músicas
    :type album: String
    :param n: Número de músicas
    :type n: int
    :raises InexistentAlbum: exceção
    :raises NonPositiveValue: exceção
    """    
    try:
        if album not in df["Album"].unique():
            raise InexistentAlbum
        if n <= 0:
            raise NonPositiveValue

        top = get_top(df.loc[df["Album"] == album], "Valence", n)
        bottom = get_bottom(df.loc[df["Album"] == album], "Valence", n)
        print(f"{album} - músicas mais 'positivas':\n", top[["Title", "Valence"]], "\n")
        print(f"{album} - músicas menos 'positivas':\n", bottom[["Title", "Valence"]], "\n\n")
    except InexistentAlbum:
        print("Erro: album inexistente")
    except NonPositiveValue:
        print("Erro: inteiro passado não é positivo")
    except KeyError:
        print("Erro: dataframe passado não é o correto")