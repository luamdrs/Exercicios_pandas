# criando um dataframe vazio e adicionando colunas manualmente

import pandas as pd

estoque = pd.DataFrame()

estoque['Produto'] = ['Caneta', 'Caderno', 'Mochila']
estoque['Categoria'] = ['Papelaria', 'Papelaria', 'Acessórios']
estoque['Quantidade'] = [100, 50, 20]

print(estoque)