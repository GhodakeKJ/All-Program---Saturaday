i=1
while(i<=3):
    print("=" * 50)
    print("Value Of i ---> in Outer while Loop:{}".format(i))
    j=1
    while(j<=3):
        print("\t\tValue Of j ---> in inner while Loop:{}".format(j))
        j=j+1

    else:
        print("I AM Going Outside Of inner while Loop")
        i=i+1
else:
    print("I Am Going Outside Of outer while Loop")
print("="*50)