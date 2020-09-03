

n = int(input("Entre com o valor: "))

n1 = n / 3600
n2 = n1 * 60
n3 = n % 60

print(f"{n1:.0f}:{n2:.0f}:{n3:.0f}")
