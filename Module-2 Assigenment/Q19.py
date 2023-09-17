# Q 19.) Write a Python program to find the first appearance of the substring 
#       'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
#       whole 'not'...'poor' substring with 'good'. Return the resulting string.

paragh = """People became poor for different poor reasons not and often they are not responsible for what happening with them. 
When we help poor people, we became not better, more moral and . Helping poor helps us to remember poor that there is another 
side of life and that we can face poor with familiar grief in any time."""


string_not = paragh.count("not")
string_poor = paragh.count("poor")

print(string_not)
print(string_poor)

#if string_not>string_poor:
not_replace = paragh.replace("not", "poor")
good_replace = paragh.replace("poor", "good")
print("Replaced paragraph into 'NOT' to 'POOR':---", not_replace)
print("Replaced paragraph into 'POOR' to 'GOOD' :---", good_replace)
