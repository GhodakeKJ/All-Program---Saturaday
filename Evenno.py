#Write Program For Nth Given Number Is Even By Using while Loop
n=int(input("Enter Any Number :"))
if(n<=0):
    print("Invalid Input Plz Enter +ve Number")

else:
    i=0
    while(i<=n):
        print("\t{}".format(i),end=" ")
        i=i+2