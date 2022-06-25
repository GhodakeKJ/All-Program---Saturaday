import pickle,sys
def SaveStudentData():
    with open("Student.data","ab") as fp:
        while(True):
            print("="*50)
            sno=int(input("Enter Student Number  :"))
            sname=input("Enter Student Name      :")
            marks=float(input("Enter Student Marks:"))
            l=list()
            l.append(sno)
            l.append(sname)
            l.append(marks)
            pickle.dump(l,fp)
            print("Student Record Saved Successfully")
            ch=input("Do You have Entered Data Of Another Student (yes/no) :")
            if(ch.lower()=="no"):
                print("Thanks For Using This Program")
                sys.exit()
SaveStudentData()