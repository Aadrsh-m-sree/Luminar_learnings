def last_max(num1,num2):
    last_num1 = num1 % 10
    last_num2 = num2 % 10

    
    if last_num1 > last_num2:
        return print(num1)
    else:
        return print(num2)

last_max(123,871)