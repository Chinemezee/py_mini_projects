while True:
    try:
        age = int(input(": "))
        print(age)
        break
    except ValueError:
        print("input number")
        continue
    except ZeroDivisionError:
        print("input number 1- 10")
        continue



