while True:
	name = input("What is your name: ")
	if name != 'kofi':
		continue
	print("Hello Kofi, What is your password: ")

	password = input()
	if password == 'swordfish':
		break
print("Access granted")
