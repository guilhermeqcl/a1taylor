import mod
import pandas as pd
import numpy as np

def main():
    data = open("./data/def.csv", "r", encoding="utf-8")
    df = pd.read_csv(data, delimiter="$")
    title_in_lyrics(df)
    length_by_album(df)

def length_by_album(df):
    for album in df["Album"].unique():
        select = mod.length_streams_n_dance(df.loc[df["Album"] == album], "Length", 1)
        print(f"{album} - músicas mais longas:\n", select[0][["Title", "Length"]], "\n")
        print(f"{album} - músicas mais curtas:\n", select[1][["Title", "Length"]], "\n\n")

def streams_by_album(df):
    for album in df["Album"].unique():
        select = mod.length_streams_n_dance(df.loc[df["Album"] == album], "Streams", 1)
        print(f"{album} - músicas mais ouvidas:\n", select[0][["Title", "Streams"]], "\n")
        print(f"{album} - músicas menos ouvidas:\n", select[1][["Title", "Streams"]], "\n\n")

def length_all(df):
    select = mod.length_streams_n_dance(df, "Length", 1)
    print("Músicas mais longas:\n", select[0][["Title", "Album", "Length"]], "\n")
    print("Músicas mais curtas:\n", select[1][["Title", "Album", "Length"]], "\n\n")

def streams_all(df):
    select = mod.length_streams_n_dance(df, "Streams", 1)
    print("Músicas mais ouvidas:\n", select[0][["Title", "Album", "Streams"]], "\n")
    print("Músicas menos ouvidas:\n", select[1][["Title", "Album", "Streams"]], "\n\n")

def words_album(df):
    print("Palavras mais comuns nos titulos dos álbuns: ", mod.count_words(df["Album"].unique()))

def words_title(df):
    print("Palavras mais comuns nos titulos das músicas: ", mod.count_words(df["Title"]))

def words_lyrics_by_album(df):
    for album in df["Album"].unique():
        lyrics = mod.get_elements(df.loc[df["Album"] == album]["Lyrics"], " // ")
        print(f"{album} - palavras mais comuns")
        print(mod.count_words(lyrics), "\n")

def words_lyrics_all(df):
    lyrics = mod.get_elements(df["Lyrics"], " // ")
    print("Toda a discografia - palavras mais comuns")
    print(mod.count_words(lyrics), "\n")

def title_in_lyrics(df):
    for word in mod.get_elements(df["Title"], " "):
        if word not in ["Edition", "Deluxe", "Platinum", "Feat"]:
            pass

def danceability_by_album(df):
    for album in df["Album"].unique():
        select = mod.length_streams_n_dance(df.loc[df["Album"] == album], "Danceability", 1)
        print(f"{album} - músicas mais dançáveis:\n", select[0][["Title", "Danceability"]], "\n")

def prizes_by_album(df):
    col_list = ["Grammy", "American Music Awards", "Billboard Music Awards", "MTV Video Music Awards", "World Music Awards", "Brit Awards"]
    df["Total Prizes"] = df[col_list].sum(axis=1)  
    print("Albuns mais premiados:\n", mod.length_streams_n_dance(df, "Total Prizes", 4)[0][["Album", "Total Prizes"]])

def correlation_test(df):
    correlation_matrix = np.corrcoef(df["Length"].to_numpy(), df["Streams"].to_numpy())
    print(correlation_matrix)
            
main()