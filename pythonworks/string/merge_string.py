text1= 'PQRST'
text2 = 'ABC'
result = ''


smallest_text = text1 if text1 < text2 else text2
biggest_number = text1 if text1 > text2 else text2

for i in range(0,len(smallest_text)):
    result += text1[i] + text2[i]

balance_text = biggest_number[len(smallest_text):]
result += balance_text

print(result)

