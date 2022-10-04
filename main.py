import mod
import pandas as pd

def main():
    data = open("./data/def.csv", "r", encoding="utf-8")
    df = pd.read_csv(data, delimiter="$")
    title_in_lyrics(df)

def length_by_album(df):
    for album in df["Album"].unique():
        select = mod.MinMaxLengthAndPop(df.loc[df["Album"] == album], "Length")
        print(f"{album} - músicas mais longas:\n", select[0][["Title", "Length"]], "\n")
        print(f"{album} - músicas mais curtas:\n", select[1][["Title", "Length"]], "\n\n")

def streams_by_album(df):
    for album in df["Album"].unique():
        select = mod.MinMaxLengthAndPop(df.loc[df["Album"] == album], "Streams")
        print(f"{album} - músicas mais ouvidas:\n", select[0][["Title", "Streams"]], "\n")
        print(f"{album} - músicas menos ouvidas:\n", select[1][["Title", "Streams"]], "\n\n")

def length_all(df):
    select = mod.MinMaxLengthAndPop(df, "Length")
    print("Músicas mais longas:\n", select[0][["Title", "Album", "Length"]], "\n")
    print("Músicas mais curtas:\n", select[1][["Title", "Album", "Length"]], "\n\n")

def streams_all(df):
    select = mod.MinMaxLengthAndPop(df, "Streams")
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
            
main()