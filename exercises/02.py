# Criando um Dataframe a partir de um dicionario

import pandas as pd

dados = {
    'Produto': ['Camisa', 'Shorts', 'Calça Jeans', 'Tênis', 'Relógio', 'Boné'],
    'Quantidade': [20, 25, 15, 30, 50, 27],
    'Preço': [39.99, 29.99, 120.00, 99.99, 79.99, 39.99]
}

estoque_loja = pd.DataFrame(dados)

print(estoque_loja)