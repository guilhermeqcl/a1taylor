import seaborn as sns
import pandas as pd
import mod
import matplotlib.pyplot as plt

df = pd.read_csv("./data/def.csv", delimiter="$")
premios = pd.read_csv("./data/albuns.csv")

#GRÁFICOS POR ÁLBUM
for album in df["Album"].unique():
        musicas_album = df.loc[df["Album"] == album]

        #GRÁFICOS DE POPULARIDADE
        sns.barplot(data = musicas_album.sort_values(by='Popularity', ascending=False), y='Title', x='Popularity').set(title=(f'Popularidade das músicas do álbum {album}'))
        plt.show()

        #GRÁFICOS DE DURAÇÃO
        sns.barplot(data = musicas_album.sort_values(by='Length', ascending=False), y='Title', x='Length').set(title=(f'Durações das músicas do álbum {album}'))
        plt.show()

#GRÁFICO DE DURAÇÃO DE TODOS OS TEMPOS
longest_all = mod.get_top(df[['Title','Album','Length', 'Popularity']], "Length", 5)
shortest_all = mod.get_bottom(df[['Title','Album','Length', 'Popularity']], "Length", 5)

duration_all = pd.concat([longest_all, shortest_all], axis=0)

sns.barplot(data = duration_all.sort_values(by='Length', ascending=False), y='Title', x='Length').set(title=(f'Música mais longas e mais curtas de todas'))
plt.show()

#GRÁFICO DE POPULARIDADE DE TODOS OS TEMPOS
most_popular = mod.get_top(df[['Title','Album','Length', 'Popularity']], "Popularity", 5)
least_popular = mod.get_bottom(df[['Title','Album','Length', 'Popularity']], "Popularity", 5)

popularity_all = pd.concat([most_popular, least_popular], axis=0)

sns.barplot(data = popularity_all.sort_values(by='Popularity', ascending=False), y='Title', x='Popularity').set(title=(f'Música mais populares e menos populares de todas'))
plt.show()

#GRÁFICOS DOS PRÊMIOS
col_list = ["Grammy", "American Music Awards", "Billboard Music Awards", "MTV Video Music Awards", "World Music Awards", "Brit Awards"]
premios["Total Prizes"] = premios[col_list].sum(axis=1)

sns.barplot(data = premios.sort_values(by='Total Prizes', ascending=False), y='Album', x='Total Prizes').set(title=(f'Prêmios acumulados de cada álbum'))
plt.show()

#GRÁFICOS DA CORRELAÇÃO POPULARIDADE-DURAÇÃO
musicas_all = df[['Title','Album','Length', 'Popularity']]
sns.scatterplot(data = musicas_all, y='Popularity', x='Length').set(title=(f'Correlação da popularidade com a duração das músicas'))
plt.show()

#GRÁFICO DA CORRELAÇÃO DANÇABILIDADE-POSITIVIDADE
musicas_all = df[['Title','Album','Danceability', 'Valence']]
sns.scatterplot(data = musicas_all, y='Danceability', x='Valence').set(title=(f'Correlação da dançabilidade com a positividade das músicas'))
plt.show()