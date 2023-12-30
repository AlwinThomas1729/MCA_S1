keys=input("Enter keys of dictionary 1: ").split()
values=input("Enter values of dictionary 1: ").split()
s={}
j=0
for i in keys:
    s[i]=values[j]
    j+=1
print("Dictionary 1: ",s)
keys1=input("Enter keys of dictionary 2: ").split()
values1=input("Enter values of dictionary 2: ").split()
s1={}
j=0
for i in keys1:
    s1[i]=values1[j]
    j+=1
print("Dictionary 2: ",s1)
s.update(s1)
print("Merged Dictionary: ",s)