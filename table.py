n=int(input("Enter Number For Table :"))
if(n<=0):
    print("{} Is Invalid Number Plz Enter +ve Number".format(n))
else:
    print("="*60)
    print("Mul Table For :{}".format(n))
    print("="*60)
    for i in range(1,11):
        print("{}    X   {}   =   {}".format(n,i,n*i))
    print("="*60)