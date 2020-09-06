while True:
	name = input("what is your name: ")
	if name != 'kofi':
		continue
	print(f"Hello, Kofi. What is your password? (It is a fish")
	password = input()
	if password == 'swordfish':
		break
print("Access granted")
