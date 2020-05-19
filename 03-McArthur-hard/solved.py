print("Let's begin our game")
month=input("Enter birth month:")

while not month.isdigit() :
    month=input("Enter birth month(1-12):")

while  int(month)<1 or int(month)>12:
    month=input("Enter birth month(1-12):")

month=int(month)

age=input("Enter your age:")
while not age.isdigit():
    age=input("Enter your age:")

age=int(age)

special=int((month*2+5)*50+age-365)
print("special number:",special)
print((special+115)//100,(special+115)%100)


