print("***CALCULATOR***")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplacatio")
print("4.Division")

a=str(input("Select any option: "))
if a=="1":
    print("  Addition  ")
    num1=int(input("Enter Number: "))
    num2=int(input("Enter Number: "))
    print("Addition of",num1,"+",num2,"is",num1+num2)
elif a=="2":
    print("  Subtraction ")
    num3=int(input("Enter Number: "))
    num4=int(input("Enter Number: "))
    print("Subtraction of",num3,"-",num4,"is",num3-num4)
elif a=="3":
    print("  Multiplacation  ")
    num5=int(input("Enter Number: "))
    num6=int(input("Enter Number: "))
    print("Multiplacation of",num5,"*",num6,"is",num5*num6)
elif a=="4":
    print("  Division  ")
    num7=int(input("Enter Number: "))
    num8=int(input("Enter Number: "))
    print("Division of",num7,"/",num8,"is",num7/num8)
else:
    print("please enter valid operator")
    

    
