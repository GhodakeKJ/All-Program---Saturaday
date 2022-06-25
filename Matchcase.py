wd=input("Enter Your Choice (Week Day) :")
match(wd.lower()):
    case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
        print("{} Is Working Day".format(wd))
    case "Saturday":
        print("{} Is Week End Day".format(wd))
    case "Sunday":
        print("{} Is Holiday".format(wd))
    case _:
        print("{} Is Not Week Day".format(wd))
