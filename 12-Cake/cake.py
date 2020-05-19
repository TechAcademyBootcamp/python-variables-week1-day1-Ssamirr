print('Three positive integers')
r=int(input("radius-table: "))
w=int(input("width-cake: "))
l=int(input("length-cake: "))
if (w*w+l*l)<=2*r:
    print("YES")
    exit()
print("NO")