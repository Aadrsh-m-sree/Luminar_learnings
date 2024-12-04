begin = int(input("enter starting :"))
end = int(input("enter limit :"))

reverse = False
if begin > end :
    reverse = True
i=begin
while(i>=end and reverse == False):
    if i%2 == 0:
        print(i)
    i+=1
    

    