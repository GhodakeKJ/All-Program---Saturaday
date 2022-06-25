#studentreportcared2.py
def reportcard():
	while(True):
		sno=int(input("Enter Student Number:"))
		if(sno>=1) and (sno<=300):
			break
		print("please enter student number with in 1 to 300 only")
	sname=input("Enter student full name:")
	cname=input("Enter student college name:")
	while(True):
		python=float(input("Enter marks in python subject:"))
		if(python>=0) and (python<=100):
			break
		print("please Enter python marks within 0 to 100")
	while(True):
		cpp=float(input("enter marks in c++ subject:"))
		if(cpp>=0) and (cpp<=100):
			break
		print("plaese enter c++ marks within 0 to 100")
	while(True):
		java=float(input("Enter marks in java subject:"))
		if(java>=0) and (java<=100):
			break
		print("please enter java marks within 0 to 100")
	totalmarks=python+cpp+java
	average=(totalmarks/300)*100

	if(python<=40) or(cpp<=40) or(java<=40):
		grade="fail"
	else:
		if(totalmarks>=250) and (totalmarks<=300):
			grade="destination"
		elif(totalmarks>=200) and (totalmarks<=249):
			grade="first"
		elif(totalmarks>=150) and (totalmarks<=199):
			grade="second"
		else:
			if(totalmarks>=120) and (totalmarks<=149):
				grade="third"
		print("*"*60)
		print("\t** S T U D  E N T   R E P O R T  C A R D  2 0 2 0 **")
		print("="*60)
		print("\t student exam number:",sno)
		print("\t student  full name:",sname)
		print("\t student college name:",cname)
		print("-"*60)
		print("\t student marks in python:",python)
		print("\t student marks in c++:",cpp)
		print("\t student marks in java:",java)
		print("-"*60 )
		print("\t student total marks:",totalmarks)
		print("\t student average:",average)
		print("="*60)
		print("\t student grade:",grade)
		print("*"*60)
#Main Program
reportcard()



