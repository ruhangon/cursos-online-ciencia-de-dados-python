jogos = ['uncharted', 'the last of us', 'GTA', 'FIFA']
print('tamanho da lista jogos: {}'.format(len(jogos)))
print(('overwatch' in jogos))
# in retorna true se esse conteúdo está na lista

nova_colecao=['call of duty', 'overwatch']
nova_colecao=nova_colecao+jogos
print('tamanho da nova coleção: {}'.format(len(nova_colecao)))
print('o último elemento da nova coleção é: {}'.format(nova_colecao[-1]))
print(('overwatch' in nova_colecao))

colecao_dividida=nova_colecao[0:2]
# cria uma lista nova, com as inclusões dos elementos 0 e 1, 2 não está contido]
print('o primeiro item da coleção dividida é: {}'.format(colecao_dividida[0]))

notebook = ['Dell', 'i5', 2000]
videogame=['playstation 4 slim', 2000]
compras=[notebook, videogame]
print('a primeira informação do primeiro item das compras é: {}'.format(compras[0][0]))

print('o último item da nova coleção sem ordenação é: {}'.format(nova_colecao[-1]))
nova_colecao.sort()
print('o último item da nova coleção ordenada é: {}'.format(nova_colecao[-1]))

nova_colecao.append('god of war')
print('o último item que foi adicionado a nova coleção é: {}'.format(nova_colecao[-1]))

nova_colecao.pop()
print('o último item foi excluído e agora voltou a ser: {}'.format(nova_colecao[-1]))

colecao_de_teste=nova_colecao.copy()
colecao_de_teste.append('forza')

print(len(nova_colecao))
print(len(colecao_de_teste))

