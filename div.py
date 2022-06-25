def division():
    try:
        a=int(input("Enter First Value :"))
        b=int(input("Enter Second Value :"))
        result=a/b
    except ZeroDivisionError as z:
        print("Don't Enter Zero For Denominator",z)
    except ValueError:
        print("Don't Enter strs,Special Symbols,And Alpha-Numerics")
    else:
        print("Division ({} and {})={}".format(a, b, result))
    finally:
        print("I Am From Finally Block")

#Main Program
division()