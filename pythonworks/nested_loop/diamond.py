#          * 
#         * * 
#        * * * 
#       * * * * 
#      * * * * * 
#     * * * * * * 
#    * * * * * * * 
#   * * * * * * * * 
#  * * * * * * * * * 
# * * * * * * * * * * 
#  * * * * * * * * * 
#   * * * * * * * * 
#    * * * * * * * 
#     * * * * * * 
#      * * * * * 
#       * * * * 
#        * * *
#         * *
#          *
 

limit = int(input("enter size of pattern : should be greater the 3 !"))
if limit % 2 == 0:
        limit +=1
else:
        limit = limit
first = limit // 2
second = limit // 2

for row in range(1,limit):
    if row <= second:
        for space in range(first,row,-1):
            print(" ",end="")
        for col in range(0,row):
            print("* ",end="")
        print()

    elif row == (limit+1)//2:
        continue
    else:
        for space in range(second,row-1):
            print(" ",end="")
        for col in range(limit,row,-1):
            print("* ",end="")
        print()
