with open("Karan.data","w") as fp:
    print("Enter The Data Dynamically And To Stop Press '@' :")
    while(True):
        kbdata=input()
        if(kbdata=="@"):
            break
        else:
            fp.write(kbdata+"\n")