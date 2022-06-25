eno=int(input("Enter Employee Number :"))
ename=input("Enter Employee Name :")
edpt=input("Enter Employee Department :")
basicsal=float(input("Enter Employee Basic Salary :"))
ta=0
da=0
hra=0
cca=0
gpf=0
lic=0
if(basicsal<0):
    print("{} Is Invalid Salary Plz Enter EMP +ve SAL :".format(basicsal))
else:
    if(basicsal>0):
        ta=basicsal*(15/100)
        da=basicsal*(13/100)
        hra=basicsal*(10/100)
        cca=basicsal*(3/100)
        gpf=basicsal*(2/100)
        lic=basicsal*(4/100)
    else:
        ta = basicsal * (18 / 100)
        da = basicsal * (12 / 100)
        hra = basicsal * (19 / 100)
        cca = basicsal * (3 / 100)
        gpf = basicsal * (1 / 100)
        lic = basicsal * (2 / 100)
#calculate Net Salary Of Employee
netsal=(basicsal+ta+da+hra+cca)-(gpf+lic)
#Display Employee Payment Slip
print("*"*50)
print("\tE M P L O Y E E  P A Y M E N T  S L E E P ")
print("*"*50)
print("\tEMPLOYEE NUMBER    :",eno)
print("\tEMPLOYEE NAME      :",ename)
print("\tEMPLOYEE DEPARTMENT:",edpt)
print("\tEMPLOYEE BASIC SALARY:",basicsal)
print("*"*50)
print("\tEMPLOYEE TA          :",ta)
print("\tEMPLOYEE DA          :",da)
print("\tEMPLOYEE HRA         :",hra)
print("\tEMPLOYEE CCA         :",cca)
print("\tEMPLOYEE GPF         :",gpf)
print("\tEMPLOYEE LIC         :",lic)
print("*"*50)
print("\tEMPLOYEE NET SALARY  :",netsal)
print("*"*50)
