rows = int(input("Enter the row number           : "))
symbol = input("Enter the symbol to use number : ")

j = 0
for x in range(rows):
    for y in range(j+1):
        print(symbol, end="")
    print("")
    j+=1