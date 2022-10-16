# Create an endless iterator using generator method to produce terms of Fibonacci
# series

from re import A


def endless_fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

lis=[]
it=iter(endless_fib())
while True:
    ans=input("Do you want to generate more element [y/n]:")
    if ans=='y':
        lis.append(next(it))
        print(lis[-1])
    else:
        print("The element generated by fibonacci series are : ")
        print(lis)
        break