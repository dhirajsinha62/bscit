#A pangram is a sentence that contains all the letters of the English alphabet
#at least once, for example: The quick brown fox jumps over the lazy dog.
#Your task here is to write a function to check a sentence to
#see if it is a pangram or not.
 
#Check the length
#If the length is less than 26, then the sentence is not Pangram
#If the length is more than 26, then we need to remove all the special characters,
#spaces from the sentence
#Convert the sentence into lower case
#Iterate through the sentence and check whether all the elements in the
#alphabetList is present or not.
 
import re
 
def isPangram(inputSentence):
 
    alphabetList = 'abcdefghijklmnopqrstuvwzyx'
    alphabetCount = 0
 
    if len(inputSentence) < 26:
        return False
    else:
        inputSentence = re.sub('[^a-zA-Z]','',inputSentence)
 
        inputSentence = inputSentence.lower()
         
        for i in range(len(alphabetList)):
            if alphabetList[i] in inputSentence:
                alphabetCount = alphabetCount+1
 
        if alphabetCount == 26:
            return True
        else:
            return False
                     
print ("Enter a sentence : ")
 
inputSentence = input()

 
if (isPangram(inputSentence)):
    print ("Input Sentence is a Pangram")
else:
    print ("Input Sentence is not a Pangram")
