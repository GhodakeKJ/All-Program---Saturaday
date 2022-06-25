try:
    a=int(input("Enter First Value :"))
    b=int(input("Enter Second Value :"))
    c=int(input("Enter Third Value :"))
    if(a==b==c):
        print("All Values Are Same/Equal")
    elif(a>b and a>c):
        print("A Value Is Big")
    elif(b>a and b>c):
        print("B Value Is Big")
    else:
        print("C Value Is Big")
except ValueError:
    print("Don't Enter strs,Alpha-Numerics And Special Symbols")