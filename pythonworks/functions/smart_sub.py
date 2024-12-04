def smart_sub(num1,num2,reverse=False):
    return num2-num1 if reverse == True else num1-num2
print(smart_sub(10,20,False))