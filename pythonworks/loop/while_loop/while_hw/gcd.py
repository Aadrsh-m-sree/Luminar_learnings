# 8. Find the Greatest Common Divisor (GCD):
#    - Write a Python program to find the GCD of two numbers using a `while` loop.

num1= int(input("enter num1 :"))
num2= int(input("enter num2 :"))

### Key Principles of the Euclidean Algorithm

# **Divisor Property**:
#  If d is a divisor of both numbers a and b, then d is also a divisor of the remainder r when a is divided by b.
    
#  **Example**: If d divides both a = 48 and b = 18, then d must also divide r = 48 % 18 = 12.
    
#  **GCD Property**:
    
#  The Greatest Common Divisor (GCD) of two numbers a and b (where a > b) is the same\
#  as the GCD of b and the remainder r when a is divided by b.
    
#  **Formula**: GCD(a, b) = GCD(b, r)

# num1 = 48 , num2 = 18
while(num2 != 0): #18!=0 12!=0 6!=0 0!=0X
    remainder = num1 % num2 #12 = 48%18=12 18%12=6 12%6=0
    num1 = num2 #num1=18 num1=12 num1=6
    num2 = remainder #num2=12 num2=6 num2=0
print("GCD =",num1) #GCD=6

