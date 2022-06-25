import pickle
try:
    with open("Student.data","rb") as fp:
        print("="*50)
        print("STudent Number\tStudent Name\tStudent Marks")
        print("="*50)
        while(True):
            try:
                obj=pickle.load(fp)
                for val in obj:
                    print("{}".format(val,end="\t\t"))
                    print()
            except EOFError:
                print("="*50)
                break
except FileNotFoundError:
    print("File Does Not Found")
