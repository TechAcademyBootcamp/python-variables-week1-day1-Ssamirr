# istifadəçinin doğulduğu ili soruşun və neçə yaşda olduğunu hesablayıb print edin
year=int(input("Doguldugunuz il: "))
now=2020-year
print("Hal-hazirdaki yash: ",now)
l1=[] #list first
l2=[] #list second
# ==============================================
# ==============================================
# 2022-ci ildə neçə yaşı olacaq?
then=2022-year
print("2022-de olacaq yash: ",then)
# ==============================================

# ==============================================

# iki rəqəmin ən böyük ortaq bölünənini tapın
for i in range(1,now+1):
    if now%i==0:
        l1.append(i)
        
for j in range (1,then+1):
    if then%j==0:
        l2.append(j)

for i in reversed(l1):
    for j in reversed(l2):
        if i==j:
            print(i)
            exit()


# ==============================================

# ==============================================