domain=input("Enter domain: ")
count=0
i=5
l=[]
while i>0:
    page=input("Enter page: ")
    l.append(page)
    i-=1
    choose=int(input("Choose 1(successful) or 0(Failed): "))
    if choose==1:
        count+=1


print(f"5 pages are tested, {count} of them were succesfull and {5-count} of them failed")