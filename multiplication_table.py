num = 2
multiply = 0
while True:
    try:
        total = num * multiply
        multiply += 1
        print(total)
        if multiply == 13:
            break 
    except ValueError:
        print("ii")