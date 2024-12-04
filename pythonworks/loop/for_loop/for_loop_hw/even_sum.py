# 13. **Print the sum of all even numbers from 1 to 10:**
#     - Input: None
#     - Output: 30

total = 0
for i in range(1,11):
    if i %2 == 0:
        total += i
print(total)