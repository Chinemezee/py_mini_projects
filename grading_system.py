grades = {}
while True:
    name = input("Enter the student name: ")
    if name.lower() == "stop":
        break
    
    try:
        score = int(input("Enter the student score: "))
        if score < 0 or score > 100:
            print("Enter score between 0 - 100")
            continue
    except ValueError:
        print("input a number")
        continue

    grades[name] = score

for name, score in grades.items():
    if 90 <= score <= 100:
        grade = "A"
    elif 80 <= score <= 89:
        grade = "B"
    elif 70 <= score <= 79:
        grade = "C"
    elif 60 <= score <= 69:
        grade = "D"
    elif 50 <= score <= 59:
        grade = "E"
    else:
        grade = "F"
    
    print(f"{name} scored {score}. The grade is {grade}")
print(grades)