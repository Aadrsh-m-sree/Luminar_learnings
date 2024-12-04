expenses = [40000,10000,20000,30000,40000,20000,40000,40000,8000]

# iteration
# for exp in expenses:
#     print(exp)


# find total without sum()

# total = 0
# for exp in expenses:
#     total += exp
# print(total)


# find maximum without max()
# maximum = 0
# i = expenses[0]
# for exp in expenses:
#     if i > exp:
#         maximum = i
#     else:
#         i = exp 
# print(maximum)


# max_exp = 0
# for exp in expenses:
#     if exp > max_exp:
#         max_exp = exp
# print(max_exp)


# find minimum without min()
# minimum = 0
# i = expenses[0]
# for exp in expenses:
#     if i < exp:
#         minimum = i
#     else:
#         i = exp 
# print(minimum)


# find average without avg()

# count_of_list = len(expenses)
# total = 0
# for exp in expenses:
#     total += exp

# average = total / count_of_list
# print(average)

# most frequent

# count = 0
# for i in expenses:
#     for j in expenses:
#         if i == j:
#             count+=1
# print(count)

most_frequent =None
max_count = 0
for i in expenses:
    count = 0
    for j in expenses:
        if i == j:
            count+=1

    if count > max_count:
        max_count = count
        most_frequent = i

print(most_frequent,max_count)


