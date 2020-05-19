domain=input("Enter domain: ")
i=5
l=[]
while i>0:
    page=input("Enter page: ")
    l.append(page)
    i-=1

print("5 pages tested on example.com")
for i in l:
    print("tested pages:",i)