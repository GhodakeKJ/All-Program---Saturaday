for i in range(1,5):
    print("Value Of i ---> Outer For Loop:{}".format(i))
    j=1
    while(j<=5):
        print("\t\tValue Of j ---> Inner while Loop:{}".format(j))
        j=j+1
    else:
        print("I AM Going Outside Of inner while Loop")
else:
    print("I AM Going Outside Of Outer for Loop")