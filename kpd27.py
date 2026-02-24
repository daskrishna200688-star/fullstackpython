num=int(input("enter a number"))
if num>=0 and num<=9:
	print("single digit")
elif num>=10 and num<=99:
	print("Double Digit")
elif num>=100 and num<=999:
	print("Third Digit")
else:
	print("+ve number")