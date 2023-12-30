def count(s):
    c = {}
    for i in s:
        if i in c:
            c[i] += 1
        else:
            c[i] = 1
    return c

word = input("Enter a word: ")
print("Character\tNo. of occurrences")
char_count = count(word)
for char in char_count:
    print(char, "\t\t\t", char_count[char])
