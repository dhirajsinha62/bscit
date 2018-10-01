#Take a list, say for example this one:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and
#write a program that prints out all the elements of the list that are less than 5.



myList=[1, 1, 12, 3, 5, 8, 13, 21, 3, 55, 89]
myNewList=[]
#number=int(input("Enter a number"))
for i in myList:
        if(i<5):
            myNewList.append(i)
         
print("List containing numbers less than 5 is/are :", myNewList)
