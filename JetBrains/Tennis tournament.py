n = int(input())

lista = []
a=0
for i in range(n):
    name = input().split()
    if name[1] == 'win':
        lista.append(name[0])
        a = a + 1

print(lista)
print(a)
