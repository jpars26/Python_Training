
#Function dosen't have parms
def addfriend():
    friends.append({"João": 30})

friends= []
addfriend()

print(friends)

#Function have parms 
def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

say_hello(name="Bob", surname="Charge")

