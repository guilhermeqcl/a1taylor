import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

df = pd.read_csv("./data/def.csv", delimiter="$")
stopwords = STOPWORDS
stopwords.update(['I', 'i', 'The', 'the', 'And', 'and', 'To', 'to', 'Me', 'me', 'feat', 'Feat',
              'A', 'a', 'It', 'it', 'In', 'in', 'My', 'my', 'Of', 'of', 'That', 'that', 'This', '&',
              'this','All', 'all', "I'm", "i'm", 'But', 'but', 'On', 'on', 'Be', 'be', 'Is', 'is', 'demo',
              'So', 'so','Oh', 'oh', 'Was', 'was', "It's", "it's", 'When', 'when', 'Just', 'just', 'Demo',
              "You're", "you're", 'For', 'for', 'With', 'with', 'What', 'what', "Don't", "don't", 'Up', 
              'up', 'Back', 'back', 'If', 'if', 'Out', 'out', "'Cause","'cause", 'At', 'at', 'Are', 'are', 
              'Deluxe', 'Edition', 'Platinum', 'Di', 'di'])

#NUVEM DOS TÍTULOS DAS MÚSICAS
wc_titles = WordCloud(background_color='white', stopwords=stopwords).generate(' '.join(df['Title']))
plt.imshow(wc_titles)
plt.axis("off")
plt.savefig("./images/wordclouds/titles_cloud.png", dpi=600)

#NUVEM DAS LETRAS DAS MÚSICAS POR ÁLBUM
for album in df['Album'].unique():
    lyrics_album = df.loc[df["Album"] == album]
    wc_lyrics_albums = WordCloud(background_color='white', stopwords=stopwords, ).generate(' '.join(lyrics_album['Lyrics']))
    plt.imshow(wc_lyrics_albums)
    plt.axis("off")
    plt.savefig((f"./images/wordclouds/{album}_cloud.png"), dpi=600)

#NUVEM DAS LETRAS DAS MÚSICAS
wc_lyrics = WordCloud(background_color='white', stopwords=stopwords).generate(' '.join(df['Lyrics']))
plt.imshow(wc_lyrics)
plt.axis("off")
plt.savefig("./images/wordclouds/lyrics_cloud.png", dpi=600)