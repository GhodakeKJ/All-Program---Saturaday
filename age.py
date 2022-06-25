while(True):
    age=int(input("Enter Citizen Age For Vote :"))
    if(age >=18 and age <=100 ):
        print("{} Age Citizen Are Eligible For Vote!".format(age))
        break
