number = 7

per = input("Voce quer jogar, se sim digite 'y' ").lower()

if per == 'y':
    user = int(input("Adivinhe o numero: "))
    if user == number:
        print("Voce acertou!!")

    elif abs(number - user) == 1:
        print("Voce errou por um!!")

    else:
        print("Voce errou!!")
else:
    print("Rode o programa dnv")

#Duplicar os numeros

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

doubled = [x * 2 for x in numbers]

print(doubled)


friends = ["Joao", "Maria", "Marco"]

#cria uma nova lista e coloca todos os elementos que comecam com M
start_s = [ friend for friend in friends if friend.startswith("M")]

print(start_s)
