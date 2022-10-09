import mod
import pandas as pd

# Abertura dos arquivos com o dataset
main_data = open("./data/def.csv", "r", encoding="utf-8")
albuns = open("./data/albuns.csv", "r", encoding="utf-8")

# Leitura dos dados
df = pd.read_csv(main_data, delimiter="$")
albums = pd.read_csv(albuns)

# Execução das funções que respondem as questões propostas
    ##### PARTE 1 ######
print("======================== PARTE 1 =========================")
print("========== Questão 1 =========")
#for album in df["Album"].unique():
#    mod.length_by_album(df, album, 10)
print("========== Questão 2 =========")
for album in df["Album"].unique():
    mod.streams_by_album(df, album, 2000)
print("========== Questão 3 =========")
mod.length_all(df, 10)
print("========== Questão 4 =========")
mod.streams_all(df, 10)
print("========== Questão 5 =========")
mod.albums_prizes(albums, 10)
print("========== Questão 6 =========")
mod.correlation_test(df, "Length", "Popularity")


    ##### PARTE 2 #####
print("======================== PARTE 2 =========================")
print("========== Questão 1 =========")    
mod.words_album(df, 10)
print("========== Questão 2=========")
mod.words_title(df, 10)
print("========== Questão 3 =========")
for album in df["Album"].unique():
    mod.words_lyrics_by_album(df, album, 10)
print("========== Questão 4 =========")
mod.words_lyrics_all(df, 10)
print("========== Questão 5 =========")
for album in df["Album"].unique():
    mod.album_title_in_lyrics(df, album)
print("========== Questão 6 =========")
mod.track_title_in_lyrics(df)

    ##### PARTE 3 #####
print("======================== PARTE 3 =========================")
print("========== Questão 1 =========")
mod.danceability_all(df, 10)
print("========== Questão 2 =========")
for album in df["Album"].unique():
    mod.danceability_by_album(df, album, 10)
print("========== Questão 3 =========")
mod.valence_all(df, 10)
print("========== Questão 4 =========")
for album in df["Album"].unique():
    mod.valence_by_album(df, album, 10)
print("========== Questão 5 =========")
mod.correlation_test(df, "Valence", "Danceability")

# Fechamento dos arquivos
main_data.close()
albuns.close()