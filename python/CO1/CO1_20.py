a=list(map(int,input("Enter numbers to list: ").split()))
print ("original List: ",a)
b=[i for i in a if i%2!=0]
print ("List after removing even numbers: ",b)