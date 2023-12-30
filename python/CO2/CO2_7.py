
def suffix(word):
    if word[-3:] == 'ing':
        word += 'ly'
    else:
        word += 'ing'
    print("Word after adding suffix: ", word)
word = input("Enter a word: ")
suffix(word)

