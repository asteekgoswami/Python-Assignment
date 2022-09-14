year=int(input("Enter any year : "))
match year:
    case year if (year%4==0 and year%100!=0):
        print(year," is a not century leap year ")
    case year if year%400==0:
        print(year," is a century leap year ")
    case year if (year%4!=0 and year%100!=0):
        print(year," non century leap year")
    case year if (year%100==0 and year%4!=0):
        print(year," century non leap year" )