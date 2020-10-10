    nomes_de_jogos=('crash', 'zelda', 'donkey kong', 'mario')

jogo_1, jogo_2, jogo_3, jogo_4 = nomes_de_jogos
# jogo_1 irá se referir ao primeiro item da lista nomes_de_jogos, jogo_2 ao segundo e assim por diante

lista_nintendo=nomes_de_jogos[1:]

for i in lista_nintendo:
    print(i)

_, _, _, jogo_mais_famoso=nomes_de_jogos
# dessa forma consigo salvar apenas o Mario, último elemento da tupla, em uma variável

print('jogo mais famoso: {}'.format(jogo_mais_famoso))

videogames=('playstation', 'nintendo', 'nintendo', 'nintendo')

for jogo, videogame in zip(nomes_de_jogos, videogames):
    print(jogo, videogame)



