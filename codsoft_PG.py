import string
import random
length = int(input("Enter password length: "))
print("Choose character set for password")
print("1. Letters")
print("2. Digits")
print("3. Special characters")
print("4. Exit")
characterList = ""
while(True):
	choice = int(input("Select a number from 1,2,3,4: "))
	if(choice == 1):
		characterList += string.ascii_letters
	elif(choice == 2):
		characterList += string.digits
	elif(choice == 3):
		characterList += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Please select a valid option!")
password = []
for i in range(length):
	randomchar = random.choice(characterList)
	password.append(randomchar)
print("The generated password is " + "".join(password))
