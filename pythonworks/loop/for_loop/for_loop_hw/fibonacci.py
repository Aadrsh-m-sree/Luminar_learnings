# 11. **Print the first 5 numbers in the Fibonacci series:**
#     - Input: None
#     - Output: 0 1 1 2 3

first = 0
second = 1
print(first, second ,end=" ")
for i in range(1,4):
    fibonacci = first+second
    first = second
    second = fibonacci
    print( fibonacci , end=" ")