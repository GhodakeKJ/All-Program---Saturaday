a=int(input("Enter Any Number :"))
b=int(input("Enter Any Number :"))
print("="*50)
print("Original Value :")
print("Value Of a :",a)
print("Value Of b :",b)
print("="*50)
#Swapping Logic
a=a^b
b=a^b
a=a^b #By Using xor Operator
print("Swapped Value :")
print("Swapped Value of a:",a)
print("Swapped Value Of b:",b)
print("="*50)