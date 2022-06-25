lst=[]  #lst=list()
lst.append(10)
lst.append(20)
lst.append("Python")
print(lst)
lst.insert(1,"Rossum")
lst.insert(3,"Karan")
print(lst)
lst.remove(10)
print(lst)
lst.pop()
print(lst)
lst.pop(1)
print(lst)

#Deep Copy
deep=lst
print(deep)
deep.append("Python")
deep.insert(1,"Android")
print(lst)
#['Python', 'Java'] <class 'list'>

#Shalow Copy
shalow=lst.copy()
print(shalow)
lst.insert(1,"Gosling")
print(shalow)
print(lst)
'''Output
['Rossum', 'Android', 'Karan', 'Python']
['Rossum', 'Gosling', 'Android', 'Karan', 'Python']
'''
print(lst.count("Python"))
print(lst)
print(lst.reverse())
print(lst.sort())
print(lst)
ls1=[10,20,30,50,40]
ls2=["Python","Java","Django"]
print(ls2.extend(ls1))

touple=(10,20,30)
print(touple,type(touple))
nestedlist=[ [10,20,30,40],["Python","Java,Django"],[100,200,300] ]
print(nestedlist,type(nestedlist))
print(nestedlist[1])
print(nestedlist[2])
print("="*80)
for val in nestedlist:
    print(val)

set={10,20,3040,10,30,40,50,50,30}
print(set,type(set))
set.add("python")
set.add("Django")
print(set)
set.remove(3040)
print(set)
set.discard(50)
print(set)
s1={10,20,30,40,50}
s2={30,40,50,60,70}
print(s1.union(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s1.update(s2))

#Dict Data Type
dict={10:"Apple",20:"Banana",30:"Mango",40:"Kiwi"}
print(dict)
dictc=dict
print(dictc)
print(dict.popitem())
print(dict.get(10))
print(dict.keys())
print(dict.values())
print(dict.items())
d1={10:"Java",20:"Python"}
d2={30:"Gosling",40:"Rossum"}
print(d1.update(d2))