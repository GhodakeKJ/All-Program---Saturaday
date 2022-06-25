#Program For Displays List,Touple,Set And Dict Values
def show(obj):
    print("="*50)
    print("Type Of Obj :",type(obj))
    print("Length Of Obj :", len(obj))
    print("=" * 50)
    for karan in obj:
        print("\t{}".format(karan))
def display(obj):
    print("=" * 50)
    print("Type Of Obj :", type(obj))
    print("Length Of Obj :",len(obj))
    print("=" * 50)
    for k,v in obj.items():
        print("\t{}\t\t{}".format(k,v))
#Main Program
karan=[10,20,30,40,50,60,70,80,90,100]
show(karan) #Function Call 1
set={10,20,30,40,50,60,70,10,20,30,50,3070,700}
show(set) #Function Call 2
touple=("Python","Java","Android","Django","HTML")
show(touple) #Function Call 3
dict={10:"Karan",20:"Abhi",30:"Scott",40:"Rossum",50:"Gosling"}
display(dict)