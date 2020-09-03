# O **argument ela coleta os argumentos nomeados em um dicionario ou podem ser usados em uma chamada de função para descompactar um dicionario em argumentos

def named(**kwargs):
    print(kwargs)

def print_necely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_necely(name="Joao", age=25)

#Pode usar os dois juntos 

def both(*args, **kwards):
    print(args)
    print(kwards)

both(1,2,3,5,6, name="Jpars", age=25)