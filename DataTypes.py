#Program For Demonstrating Data Types In Python
#In Python Their Are 14 Data Types They Are:
# 1)Fundamental Deta Type:
        #1.int() 2.float()  3.bool()  4.complex()
a=10  #Here a is Called Identifier And '10' Is Called Literal
print(a,type(a),id(a))  #O/p :10 <class 'int'> 2577464715856
b=10.5
print(b,type(b),id(b))  #o/p :10.5 <class 'float'> 1791902972816
c=True #or False 'T' & 'F' Must Be Capital
print(c,type(c),id(c))  #O/p: True <class 'bool'> 140717901244520
d=2+3j
print(d.real)  #Real Part 2.0
print(d.imag)  #imag Part 3.0
print(d,type(d),id(d)) #O/p :(2+3j) <class 'complex'> 2197510650480

# 2) Sequence Data type :
        # 5)str()  6)bytes()  7)bytearray()  8)range()

s="python"  #single Line Sting
print(s,type(s),id(s))  #O/p :python <class 'str'> 2342370757552

s1='''\tGuido Van Rossum
      Python Language Developer
      USA
      Python Language Realesed In Year 1991
      '''  #Multi Line String
print(s1,type(s1))
"""Output:
Guido Van Rossum
Python Language Developer
USA
Python Language Realesed In Year 1991
<class 'str'>"""

#Indexing
s2="Hyderabad"  #Index Always Start From 0...1...2...n Forword===>
                #BackWord Indesx -1...-2...-n
print(s2[2])  #d
print(s2[-3]) #b
#Slicing
#Begin:End
print(s2[0:-1]) #Hyderaba
print(s2[-3:-1]) #ba
#Begin
print(s2[3:])  #erabad
#End
print(s2[:4]) #Hyde
#[:]
print(s2[:]) #Hyderabad
#strobj[Begin:End:End]
print(s2[0:10:2]) #Hdrbd

#Type Casting In Python
a1=20
a2=float(a1)
print(a2,type(a2)) #20.0 <class 'float'>

a3=complex(a1)
print(a3,type(a3)) #(20+0j) <class 'complex'>

a4=str(a1)
print(a4,type(a4))  #20 <class 'str'>
print("="*70)
b=[10,20,30,40,50,60,70]
ba=bytes(b)
print(ba,type(ba))  #b'\n\x14\x1e(2<F' <class 'bytes'>
for val in ba:
    print("\t{}".format(val))
'''Output
10
	20
	30
	40
	50
	60
	70
'''
br=bytearray(b)
print(br,type(br))  #bytearray(b'\n\x14\x1e(2<F') <class 'bytearray'>
for val in br:
    print("\t{}".format(val))
'''Output
10
	20
	30
	40
	50
	60
	70
'''
#range Data Type
for i in range(1,11):
    print(i,end=" ")
'''OutPut
1 2 3 4 5 6 7 8 9 10 
'''
n=23
for i in range(1,11):
    print("\t{} X {} = {}".format(n,i,n*i))
'''Output
23 X 2 = 46
	23 X 3 = 69
	23 X 4 = 92
	23 X 5 = 115
	23 X 6 = 138
	23 X 7 = 161
	23 X 8 = 184
	23 X 9 = 207
	23 X 10 = 230
'''
#Generate Pattern Like 100 80 60 40 20 0
for i in range(100,-1,-20):
    print(i)
'''OutPut
100
80
60
40
20
0
'''
# 3)List Data Type
    # 9) List()  10) touple()

list=[10,20,30,40,50,60,10,20,40]
print(list,type(list))
'''Output
[10, 20, 30, 40, 50, 60, 10, 20, 40] <class 'list'>
'''
touple=(100,200,300,400,500)
print(touple,type(touple))
'''
(100, 200, 300, 400, 500) <class 'tuple'>
'''
#Create An Empty list
l=[]
l.append("Python")
l.append("Java")
print(l,type(l))
'''
['Python', 'Java'] <class 'list'>
'''
