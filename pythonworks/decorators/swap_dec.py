def swap_dec(func): # 3 decorator function 
    def  wrapper(n1,n2): # 5 executes wrapper function()
        if n1 < n2 :
            (n1,n2) = (n2,n1)
        return func(n1,n2) # 6 returns  the result of func(n1,n2) / division(10,2)
    return wrapper # 4 finds wrapper

def round_dec(func):
    def wrapper(n1,n2):
        n1 = round(n1)
        n2 = round(n2)
        return func(n1,n2)
    return wrapper

@round_dec
@swap_dec
def add_numbers(num1,num2):
    return num1 + num2

@swap_dec
def subtraction(num1,num2):
    return num1 - num2

@round_dec
@swap_dec
def division(num1,num2): # 2 calling decorator
    return num1 / num2

print(division(2.5,3.6)) # 1 function call
print(add_numbers(2.5,3.6))