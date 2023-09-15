# Q 8.) Write a Python program to test whether a passed letter is a vowel or not.


letter = input("Input a letter of the alphabet: ")

if letter in ('a', 'e', 'i', 'o', 'u'):
	print(letter, " is a vowel." )
else:
	print(letter, " is a consonant." ) 