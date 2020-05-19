category=input("Enter category code(r,c,i): ")
beforeUse=int(input("Before use water: "))
afterUse=int(input("After use water: "))

if category.lower()=="r":
    if afterUse>beforeUse:
        gallons=(afterUse-beforeUse)/10
        debt=5+gallons*0.0005
    print("Enter category code(r,c,i): ",category)
    print("Before use water: ",beforeUse)
    print("After use water: ",afterUse)
    print("Gallons: ",gallons)
    print("Debt: ",debt)


if category.lower()=="c":
    if afterUse>beforeUse:
        gallons=(afterUse-beforeUse)/10
        if gallons>4000000:
            debt = 1000 + (gallons-4000000) * 0.00025
        else:
            debt = 1000
    print("Enter category code(r,c,i): ",category)
    print("Before use water: ",beforeUse)
    print("After use water: ",afterUse)
    print("Gallons: ",gallons)
    print("Debt: ",debt)

if category.lower()=="i":
    if afterUse>beforeUse:
        gallons=(afterUse-beforeUse)/10
        if gallons>10000000:
            debt=3000 + (gallons - 10000000)*0.00025
        if gallons>4000000:
            debt=1000
        else:
            debt=2000
    print("Enter category code(r,c,i): ",category)
    print("Before use water: ",beforeUse)
    print("After use water: ",afterUse)
    print("Gallons: ",gallons)
    print("Debt: ",debt)
