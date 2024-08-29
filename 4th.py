#  Write a function that takes a character (i.e. a string of length 1) and returns Trueif it is a vowel, Falseotherwise.
def vowel_or_not():
    vowels = ["A","E","I","O","U"]
    if char in vowels :
        return "True"
    else:
        return "False"
char = input("Enter a character :")  # we can  also use char as a argument
char = char.upper()    
print(vowel_or_not())
