signal = input("enter a color :").lower()

if signal == 'red':
    print("STOP")
elif signal == 'green':
    print("GO")
elif signal == 'yellow':
    print("WAIT")
else:
    print(f"{signal} is an invalid signal")