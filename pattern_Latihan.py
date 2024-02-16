i = 0
count = 20
space = int(1/2 * count)
while True:
    if i == count:
        break
    elif i % 2 :
        print(f" "* space, "+"*i)
        space -= 1
    i += 1
i = 0
count = 20
space = 1
while True:
    if i == count:
        break
    elif i % 2 :
        print(f" "* (space + 1), "+"*((20-i)-2))
        space += 1
    i += 1

i = 0
count = 20
space = 1
while True:
    if i == count:
        break
    elif i % 2 :
        print(f"+"* (space - 1), " "*((19-i)), "+"* (space - 1))
        space += 1
    i += 1

print("+"*20)
print("+"*20)

i = 0
count = 20
space = int(1/2 * count)
while True:
    if i == count:
        break
    elif i % 2 :
        print(f"+"* (space - 1), " "*(i - 1), "+"* (space - 1))
        space -= 1
    i += 1