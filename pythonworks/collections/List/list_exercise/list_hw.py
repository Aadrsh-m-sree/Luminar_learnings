# 1. Write a Python program to find the sum of all elements in a list.

my_list = [1, 2, 3, 4, 5]
total_sum = sum(my_list)
print(total_sum)

# 2. Write a Python program to remove duplicates from a list.

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print(unique_list)

# 3. Write a Python program to find the second largest element in a list.

my_list = [10, 20, 4, 45, 99]
my_list.sort()
second_largest = my_list[-2]
print(second_largest)

# 4. Write a Python program to count the occurrences of each element in a list.

my_list = [1, 2, 2, 3, 4, 4, 5]
frequency = [(element, my_list.count(element)) for element in set(my_list)]
for element, count in frequency:
    print(f'{element}: {count}')

# 5. Write a Python program to reverse a list.

my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)

# 6. Write a Python program to find the maximum and minimum elements in a list.

my_list = [1, 2, 3, 4, 5]
max_value = max(my_list)
min_value = min(my_list)
print("Max:", max_value, "Min:", min_value)

# 7. Write a Python program to merge two lists and sort the resulting list.

list1 = [1, 5, 3]
list2 = [2, 6, 4]
merged_list = sorted(list1 + list2)
print(merged_list)

# 8. Write a Python program to find common elements in two lists.

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = list(set(list1) & set(list2))
print(common_elements)


# 9. Write a Python program to check if a list is empty.

my_list = []
is_empty = len(my_list) == 0
print("List is empty:", is_empty)

# 10. Write a Python program to remove an element from a list by index.

my_list = [1, 2, 3, 4, 5]
index_to_remove = 2
del my_list[index_to_remove]
print(my_list)

# 11. Write a Python program to find the length of a list without using the len() function.

my_list = [1, 2, 3, 4, 5]
length = 0
for _ in my_list:
    length += 1
print(length)


# 12. Write a Python program to multiply all elements in a list.

my_list = [1, 2, 3, 4]
result = 1
for num in my_list:
    result *= num
print(result)


# 13. Write a Python program to find all the even numbers in a list.

my_list = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in my_list if num % 2 == 0]
print(even_numbers)

# 14. Write a Python program to replace an element in a list with another element.

my_list = [1, 2, 3, 4, 5]
index_to_replace = 2
new_value = 99
my_list[index_to_replace] = new_value
print(my_list)

# 15. Write a Python program to split a list into two halves.

my_list = [1, 2, 3, 4, 5, 6]
mid = len(my_list) // 2
first_half = my_list[:mid]
second_half = my_list[mid:]
print("First half:", first_half)
print("Second half:", second_half)
