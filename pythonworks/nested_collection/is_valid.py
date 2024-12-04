user_input = input('enter input')

symbol_dict = { '{' : '}' , '[' : ']' , '(' : ')' }
symbol_stack = []
top = -1
is_valid = True
        
for x in user_input:
    if x in symbol_dict:
        top = top+1
        symbol_stack.append(x)
    elif top == -1:
        is_valid == False
    elif x == symbol_dict.get(symbol_stack[top]):
        top = top-1
        symbol_stack.pop()
    else:
        is_valid == False
    
if len(symbol_stack) == 0 and is_valid:
    print("Valid")
else:
    print("Invalid")

        
    
        

