def vote(age):
    if age<18:
        raise Exception("Invalid age")
    else:
        print("Voted")
n=int(input("Enter the limit:"))
try:
        age=int(input("Enter the age:"))
        vote(age)
        n-=1
except Exception as e:
    print(e)
    try:
        for i in range(n):
            age=int(input("Enter the age:"))
            vote(age)
    except Exception as e:
        print(e)