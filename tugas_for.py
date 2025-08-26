for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("Telu ro Limo")
    elif i % 3 == 0:
        print("Telu")
    elif i % 5 == 0:
        print("Limo")
    else:
        print(i)
