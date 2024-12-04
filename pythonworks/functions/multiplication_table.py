def multiplication_table(num,limit=10):
    for i in range(1,limit+1):
        print(f" {i} * {num} = ",num * i)
    
multiplication_table(3)