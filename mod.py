import pandas as pd

def length_n_streams(df, parameter):
    min = df.sort_values(by=parameter).head(3)
    max = df.sort_values(by=parameter, ascending=False).head(3)

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