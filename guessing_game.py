import random
def guessgame():
    random_number = random.randint(1, 100)
    print("Welcome to the guess game")
    while True:
        try:
            user_guess = int(input("> "))
            attempts = 0
            attempts += 1
            if attempts == 5:
                print("max attempts")
                break
            if user_guess < random_number:
                print("too small\ntry again")
            elif user_guess > random_number:
                print("too big\ntry again")
            else:
                print("correct number")
                break
        except ValueError:
            print("invalid")

                

guessgame()
        
            
