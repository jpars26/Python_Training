
n = int(input("Entre com o valor: "))

n1 =0
n2=0
n5=0
n10=0
n20=0
n50=0
n100=0

while n != 0:
    if n >= 100:
        n = n - 100
        n100 = n100 + 1
    elif n >= 50:
        n = n - 50
        n50 = n50 + 1
    elif n >= 20:
        n = n - 20
        n20 = n20 +1
    elif n >= 10:
        n10 = n10 +1
    elif n >= 5:
        n = n - 5
        n5 = n5 +1
    elif n >=2:
        n = n- 2
        n2 = n2+1
    else:
        n = n -1
        n1 = n1 + 1

print(f"{n100} nota(s) de R$ 100,00,\n{n50} nota(s) de R$ 50,00, \n{n20} nota(s) de R$ 20,00,\n{n10} nota(s) de R$ 10,00,\n{n5} nota(s) de R$ 5,00,\n{n2} nota(s) de R$ 2,00,\n{n1} nota(s) de R$ 1,00")
