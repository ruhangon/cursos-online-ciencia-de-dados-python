import pandas as pd

dataset = pd.read_csv('C:/data/db.csv', sep = ';')
# pd.set_option('display.max_rows', 10)
# pd.set_option('display.max_columns', 10)

# print(dataset)

print(dataset[['Quilometragem', 'Valor']].describe())
# calcula estatísticas descritivas em cima do que for pedido

print(dataset.info())

