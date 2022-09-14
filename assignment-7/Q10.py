color=input("Enter your favourite color : ")
lis=['yellow','blue','orange','white','black','red']
for i in lis:
    if i in color:
        c=i
        break
else:
    c="other"
match color:
    case 'yellow':
        print("Monday")
    case 'blue':
        print("Tuesday")
    case 'orange':
        print('Wednesday')
    case "white":
        print("Thursday")
    case 'black':
        print("Friday")
    case "red":
        print("Saturday")
    case "other":
        print("Sunday")