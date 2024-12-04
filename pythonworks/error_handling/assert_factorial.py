def factorial(num):
    if num==0:
        return 1
    else:
        f=1
        for i in range(1,num+1):
            f=f*i
        return f

def test_factorial():
    assert factorial(5)==120,"Factorial check failed"
    assert factorial(0)==1,"Zero check failed"
try:

    test_factorial()
    print("Test passed")
except Exception as e:
    print(e)