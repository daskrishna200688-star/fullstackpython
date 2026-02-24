#wap take two number from keyboard enter your choice 1.add 2.sub 3.mult invalid choice monu driven program
n1=int(input("enter a number"))
n2=int(input("enter a number"))
print("Enter your choice")
print("1.add")
print("2.sub")
print("3.mult")
choice=(int(input("enter choice(1/2/3):")))
if choice==1:
	result=n1+n2
	print("add=",result)
elif choice==2:
	result=n1-n2
	print("sub=",result)
elif choice==3:
	result=n1*n2
	print("mult=",result)
else:
	print("Invalid Choice- menu driven program")
