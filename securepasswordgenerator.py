#Python password generator by Psychovik

import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
symbol="{}[]()*&%$#@!,/-_;:"

case=lower+upper
alphanum=lower+number
strong=lower+number+upper
all=symbol+upper+number+lower

print("Welcome to the Secure Password Generator")
print("                                --By Psychovik")

i=0
while i < 5:
	print(" \n Menu: Choose your option \n-------------------------------------------------------------------------------\n 1.Case Sensitive Password \n 2. Alphanumeric Password(Case Insensitive) \n 3.Strong Password (Alphanumeric with Case Sensitive) \n 4.Ultra Secure Password \n 5. Exit \n ----------------------------------------------------------------------------")
	length=8
	password=""
	i=int(input("Enter your choice ----> "))
	if i==1:
		le=input("Do you want to change the length of the password (Default length is 8) Y/N: ")
		le=le.lower()
		if le=='y':
			length=int(input("Enter the length of the password"))
		else:
			length=8
		password="".join(random.sample(case,length))
		print("\n *************************** \n Your password is ---> "+password + "\n ***************************")
	elif i==2:
		le=input("Do you want to change the length of the password (Default length is 8) Y/N: ")
		le=le.lower()
		if le=='y':
			length=int(input("Enter the length of the password"))
		else:
			length=8
		password="".join(random.sample(alphanum,length))
		print("\n *************************** \n Your password is ---> "+password + "\n ***************************")
	elif i==3:
		le=input("Do you want to change the length of the password (Default length is 8) Y/N: ")
		le=le.lower()
		if le=='y':
			length=int(input("Enter the length of the password"))
		else:
			length=8
		password="".join(random.sample(strong,length))
		print("\n *************************** \n Your password is ---> "+password + "\n ***************************")
	elif i==4:
		le=input("Do you want to change the length of the password (Default length is 8) Y/N: ")
		le=le.lower()
		if le=='y':
			length=int(input("Enter the length of the password"))
		else:
			length=8
		password="".join(random.sample(all,length))
		print("\n *************************** \n Your password is ---> "+password + "\n ***************************")
				
