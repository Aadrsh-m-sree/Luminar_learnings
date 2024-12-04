num1= 100
num2 = 200
print(num1 , num2)

# method 1 (temp variable)
temp= num1
num1 = num2 
num2= temp
print(num1, num2)

# method 2 (arithmetic operator)
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print(num1 , num2)

# # method 3 (tuple unpacking)
num1, num2 = num2 , num1
print(num1,num2)

