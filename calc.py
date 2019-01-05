print("Welcome to the Calculator Program\n")
print("Enter 1 for Addition: ")
print("Enter 2 for Subtraction: ")
print("Enter 3 for Multiplication: ")
print("Enter 4 for Division: ")
x = input("Your Choice ? ")
if x==1:
		s = 0
	 	while True:
			y = input("Enter Number: ")
			s += y
			ch = input("Add more? Press 1 : ")
			if ch != 1:
				break;
		print("Sum is: "+str(s)+"")
elif x==2:
		print("Enter the greatest number first:")
		y=input ("Enter the number:")
		s=y
		while True:
			ch= input("Enter more? Press 1 : ")
			if ch==1:
				y=input("Enter the number: ")
				s=s-y
			if ch!=1:
				break;
		print("Subtraction is: "+str(s))
elif x==3:
		s=1
		while True:
			y=input("Enter number: ")
			s=s*y
			ch= input("Enter more ? Press 1 : ")	
			if ch!=1:
				break;
		print("multiplication is: "+str(s))
elif x==4:
		print("Enter the number in descending order:")
		y=input ("Enter the number: ")
		s=y
		while True:
			ch= input("Enter more? Press 1 : ")
			if ch==1:
				y=input("Enter the number: ")
				s=s/y
			if ch!=1:
				break;
		print("Division is: "+str(s))
else:
		print("Wrong Input")