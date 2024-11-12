#!/usr/bin/python3

import os
os.system('clear')
print("\n\nImported os\n\n")

def personal(name,age,col,py,world):
	import string
	print("\nYou have provided the following details:\n\tName: ",name,"\n\tAge: ",age,"\n\tFavourite color: ",col,"\n\tLike Python or not? : ",py,"\n\tFlat world: ",world)
# comments
	for character in name:
		if character not in string.ascii_letters:
			return print("\nYou are more than just a number, honestly, please start again.")
	if age >99 or age < 3 :
		print("\n",name,", I dont think your age is credible.")
	if col.upper() != "BLUE":
		print("\nI really like blue, but ",col," is also good.")
	else:
		print("\nI like it too!")
	if py.upper()[0] != "Y":
		print("\nI am sorry that you dont like Py")
	else: 
		print("\nGlad you like Py")
	if world != "False":
		return print("\nEither you really do think the world is flat,\nor you havent typed False in the correct Python format\n\n")
	else:
		print("Correct common sense!")
	return "OK", print("\nAll OK, thanks a lot.")


# get the input and make the dir
details={}
details["Name"] = input("what is your name?")
details["Age"] = int(input("How old are you?"))
details["Color"] = input("What is your favourite color?")
details["Python"] = input("Do you like py?")
details["World"] = input("The world is flat: True or False?")

# use the function
personal(*list(details.values()))

print("\n\nThis was the dictionary you set up...\n\n",details,"\n\nBye!\n\n")

