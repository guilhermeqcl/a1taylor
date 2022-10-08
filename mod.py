import pandas as pd

def length_streams_n_dance(df, parameter, n):
    min = df.sort_values(by=parameter).head(n)
    max = df.sort_values(by=parameter, ascending=False).head(n)

    return max, min

def get_elements(df, delimiter):
    set = []
    ignore = [ 'I', 'i', 'The', 'the', 'And', 'and', 'To', 'to', 'Me', 'me', 'feat', 'Feat',
              'A', 'a', 'It', 'it', 'In', 'in', 'My', 'my', 'Of', 'of', 'That', 'that', 'This', '&',
              'this','All', 'all', "I'm", "i'm", 'But', 'but', 'On', 'on', 'Be', 'be', 'Is', 'is', 'demo',
              'So', 'so','Oh', 'oh', 'Was', 'was', "It's", "it's", 'When', 'when', 'Just', 'just', 'Demo',
              "You're", "you're", 'For', 'for', 'With', 'with', 'What', 'what', "Don't", "don't", 'Up', 
              'up', 'Back', 'back', 'If', 'if', 'Out', 'out', "'Cause","'cause", 'At', 'at', 'Are', 'are']
    for row in df:
        for element in row.split(delimiter):
            if element != "-" and element not in ignore:
                set.append(element.strip('[],.;!"?()').capitalize())
    return pd.DataFrame(set)[0]

def count_words(df): 
    words_df = get_elements(df, " ")
    return words_df.value_counts().head(10)