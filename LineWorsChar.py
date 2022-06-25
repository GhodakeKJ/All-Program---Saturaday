fname=input("Enter Any File Name  :")
try:
    nl=0
    nw=0
    nc=0
    with open(fname)as fp:
        lines=fp.readlines()
        for line in lines:
            print(line,end="")
            nl=nl+1
            nw=nw+len(line.split())
            nc=nc+len(line)
            print("="*50)
            print("Number Of Lines =",nl)
            print("Number Of Words =",nw)
            print("Number Of Chars =",nc)
            print("="*50)

except FileNotFoundError:
    print("File Does Not Exists")
