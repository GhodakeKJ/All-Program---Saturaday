while(True):
    sno=int(input("Enter Student Number :"))
    if(sno>=1) and (sno<=300):
        break
    print("Plz Enter Student Number Within 1 To 300 Only")
sname=input("Enter Student Full Name :")
cname=input("Enter Student Collage Name :")
while(True):
    python=float(input("Enter marks In Python Subject :"))
    if(python>=0) and (python<=100):
        break
    print("Plz Enter Python Marks Within 0 to 100 Only")
while(True):
    cpp=float(input("Enter marks In C++ Subject :"))
    if(cpp>=0) and (cpp<=100):
        break
    print("Plz Enter C++ Marks Within 0 to 100 Only")
while(True):
    java=float(input("Enter marks In java Subject :"))
    if(java>=0) and (java<=100):
        break
    print("Plz Enter Java Marks Within 0 to 100 Only")
totalmarks=python+cpp+java
average=(totalmarks/300)*100

if(python<40) or (cpp<40) or (java<40):
    grade="FAIL"
else:
    if(totalmarks>=250) and (totalmarks<=300):
        grade="Destination"
    elif(totalmarks>=200) and (totalmarks<=249):
        grade="First"
    elif(totalmarks>=150) and (totalmarks<=199):
        grade="Second"
    else
        if(totalmarks>=120) and (totalmarks<=149):
            grade="Third"
print("*"*60)
print("\t** S T U D E N T  R E P O R T  C A R D  2 0 2 2 **")
print("="*60)
print("\tStudent Exam Number  :",sno)
print("\tStudent Full Name    :",sname)
print("\tStudent Collage Name :",cname)
print("-"*60)
print("\tStudent Marks In Python  :",python)
print("\tStudent marks In C++     :",cpp)
print("\tStudent Marks In Java    :",java)
print("-"*60)
print("\tStudent Total marks      :",totalmarks)
print("\tStudent Average          :",average)
print("-"*60)
print("\tStudent Grade            :",grade)
print("*"*60)
