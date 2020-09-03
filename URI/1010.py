A, B, C = input("Valores 1: ").split(' ')
D, E, F = input("Valores 2: ").split(' ')

A = int(A)
B = int(B)
C = float(C)
D = int(D)
E = int(E)
F = float(F)

result =  (B * C) + (E * F)
print('VALOR A PAGAR: R$ {:.2f}'.format(result))

