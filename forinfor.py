for i in range(1,3): #This Is Outer for Loop
    print("=" * 50)
    print("Value Of i ---> From Outer for Loop :{}".format(i))
    print("-" * 50)
    for j in range(1,2): #This Is inner for Loop
        print("Value Of j ---> From Inner for Loop :{}".format(j))
    else:
        print("I Am Going Outside From Inner for Loop")
        print("="*50)
else:
    print("I Am Going Outside From Outer For Loop")
print("="*50)