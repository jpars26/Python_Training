
listas = [
    (1, "Cachorro Quente", 4.00),
    (2, "X-Salada", 4.50),
    (3, "X-Bacon", 5.00),
    (4, "Torrada Simples", 2.00),
    (5, "Refigerante", 1.50),
    ]


b,c = input("Entre com os valores: ").split()

b = int(b)
c = int(c)

for lista in listas:
    if lista[0] == b:
        print("Total: R$ {:.2F}".format(lista[2] * c))
        break
  
