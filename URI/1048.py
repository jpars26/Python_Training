salario = float(input())

per = [15, 12, 10, 7, 4]

if salario <= 400.00:
    aux2 = per[0]
    aux = salario * (per[0]/100)
    salario = aux + salario

    
elif salario <= 800.00:
    aux2 = per[1]
    aux = salario * (per[1]/100)
    salario = aux + salario

elif salario <= 1200.00:
    aux2 = per[2]
    aux = salario * (per[2]/100)
    salario = aux + salario

elif salario <= 2000.00:
    aux2 = per[3]
    aux = salario * (per[3]/100)
    salario = aux + salario


elif salario > 2000.00:
    aux2 = per[4]    
    aux = salario * (per[4]/100)
    salario = aux + salario
    
print("Novo salario: {:.2f}".format(salario))
print("Reajuste ganho: {:.2f}".format(aux))
print(f"Em percentual: {aux2} %" )

