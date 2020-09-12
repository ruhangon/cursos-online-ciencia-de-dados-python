import numpy as np

contador=np.arange(10)
for i in contador:
    print(i)

pares=contador[0:-1:2]
for i in pares:
    print(i)

km = np.array([19000., 14000., 58000., 29000., 9000.])
anos = np.array([2000, 2005, 1990, 1990, 2010])

dados = np.array([km, anos])

print(dados[1][4])

km_media = dados[0] / (2019 - dados[1])

print(km_media)

km_lista=km.tolist()
# km_lista recebe uma lista convertida do array
anos_lista=anos.tolist()
# anos_lista recebe uma lista convertida do array

info_carros=km_lista+anos_lista

print(np.array(info_carros))

print(np.array(info_carros).reshape((2, 5)))

novos_dados=dados.copy()

novos_dados.resize((3, 5), refcheck=False)
# refcheck=false faz com que o numpy não cheque a referência ao criar a nova linha, pois nesse caso daria erro sem isso

novos_dados[2] = novos_dados[0] / (2019 - novos_dados[1])
# a nova linha criada agora receberá as informações de km média

print(novos_dados)

