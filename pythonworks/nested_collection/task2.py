# # avg by index

# student =  {
#     "Hari" : [45,40,35],
#     "Vipin" : [34,40,45],
#     "Vinay" : [45,40,35],
#     "Bijoy" : [33,38,35],
#     "Anvin" : [32,30,40]
# }

# print(student)
# inn = int(input())

# for i,element in enumerate(student):
#     if i+1 == inn:
#         print(element)
#         marks = student.get(element)
#         avg = sum(marks) / len(marks)
#         print(avg)
        

# all average 

student =  {
    "Hari" : [45,40,35],
    "Vipin" : [34,40,45],
    "Vinay" : [45,40,35],
    "Bijoy" : [33,38,35],
    "Anvin" : [32,30,40]
}

print(student)

for i,element in enumerate(student):
        print(element)
        marks = student.get(element)
        avg = sum(marks) / len(marks)
        print(f"{avg:.2f}")

# student_avg = {k:sum(v)/len(v) for k,v in student.items()}
# print(student_avg)
        