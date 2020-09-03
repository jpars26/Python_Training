a = input()
B = list(a)

print('---------')
print(f"| {B[0]} {B[1]} {B[2]} |")
print(f"| {B[3]} {B[4]} {B[5]} |")
print(f"| {B[6]} {B[7]} {B[8]} |")
print('---------')

listaX = []
listaO = []
lista_ = []

for matriz in B:

    if matriz == 'X':
        listaX.append(matriz)
        print(listaX)
    if matriz == 'O':
        listaO.append(matriz)
        print(listaO)
            
