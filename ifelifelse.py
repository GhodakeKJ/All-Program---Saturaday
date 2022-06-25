a=int(input("Enter First  Value For a :"))
b=int(input("Enter Second Value For b :"))
c=int(input("Enter Third Value For  c :"))
if(a==b==c):
    print("All Values Are Same Or Equals")
elif(a>b and a>c):
    print("A Value Is Big")
elif(b>a and b>c):
    print("B Value Is Big")
else:
    print("C Value Is Big")
