# def poll(age):
#     assert age>=18,"Invalid age"
#     print("Voted")
# try:
#     poll(16)
# except Exception as e:
#     print(e)

def review(rating):
    assert rating>=0,"Too low"
    # assert rating<=10,"Too high"
    assert rating in range(0,11),"Too high"
    print("Done")

try:
    review(11)
except Exception as e:
    print(e)