txt = input()
fixed_txt = txt.strip("*_~'´")
outra_txt = txt.title()
ex_txt = txt.replace("!", "").replace("?", "").lower()


print(outra_txt)
print(fixed_txt)
print(ex_txt)

txt = input().lower()
txt = [a.strip(",.?!") for a in text]
print("".join(txt))
