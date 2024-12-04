num = int(input("num :"))
og_num  = num
num_len = len(str(num))

total = 0
while(num > 0):
    rem = num % 10
    result = rem ** num_len
    total += result
    num = num // 10
print(f"{total} is an amstrong"  if total == og_num  else "not amstrong")