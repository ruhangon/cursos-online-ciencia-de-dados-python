import pandas as pd

dataset = pd.read_csv('C:/data/db.csv', sep = ';', index_col=0)
# pd.set_option('display.max_rows', 10)
# pd.set_option('display.max_columns', 10)

print(dataset.head())

novo_dataset_loc = dataset.loc[['Passat', 'DS5'], ['Ano', 'Valor']]
print(novo_dataset_loc.head())

novo_dataset_iloc = dataset.iloc[[0, 2]]
print(novo_dataset_iloc.head())

# print(dataset.Motor == 'Motor Diesel')

carros_zero_km = dataset.query('Zero_km == True')
print(carros_zero_km.head())

for index, row in dataset.iterrows():
    if (2019 - row['Ano'] != 0):
        dataset.loc[index, 'Km_media'] = row['Quilometragem'] / 2019 - row['Ano']
    else:
        dataset.loc[index, 'Km_media'] = 0

print(dataset.head())

# print(dataset[['Quilometragem', 'Valor']].describe())

print(dataset.info())

# verifica valores NA dentre as quilometragens
print(dataset[dataset.Quilometragem.isna()])

# troca valores NA por 0 e mantem isso
dataset.fillna(0, inplace = True)
print(dataset.head())

