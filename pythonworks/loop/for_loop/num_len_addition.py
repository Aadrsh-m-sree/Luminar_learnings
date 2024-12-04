num = input("enter number :") #num = "3"  
num_str = num #num_str = "3"
size = int(num) #size = 3

total = 0 # 0

for i in range(1, size +1): #1 , 2 , 3 
    total += int(num) # 3 , 3+33=36 36 +333=369
    num += num_str # num = 33 , num = 333 
print(total) 
    
    
