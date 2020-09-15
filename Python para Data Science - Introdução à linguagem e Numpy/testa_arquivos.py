import numpy as np

anos = np.loadtxt(fname = "C:/data/carros-anos.txt", dtype = int)
km = np.loadtxt(fname = "C:/data/carros-km.txt")
valor = np.loadtxt(fname = "C:/data/carros-valor.txt")

print(anos.shape)
print(km.shape)
print(valor.shape)

dataset = np.column_stack((anos, km, valor))
# column_stack transforma um array unidimensional em colunas de um array bidimensional

print(dataset.shape)

print(np.mean(dataset[:,1]))
print(np.mean(dataset[:,2]))
# mean calcula a média

print(np.std(dataset[:,2]))
# std calcula o desvio padrão

print(np.sum(dataset, axis = 0))
# sum calcula a soma

