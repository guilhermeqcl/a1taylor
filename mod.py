import pandas as pd

def length_streams_n_dance(df, parameter, n):
    min = df.sort_values(by=parameter).head(n)
    max = df.sort_values(by=parameter, ascending=False).head(n)

    return max, min

def get_elements(df, delimiter):
    set = []
    for row in df:
        for element in row.split(delimiter):
            if element != "-":
                set.append(element.strip('[],.;!"?()').capitalize())
    return pd.DataFrame(set)[0]

def count_words(df): 
    words_df = get_elements(df, " ")
    return words_df.value_counts().head(5)