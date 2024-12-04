def swap_decorator(fn):
    def wrapper(n1,n2):
        if n1<n2:
            n1,n2=n2,n1
        return fn(n1,n2)
    return wrapper




def smart_sub(n1,n2):
    return n1-n2
@swap_decorator
def smart_div(n1,n2):
    return n1/n2 
smart_sub=swap_decorator(smart_sub)
print(smart_sub(2,10))
print(smart_div(10,2))
