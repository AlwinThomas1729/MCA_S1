def fib(a,b,n,i):
    if(i>n):
        return
    else:
        c=a+b
        print(c)
        fib(b,c,n,(i+1))

n=int(input("Enter Limit: "))
print("Fibonacci Series:")
if(n==1):
    print(0)
else:
    print(0)
    print(1)
    fib(0,1,n-2,1)