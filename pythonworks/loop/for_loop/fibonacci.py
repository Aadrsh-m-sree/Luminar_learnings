prev = 0
current = 1
print(prev,current , end = " ")
for i in range(1,6):
    next = prev + current
    prev = current
    current = next
    print(next, end= " ")
