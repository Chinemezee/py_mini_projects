import random
def guess():
    randomnumber = random.randint(1, 100)
    print(randomnumber)
    
    while True:
        try:
            user_guess = int(input("guess> "))
            if user_guess < randomnumber:
                print("wrong number, too low, try again")
            elif user_guess > randomnumber:
                print("wrong number, too high, try again")
            else:
                print("right")
                break
        except ValueError:
            print("only wholes")
guess()