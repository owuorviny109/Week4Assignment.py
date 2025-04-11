print("Basic calculator")
operation=input("choose type of operation to do(+,-,*,/,//):")
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))  
if operation=="+":
     result=num1+num2
     print(f"{num1} {operation} {num2} = {result}")
elif operation=="-":
     result=num1-num2
     print(f"{num1} {operation} {num2} = {result}")
elif operation=="*":
     result=num1*num2
     print(f"{num1} {operation} {num2} = {result}")
elif operation=="/":
     result=num1/num2
     print(f"{num1} {operation} {num2} = {result}")
elif operation=="//":
     result=num1//num2
     print(f"{num1} {operation} {num2} = {result}")
else:
     print("Invalid operation")