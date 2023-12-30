keys=input("Enter keys for dictionary: ").split()
values=input("Enter values for dictionary: ").split()
s = dict(zip(keys,values))
keys.sort()
ascending_s={i:s[i] for i in keys}
keys.reverse()
descending_s={i:s[i] for i in keys}
print("Original Dictionry: ", s)
print("Dict in ascending order: ", ascending_s)
print("Dict in descending order: ", descending_s)