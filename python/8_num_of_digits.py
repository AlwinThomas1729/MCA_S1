num=int(input("Enter a number: "))
c=0
n=num
while(num>0):
    c+=1
    num=num//10
print(n,"has ",c," digits.")