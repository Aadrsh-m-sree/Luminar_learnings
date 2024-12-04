def add_numbers(*args): #NOTE -  *args used to take any number of arguments as a tuple
    print(args)

add_numbers(10,20)
add_numbers(10,20,30)


def product(*args):
    result = 1
    for num in args:
        result = result*num
    return result
print(product(10,20,5,6))

# second largest

def second_largest(*args):
    second = sorted(args, reverse=True)
    return second[1]
print(second_largest(10,20,30,40))


