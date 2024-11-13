# definindo um indice personalizado

import pandas as pd

df = {
    'Produto': ['Camisa', 'Shorts', 'Calça Jeans', 'Tênis', 'Relógio', 'Boné'],
    'Quantidade': [20, 25, 15, 30, 50, 27],
    'Preço': [39.99, 29.99, 120.00, 99.99, 79.99, 39.99]
}

estoque_loja = pd.DataFrame(df)

estoque_loja.set_index('Produto', inplace=True)

print(estoque_loja)

# acessando o produto diretamente
print(estoque_loja.loc['Boné'])