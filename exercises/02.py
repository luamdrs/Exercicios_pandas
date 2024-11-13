# Criando um Dataframe a partir de um dicionario

import pandas as pd

df = {
    'Produto': ['Camisa', 'Shorts', 'Calça Jeans', 'Tênis', 'Relógio', 'Boné'],
    'Quantidade': [20, 25, 15, 30, 50, 27],
    'Preço': [39.99, 29.99, 120.00, 99.99, 79.99, 39.99]
}

estoque_loja = pd.DataFrame(df)

estoque_loja['Valor Total'] = estoque_loja['Quantidade'] * estoque_loja['Preço']
print(estoque_loja)

valor_total_produtos = estoque_loja['Valor Total'].sum()

print(f'\nValor total dos produtos: R${valor_total_produtos:.2f}')