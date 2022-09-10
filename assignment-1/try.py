# x=int(input('enter a no. :'))
# if x>0:
#     print(x,' is positive number : ')
# if x<=0:
#     print(x,' is not positive number :')

# x=1
# for i in range(5,51):
#     for j in range(5,0,-1):
#         x=x*j
#         if(j==1):
#             print('factorial of ',i,'is :',x)
#             continue



# x=int(input('enter a no. :'))
# print('positive ' if x>0 else 'non-positive')

# print('positve ' if int(input('Enter a no. :'))>0 else 'non-positive ')



# x=5
# match x:
#     case 1:
#         print('hey !')
#     case 5:
#         print('Ram Ram')
    

# print(eval(input('enter the data :')))

# x=eval(input('enter the data :'))

# match x:
#     case 'hello':
#         print('hello type is',type(x))
#     case 1:
#         print('1 type is ',type(x))
#     case True:
#         print('true type is',type(x))

# x=1
# while x<=5:
#     print('MySirG ',end="")
#     x+=1

# x=1
# while x>5:
#     print(x,end=" ")
#     x-=1
# else:
#     print('bye')

# x=input('enter the string :')
# j=0
# for i in x:
#     if(i=='a'):
#         j+=1
# print('total no. of a in the string are :',j)

# x='12345'
# for i in x:
#     if(i=='23'):
#         print('break')
#         break
# else:
#     print('break not executed')


# x=input('enter the string :')

# for i in x:
#     if(i=='r'):
#         print('break')
#         break
#     else:
#         print(i)
# else:
#     print('all the character successfully printed')

# print('enter the 3 no. :')
# x=int(input())
# y=int(input())
# z=int(input())

# if x>y and x>z:
#     print(x)
# elif y>x and y>z:
#     print(y)
# elif z>x and z>y:
#     print(z)


# n = int(input('enter the no. :'))
# s=0
# for i in range(1,n+1):
#     s=s+i
# print('sum of first ',n,' natural no. are :',s)

# x=3+4j

# print(x.imag)




# l1=[1,2,3,4,5]
# x=0
# for i in l1:
#     if i==4:
#         l1.remove(i)
    
# print(l1)


# n=int(input("enter the no. :"))
# print("enter the list elements :")
# l=[]
# i=0
# while i<n:
#     l.append(int(input()))
#     i+=1
# print(l)



# print("enter the list elements :")
# x=eval(input())
# print(x)



# l1=[1,5,4,3,2]
# # l1.sort()
# # print(l1)

# l1.sort(reverse=True)
# print(l1)

# x=4.5
# y=4.5
# print(hash(x))
# print(hash(y))


# x="12345"
# print(sum([int(i) for i in x]))\

x=[1,2,3,4,5,6]
print(list([i for i in x if i%2==0]))
