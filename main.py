import mod
import pandas as pd
import numpy as np

# Abertura dos arquivos com o dataset
main_data = open("./data/def.csv", "r", encoding="utf-8")
albuns = open("./data/albuns.csv", "r", encoding="utf-8")

# Leitura dos dados
df = pd.read_csv(main_data, delimiter="$")
albums = pd.read_csv(albuns)

# Execução das funções que respondem as questões propostas
mod.correlation_test(df)

# Fechamento dos arquivos
main_data.close()
albuns.close()
