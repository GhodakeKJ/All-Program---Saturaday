while(True):
    age=int(input("enter age for vote:"))
    if(age >=18) and (age  <=100):
        print("{} age citizen age for eligible for vote!".format(age))
        break
