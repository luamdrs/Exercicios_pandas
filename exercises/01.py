# Criação de um Dataframe básico
import pandas as pd

dados = {
    'Produto': ['Camiseta', 'Calça Jeans', 'Tênis', 'Casaco', 'Boné'],
    'Categoria': ['Vestuário', 'Vestuário', 'Calçados', 'Vestuário', 'Acessórios'],
    'Quantidade': [50, 30, 20, 15, 60],
    'Preço': [29.99, 89.99, 120.00, 150.00, 25.00]
}

estoque = pd.DataFrame(dados)

print(estoque)

print()

# Selecao de dados
# Selecionando a coluna "Produto"
produtos = estoque['Produto']
print(produtos)

print()

# Selecionando as colunas "Produto" e "Quantidade"
produtos_quantidade = estoque[['Produto', 'Quantidade']]
print(produtos_quantidade)

print()

# Selecionando a primeira linha (indexacao baseada em posicao)
primeira_linha = estoque.iloc[0]
print(primeira_linha)

print()

# Selecionando a linha com indice 2 (indexacao baseada em rotulo)
linha_indice_2 = estoque.loc[2]
print(linha_indice_2)

print()

# filtrando um produto baseado em uma condicao "produtos com quantidade maior que 20"
qtd_maior_que_20 = estoque[estoque['Quantidade'] > 20]
print(qtd_maior_que_20)

print()

# filtrando produtos baseados em multiplas condicoes (usamos o & "e" ou | "ou")
# produtos com quantidade maior que 20 e que sao da categoria "Vestuario"
filtro = estoque[(estoque['Quantidade'] > 20) & (estoque['Categoria'] == 'Vestuário')]
print(filtro)