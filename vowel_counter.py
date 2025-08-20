word = input("> ").lower()
vowels = "aeiou"
count = 0
for letters in word:
    if letters in vowels:
        count += 1
print(f"number: {count}") 