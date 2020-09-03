lst = ["Q1", "Q2", "Q3","Q4"]

x, y = input().split()

x = float(x)
y = float(y)

if x > 0 and y > 0:
    print(lst[0])
elif x < 0 and y > 0:
    print(lst[1])
elif x < 0 and y < 0:
    print(lst[2])
elif x > 0 and y < 0:
    print(lst[3])
else:
    print("Origem")
        
