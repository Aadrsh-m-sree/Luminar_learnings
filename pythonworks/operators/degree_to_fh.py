# create a python programme to convert from degree celsius to Farenheitd

def dc_to_fh():
# F = (9/5 * C) + 32
    C = int(input("Enter degree celsius :"))
    F = (9/5 * C) +32
    print(f"{C} Degree Celsius is {F} Degree Farenheit")
dc_to_fh()