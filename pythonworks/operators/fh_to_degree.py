# create a python programme to convert from  Farenheit to degree celsius

def fh_to_dc():
# C = (F-32) * 5/9
    F = int(input('Enter Farenheit :'))
    C = (F - 32) * 5/9
    print(f"{F} Degree Farenheit is {C} Degree Celcius")

fh_to_dc()