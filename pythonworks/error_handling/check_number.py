def numcheck(num):
    if num>0:
        return "+ve"
    elif num<0:
        return "-ve"
    elif num==0:
        return "zero"

def test_fn():
    assert numcheck(10)=="+ve","+ve check failed"
    assert numcheck(-2)=="-ve","-ve check failed"
    assert numcheck(0)=="zero","zero check failed"
try:
    test_fn()
    print("test passed")
except Exception as e:
    print(e)