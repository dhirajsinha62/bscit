# Program to check if a string
# is palindrome or not with function


print('!* To Find Palindrome and/or Armstrong Number')
def Palindrome_Number():
    n = int(input('Enter a Number to check for palindromee'))
    m=n
    a = 0
    while(m!=0):
        a = m % 10 + a * 10
        m = m // 10

    if( n == a):
        print(n,'is a palindrome number')
    else:
        print(n,'is not a palindrome number')



def Armstrong_Number():
      number = int(input('Enter a Number to check for Armstrong'))
      temp = number
      Sum = 0
 
      #loop till the quotient is 0
      while(temp != 0):
          rem  = temp % 10 #find reminder
          Sum  = Sum + (rem * rem * rem) #cube reminder and add it to the Sum
          temp = temp // 10 #find quotient, if 0 then loop again
       
      #if the entered number and the Sum value matches, it is an Armstrong number
      if(number == Sum):
          print (number,"is Armstrong Number")
      else:
          print (number,"is Not an Armstrong Number")

