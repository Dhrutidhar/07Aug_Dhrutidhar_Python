# Q 51.) Write a Python function that checks whether a passed string is palindrome or not.


# A palindrome is a word, phrase, or sequence that reads the same backward as forward, 
# e.g., madam or nurses run.

def ispalindrome(str):
    return str == str[::-1]
 
str_1 = input("enter a word: ")
answer = ispalindrome(str_1)
 
if answer:
    print("Yes")
else:
    print("No")