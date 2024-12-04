# 12. Check for Prime Number:
#     - Write a Python program to check if a given number is a prime number using a `while` loop.


prime = int(input("enter a number to check if prime ?"))
is_prime = True
i = 2

while(i*i <= prime and is_prime):
    is_prime = (prime % i !=0)
    i+=1
print(f"number is prime" if is_prime and prime>1 else "not prime")


# prime = int(input("enter a number to check if prime ?"))
# is_prime = True
# i = 2

# while(i*i < prime):  #36 [2*2<36 (True),],[3*3 < 37, (True)]
#     if prime % i == 0: # [36 % 2 != 0 (False) ,] ,[37 %2 != 0]
#         is_prime = True
#         print(prime)
#     else: # [prime % 2 == 0]
#         prime += 1 #[37]
        
        