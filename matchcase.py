try:
    print("="*60)
    print("\tArithmatic Opearators")
    print("="*60)
    print("\t1.Addition")
    print("\t2.Subtraction")
    print("\t3.Multiplication")
    print("\t4.Divition")
    print("\t5.Modulo Division")
    print("\t6.Exponatitation")
    print("\t7.Remainder")
    print("="*60)
    ch=int(input("Enter Your Choice  :"))
    match(ch):
        case 1:
            a=int(input("Enter Value For a Addition :"))
            b=int(input("Enter Value For b Addition :"))
            sum=a+b
            print("Addition Of a and b ={}".format(sum))
        case 2:
            a = int(input("Enter Value For a Subtraction :"))
            b = int(input("Enter Value For b Subtraction :"))
            sub = a - b
            print("Subtraction Of a and b ={}".format(sub))
        case 3:
            a = int(input("Enter Value For a Multiplication :"))
            b = int(input("Enter Value For b Multiplication :"))
            mul = a * b
            print("Multiplication Of a and b =",mul)
        case 4:
            a = int(input("Enter Value For a Division :"))
            b = int(input("Enter Value For b Division :"))
            div = a / b
            print("Division Of a and b ={}".format(div))
        case 5:
            a = int(input("Enter Value For a Modulo Div :"))
            b = int(input("Enter Value For b Modulo Div :"))
            modudiv = a // b
            print("Modulo Div Of a and b ={}".format(modudiv))
        case 6:
            a = int(input("Enter Value For Base :"))
            b = int(input("Enter Value For Power :"))
            expo = a ** b
            print("Exoponasional Div Of a and b ={}".format(expo))
        case 7:
            a = int(input("Enter Value For Base :"))
            b = int(input("Enter Value For Power :"))
            Remainder = a % b
            print("Exoponasional Div Of a and b ={}".format(Remainder))
        case _:
            print("Your Choice is Invalid Cheak And Try-Again!")
except ValueError:
    print("strs,Special Symbols And Alpha-Numerics Are Not Allowed !")



