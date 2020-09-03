a = int(input())
b = int(input())

lista = []

for lst in range(a, b + 1):
    lista.append(lst)
    
lista2 = []

for aux in lista:
    if aux % 3 == 0:
        lista2.append(aux)

calculo = sum(lista2) / len(lista2)

print(calculo)
