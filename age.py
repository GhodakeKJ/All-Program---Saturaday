age=int(input("Enter Age Of Citizen For Cheacking Eligible For Vote :"))
if(age>=18):
    print("{} Is Eligible For Vote ".format(age))
else:
    print("{} Is Not Eligible For Vote".format(age))