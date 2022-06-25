try:
    with open("hyd.data","r") as fp:
        filedata=fp.read()
        print(filedata)
        print("File Data Will Be Show Here")
except FileNotFoundError:
    print("File Does Not Found")