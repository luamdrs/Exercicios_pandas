# Dataframe com listas aninhadas

import pandas as pd

notas = [
    [8.5, 9.0, 7.0],
    [8.8, 7.6, 9.2],
    [9.2, 8.5, 8.9], 
    [7.0, 8.0, 6.5],
    [9.5, 9.0, 9.3]
]

nomes = ['Ana', 'Alice', 'Pedro', 'João', 'Maria']

df_notas = pd.DataFrame(notas, columns=['1ª Prova', '2ª Prova', '3ª Prova'], index=nomes)

df_notas['Média'] = df_notas.mean(axis=1).round(1)

print(df_notas)