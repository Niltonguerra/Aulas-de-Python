# lista = [1,3,5,7]
# lista_de_animais= ['cachorro','cão','animal','totó']
# print(lista_de_animais)
#
#soma = 0
# for x in lista:         contador de números na lista
#     print(x)
#     soma += x
#     print(soma)
#
# for x in lista_de_animais:        #escreve todos os itens da lista
#     print(x)

# print(sum(lista))                 #psoma todos os item da lista
# print(max(lista))                 #pega o maior valor da lista
# print(min(lista))                 #pega o menor valor da lista
# print(min(lista_de_animais))      #pega o menor valor da lista, aqui como é alfabético fica como a letra mais próxima de A
#
# nova_lista = lista_de_animais * 3
# print(nova_lista)


# if 'lobo' in lista_de_animais:              #procura um item na lista
#     print('existe um lobo na lista')
# else:
#     print('não existe um lobo na lista')
#     lista_de_animais.append('lobo')       #acrescenta um item a lista
#     print(lista_de_animais)
#
# lista_de_animais.pop(4)     #tira o ultimo item da lista ou o qual você indicar a posição nos parentes
# print(lista_de_animais)
#
# lista.sort(lista_de_animal)                  #coloca a lista em ordem crescente
# print(lista_de_animais)
#
# lista.reverse(lista_de_animais)              #coloca a lista em ordem decrescente
# print(lista_de_animais)
#
#
# tupla = (1,2,15,89)                            #A tuple é imutavel, não é possivel alterar os item nela
# print(len(tupla))                              #serve para descobrir quantos item tem uma lista/tuple
#
# animais = tuple(lista_de_animais)             #transforma lista em tuple
# animais_lista = list(animais)                 #transforma em lista
#
# print(type(lista_de_animais))                 #mostra o tipo da varialvel
#
#
# conjunto = {1,2,3,4,5,6}                      #conjunto
# conjunto.add(7)                               #adiciona itens
# conjunto.discard(7)                           #revome itens

#
# conjunto1 = {1,2,3,4,5,6,7}
# conjunto2 = {7,8,9}
# conjunto_uniao = conjunto1.union(conjunto2)    #uni os conjuntos
# conjuntointerseccao = conjunto1.intersection(conjunto2)    #pega o que tem nos dois
# conjuntodiferentes = conjunto1.difference(conjunto2)      #pega tudo mesmos o que tem no segundo conjunto referido
# conjuntodiferentes2 = conjunto2.difference(conjunto1)
# conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2) #pega tudo menos o que tem nos dois
# print(conjunto_diff_simetrica)
# print(conjuntodiferentes2)
# print(conjuntodiferentes)
# print(conjuntointerseccao)
# print(conjunto_uniao)



#
# conjuntoa = {1,2,3}
# conjuntob = {1,2,3,4,5,6}
# conjunto_subset = conjuntoa.issubset(conjuntob)          #verifica se o primeiro está contido no segundo
# conjunto_superset = conjuntob.issuperset(conjuntoa)      #verifica se o primeiro está contendo no segundo
# print(conjunto_superset)
# print(conjunto_subset)

# lista = ['cachorro', 'cachorro', 'gato','lobo','elefante']           #converter de lista para conjunto tira a duplicidade
# conjunto_animais = set(lista)
# lista_animais =list(conjunto_animais)
# print(lista_animais)

