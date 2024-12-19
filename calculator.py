print("This is simple calculator performs basic arithmetic operations: addition, subtraction, multiplication and division    \n") 

print(" if  you want addion enter 1 , subtraction enter 2 , multiplication enter 3 , division enter 4 \n")
num1=float(input("enter first number \n  "))


num2=float(input("enter second number \n  "))

user=input("chose the prosses you want  (+)  or (-)  or  (*)  or (/)  ")

if user == "1":
        print(f" you chose addicton  the result is {num1+num2}")
elif user=="2":
        print(f" you chose substraction  the result is {num1-num2}")        
elif user=="3":
        print(f" you chose multiblaction  the result is {num1*num2}")
elif user=="4":
        print(f" you chose division  the result is {num1/num2}")