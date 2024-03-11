n1=int(input("Enter a number"))
n2=int(input("Enter a number"))
print("Please select the operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus division")
print("6.Floor division")
print("7.Exponenet")
ch=int(input("Enter the option number"))
if(ch==1):
    n3=n1+n2
    print(n1,"+",n2,"=",n3)
elif(ch==2):
    n3=n1-n2
    print(n1,"-",n2,"=",n3)
elif(ch==3):
    n3=n1*n2
    print(n1,"*",n2,"=",n3)
elif(ch==4):
    n3=n1/n2
    print(n1,"/",n2,"=",n3)
elif(ch==5):
    n3=n1%n2
    print(n1,"%",n2,"=",n3)
elif(ch==6):
    n3=n1//n2
    print(n1,"//",n2,"=",n3)
elif(ch==7):
    n3=n1**n2
    print(n1,"**",n2,"=",n3)
else:
    print("Your entered option is Invalid .please enter a Valid option number") 
    

