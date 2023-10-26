# Q 10.) Write a Python program to count the frequency of words in a file.


number_of_words = 0

with open(r'global_warming.txt','r') as file:
	data = file.read()

	lines = data.split()

	number_of_words += len(lines)

print("The Number of Words in file is: ",number_of_words)


with open('global_warming.txt', 'r') as f:
    line= f.read()

word = input("Enter the word to check it's freq: ")
result = line.count(word)
print("Number of substring occurrences:", result)
