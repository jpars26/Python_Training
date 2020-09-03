a, b ,c = input().split()

a = float(a)
b = float(b)
c = float(c)

lst = [a,b,c]
lst.sort(key=float, reverse=True)

soma_BC = lst[1] + lst[2]

reserva = lst[0]

lst[0] = lst[0] ** 2
lst[1] = lst[1] ** 2
lst[2] = lst[2] ** 2


result = lst[1] + lst[2]

if reserva >= soma_BC:
    print("NAO FORMA TRIANGULO")
elif lst[0] == result:
    print("TRIANGULO RETANGULO")
elif lst[0] > result:
    print("TRIANGULO OBTUSANGULO")
elif lst[0] < result:
    print("TRIANGULO ACUTANGULO")

if a == b and a == c:
    print("TRIANGULO EQUILATERO")
elif a == b or b == c or c == a:
    print("TRIANGULO ISOSCELES")
