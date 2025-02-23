rows=int(input("Enter the no. of rows: "))
columns=int(input("Enter the no. of columns: "))
symbol=input("Enter the symbol to use: ")
for y in range(rows):
    for x in range(columns):
        print(symbol,end="") #to print consecutively
    print()    #add a break to the next line