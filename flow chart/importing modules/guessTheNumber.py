import random

secret_number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20")

for guessTaken in range(1, 7):
	print("Take a guess")
	guess = int(input())

	if guess < secret_number:
		print("Your guess is too low")
	elif guess > secret_number:
		print("Your guess is too high")
	else:
		break
if guess == secret_number:
	print("Good job you guess my number in" + str(guessTaken))
else:
	print("Nope. The number I was thing of was" + str(secret_number))