#Write a function that reverses the user defined value.
def rev():
    num = int(input("Enter a number: "))
    org=num
    rev=0
    while num!=0:
        rem=num%10
        num=num//10
        rev=rev*10+rem
    
    print("Reverse of number ",org,"is = ",rev)
