import pandas as pd
import numpy as np

# 1. Ler o conjunto de dados para um DataFrame
df = pd.read_csv("/Users/lucasbatista/My-Drive-batistalucasdev/lucasbatista_ifpi/TEP/atividade-pandas-1/heart.csv")

# 2. Verificar as primeiras linhas do DataFrame usando head()
print("2. Primeiras linhas:")
print(df.head())

# 3. Verificar as últimas linhas do DataFrame usando tail()
print("\n3. Últimas linhas:")
print(df.tail())

# 4. Verificar as dimensões do DataFrame usando shape
print("\n4. Dimensões do DataFrame:")
print(df.shape)

# 5. Verificar as informações sobre as colunas do DataFrame usando info()
print("\n5. Informações sobre o DataFrame:")
print(df.info())

# 6. Verificar as estatísticas descritivas básicas do DataFrame usando describe()
print("\n6. Estatísticas descritivas:")
print(df.describe())

# 7. Verificar dados ausentes
print("\n7. Verificação de dados ausentes por coluna:")
print(df.isnull().sum())

# 8. Selecionar uma coluna específica como array Numpy (exemplo: idade)
idade_array = df['age'].to_numpy()
print("\n8. Coluna 'age' como array NumPy:")
print(idade_array)

# 9. Selecionar duas ou mais colunas como DataFrame (exemplo: 'age' e 'chol')
colunas_selecionadas = df[['age', 'chol']]
print("\n9. Duas colunas como DataFrame:")
print(colunas_selecionadas.head())

# 10. Selecionar linha específica com loc (exemplo: índice 10)
print("\n10. Linha com índice 10:")
print(df.loc[10])

# 11. Selecionar linhas com base em condições (exemplo: idade > 50 e colesterol > 200)
condicoes = df.loc[(df['age'] > 50) & (df['chol'] > 200)]
print("\n11. Linhas com idade > 50 e colesterol > 200:")
print(condicoes)
