a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)

lst = [a, b, c]
sorted(lst, key=int)
for lista in lst:
    print(lista)

print(" ")

for lista2 in lst:
    print(lst)

