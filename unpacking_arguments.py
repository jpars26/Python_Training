
# O *args faz com que a função receba qual quer numero de argumentos
def mutiply(*args):
    total = 1
    for arg in args:
        total = total * arg

    return total
    
def apply (*args, operator):

    if operator == "*":
        return mutiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provide apply()"

print(apply(1,2,3, operator = "*"))