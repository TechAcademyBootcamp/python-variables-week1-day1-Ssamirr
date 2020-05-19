print("Three integers: ")
first=input()
second=input()
third=input()
if first<second and first<third:
    print('Minimum:',first)
    exit()
if second<third:
    print("Minimum:",second)
    exit()
print("Minimum:",third)