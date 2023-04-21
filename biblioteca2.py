# 2° Biblioteca chamada pandas, uma das principais usadas em manipulação, analise, ciência de dados.

import pandas as pd

data = {'Nome': ['João', 'Maria', 'Pedro', 'Lucas'],
        'Idade': [25, 30, 18, 40],
        'Sexo': ['M', 'F', 'M', 'M']}

df = pd.DataFrame(data)

# Selecionando apenas a coluna 'Nome'
nomes = df['Nome']
print(nomes)

# Selecionando apenas as linhas em que a idade é maior ou igual a 30
mais_velhos = df[df['Idade'] >= 30]
print(mais_velhos)