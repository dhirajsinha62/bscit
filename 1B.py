#Enter the number from the user and depending on whether the
#number is even or odd, print out an appropriate message to the user.

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")
