text = input()
text = text.lower()
words = text.split(" ")
for word in words:
    if word[0] == "www.":
        print(word[0])
