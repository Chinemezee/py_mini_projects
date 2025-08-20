def num(num_list = []):
    for pips in range(5):
        value = int(input("insert: "))
        num_list.append(value)
    even = []
    for num0 in num_list:
        if num0 % 2 == 0:
            even.append(num0)
    print(even)
    print(num_list)
num()
