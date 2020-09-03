
# # O .lower() transforma toda a string em letras minusculas
# day_of_week = input("what day of the week is it today?").lower()

# if day_of_week == "monday":
#     print("Cool")
# elif day_of_week =="tuesday":
#     print("Great")
# else:
#     print("LOL")


movie_whatched = {"Matrix", "Piratas", "Rei Lao"}
user_movie = input("Enter something you've whatched recently: ")

if user_movie in movie_whatched:
    print(f"I've whatched {user_movie} too!!")
else:
    print("I haven't whatched that yet!")