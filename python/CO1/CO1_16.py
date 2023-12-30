# Take two strings input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Swap characters at position 1
s1 = string2[0] + string1[1:]
s2 = string1[0] + string2[1:] 

# Create a single string separated by space
result_string = s1 + ' ' + s2

# Display the result
print("Resulting string:", result_string)