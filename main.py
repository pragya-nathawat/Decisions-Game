print("Welcome to the Decision game!")
name = input("Enter your name:")
age = input("Enter your age:")
print("Hello " + name +", you are "+ age +" years old.")
#there is a +/- when you move your cursor near if in next line
if (int(age) > 18):
	print("You are eligible to play! ")
	beg = input("Are you ready?").lower()
else:
	print("You need to be atleast 18 to play!")
print(beg)