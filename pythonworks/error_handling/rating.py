def review(rating):
    if rating<0:
        raise Exception("Too low\n")
    elif rating>10:
        raise Exception("Too high\n")
    else:
        print("done")
n=int(input("Enter the limit:"))
for i in range(n):
    r=int(input("Enter the rating:"))
    try:
        review(r)
    except Exception as e:
        print(e)
        review(r)

print("hello")
print("hai")