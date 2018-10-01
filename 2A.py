"""
Write a function that takes a character (i.e. a string of length 1) and returns
True if it is a vowel, False otherwise.
"""


def is_vowel(char):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if char not in vowels:
        return False
    return True



c= input("Enter a character of length 1 to check whether it is vowel or not:")
if len(c)==1:
    print ("Result is",is_vowel(c))
else:
    print("You have not entered character of length 1")
