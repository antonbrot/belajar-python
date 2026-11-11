"""rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range (rows):
    for y in range(columns):
        print(symbol, end = "")
    print()"""

"""colors = ['red', 'blue', 'green']
sizes = ['S', 'M', 'L']
for c in colors:
    for s in sizes:
        print(f"{c} - Sizes {s}")"""

"""years = [2010, 2011, 2012, 2013]
months = ['Nov', 'Dec']
days = range(1,31)
for y in years:
    for m in months:
        for d in days:
            print(f"report_{y}_{m}_{d}.txt")"""

"""tables = ['customers', 'products', 'orders', 'prices']
columns = ['id', 'create-date']
for t in tables:
    for c in columns:
        print(f"SELECT * FROM {t} WHERE {c} IS NULL;")"""

for i in range(5):              
    for j in range(5):          
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()