
print('----- CONJUNTOS e SUBCONJUNTOS de elementos -----') #RNW

conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
#junção dos dois conjuntos
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))
# Saber qual número se repete
conjuto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjuto_interseccao))
conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))


print('----- SUBSET E SUPERSET -----') #RWN
#subset (subconjunto do conjunto)

conjunto_a = {1, 2, 3,}
conjunto_b = {1, 2, 3, 4, 5, 6}
conjunto_subset = conjunto_a.issubset(conjunto_b)
# o conjunto a tem todos os componentes que o conjunto b portanto é TRUE. se o B tem mais componentes que o A-
# portanto é FALSE.
conjunto_superset = conjunto_b.issuperset(conjunto_a)
# o conjunto b tem todos os componentes que o conjunto a portanto é TRUE. se o a tem menos componentes que o B-
# portanto é FALSO.
print('A é um subconjunto de B: {}'.format(conjunto_subset))
print('B é um superconjunto de A: {}'.format(conjunto_superset))

#Como remover a duplicidade de um conjunto
lista = ('cachorro', 'cachorro', 'gato', 'gato', 'avestruz', 'peixe')
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
#Voltar para a lista sem duplicidades
lista_animais = list(conjunto_animais)
print(lista_animais)



###############################
############# RNW  ############
###############################