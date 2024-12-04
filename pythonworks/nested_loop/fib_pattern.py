#       Fibonacci pattern
#       0 
#       0 1
#       0 1 1
#       0 1 1 2
#       0 1 1 2 3
#       0 1 1 2 3 5
#       0 1 1 2 3 5 8


limit = int(input("enter limit :"))
prev = 0
current = 1
for row in range(1,limit):
    for col in range(0,row):
        if col == 0:
            print(str(prev)+" " ,end="")
        if col == 1:
            print(str(current)+" ",end="")
        elif col > 1:
            next_value = prev + current
            prev = current
            current = next_value
            print(str(next_value)+" ",end="")
    print()
    prev = 0
    current = 1
    
    
    


