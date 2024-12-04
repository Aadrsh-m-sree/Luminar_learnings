# Write an if statement to check if a given year is a leap year.

year = int(input("enter an year :"))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print("leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print ("not a leap year")

if (year % 100 != 0 and year % 4 == 0) or (year % 100 == 0 and year % 400 == 0):
    print("leap year")
else:
    print("not leap year")