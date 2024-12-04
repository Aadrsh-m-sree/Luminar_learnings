word = 'aberrant'
target = 'errant'

charachter_count = {ch:word.count(ch) for ch in word }
is_kangaroo = True

for ch in target:
    if ch in charachter_count and charachter_count.get(ch) >0 :
        charachter_count[ch] -= 1
    else:
        is_kangaroo = False
        break
    
print(is_kangaroo)