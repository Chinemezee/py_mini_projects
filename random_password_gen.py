import random
import string
while True:
    password = ""
    pass_length = int(input("Length of password: "))
    pass_characters = [string.ascii_lowercase,
                        string.ascii_uppercase,
                        string.digits,
                        string.punctuation]
    weight = [0.4, 0.3, 0.2, 0.1]
    for i in range(pass_length):
         group = random.choices(pass_characters, weights=weight)[0]
         password += random.choice(group)
    print(password)
    continue

