users = [
   (0, "Bob", "password"),
   (1, "Joao", "123456"),
   (2, "Maria", "32656"),
     ]

username_mapping = {user[1]: user for user in users}

username_input = input("Enter you username! ")
password_input = input("Enter your password! ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct!!")
else:
    print("Your details are incorrect!!")

print(username_mapping)