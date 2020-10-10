jogos = ['crash', 'zelda', 'donkey kong', 'mario']
videogames = ['playstation', 'nintendo', 'nintendo', 'nintendo']

print(jogos.index('zelda'))

dados = {'crash': 'playstation', 'zelda': = 'nintendo', 'donkey kong': 'nintendo', 'mario': 'nintendo'}
print(dados)

novos_dados = dict(zip(jogos, videogames))
print(novos_dados)

novos_dados['spyro'] = 'playstation'
print(novos_dados)

del novos_dados['donkey kong']
print(novos_dados)

novos_dados.update({"donkey kong': 'nintendo'})
print(novos_dados)

dados_copia=novos_dados.copy()
dados_copia.pop('crash', 'chave não encontrada')
print(dados_copia)

for key in novos_dados.keys():
    print(novos_dados[key])

print(novos_dados.itens())

