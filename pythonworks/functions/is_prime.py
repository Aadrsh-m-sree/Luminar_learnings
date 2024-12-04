def is_prime(num):
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
    return is_prime

result = is_prime(8)
print(result)