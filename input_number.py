def increment(count):
	while count != 101:
		count = count + 1
		if count % 3 == 0 and count % 5 == 0:
				print("FizzBuzz!")
		elif count % 3 == 0:
				print("Fizz!")
		elif count % 5 == 0:
				print("Buzz!")

		else:
			print(count)

increment(1)

print("Enter a string")
string = input()


reverse = string[::-1] #by leaving the begining and the end off and specifying a step 0f _1, it reverses a string

print(reverse)

def palindrome(string, reverse):
	if string == reverse:
		print("Yep! we have a palindrome!")
	else:
		print("Sorry try again!")

palindrome(string,reverse)