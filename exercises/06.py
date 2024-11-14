# indexacao com loc e iloc 

import pandas as pd

dados = {
    'Cidade': ['João Pessoa', 'Recife', 'Teresina', 'Fortaleza', 'Belo Horizonte', 'Curitiba', 'São Paulo'],
    'População': [888679, 4305130, 1059660, 2574412, 6300410, 3697928, 44411238],
    'Área (km²)': [211, 218, 138, 314, 331, 430, 1521]
}

df_cidades = pd.DataFrame(dados)
df_cidades.set_index('Cidade', inplace=True)

info_loc = df_cidades.loc['Recife']
print('Informações usando loc para Recife:\n', info_loc)

info_iloc = df_cidades.iloc[0]
print('\nInformações usando iloc para o primeiro índice:\n', info_iloc)