#LISTAS


#Pode adicionar e remover 
lista = [0,2,5,8,6,3,21,5,8,2,1]

#Não pode alterar depois de cirada
tupla = (0,3,5,4,8)

#Pode adicionar elementos, mas nao pode elemento duplicado
conjunto = {0,5,2,3,8,6}
conjunto2= {0,5,2,9,10,11}

#Mostra os elementos que estão nos dois conjuntos
juncao = conjunto.intersection(conjunto2)

#Compara os dois conjuntos e mostra qual elemento é diferente
juncao2 = conjunto.difference(conjunto2)

#Agrupa os dois conjuntos e os elementos repetidos são eliminados 
juncao3 = conjunto.union(conjunto2)


print(juncao)
print(juncao2)
print(juncao3)


friends = ["Joao", "Marco", "Anna"]
abroad = ["Joao", "Marco", "Anna"]

print(friends == abroad)

#Verifica se dois elementos são a mesma coisa, nao se eles tem o mesmos elementos dentro
print(friends is abroad)

#o comparador IN compara se tem o elemento na lista e tambem compara um string de entrada se tem na lista
print("Joao" in friends)

