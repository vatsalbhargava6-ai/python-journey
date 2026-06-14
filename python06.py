# # # print number  from 1 to 100
i = 1
while i <= 100:
    print(i)
    i+=1
# # # #print number from 100 to 1
i = 100
while i >= 1: #stopping condition
    print(i)
    i-=1
 
# # #print  the multiplication table of number n
# # #for n=18
i = 1
while i <=10:
    print(18*i)
    i+=1

# # #print the element of the following list using loop
# # #[1,4,9,16,25,36,49,64,81,100]
num  = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(num):
    print(num[idx])
    idx+=1
# #same  with heroes
heroes = ["vatsal", "radha", "krishna", "shiv", "ppl"]

idx = 0
while idx < len(heroes):
    print(heroes[idx])
    idx += 1


#print the element of the following list using loop
list = [1,4,9,16,25,36,49,64,81,100]
for A in list:
    print(A)
    
    #search  for a number x in  this tuple using loop
tup = (1,4,9,16,25,36,49,64,81,100,49)    
x = 49
A = 0
for val in tup:
    if(val == x):
        print("yeah num is there at idx:", A)
        break
    A+=1
    
#using for and range()
# print  numbers  from 1 to 100?

A = range(1, 101)
for val in A:
    print(val)
#print number from 100 to 1
A = range(100,0,-1)
for val in A:
    print(val)
    
#print the multiplication  table of number n.
n = int(input("write no."))

for i in range(1,11):
    print(n * i)
#WAP to find  the sum of first n natural number(USING WHILE)
n = 7

sum = 0
A = range(1, n+1)
for i in A:
    sum+=i
print("total sum =", sum)
#METHOD 2
n = 7
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("total sum=", sum)


#WAP to  find factorial of first n natural number(using for)
n = 5
i = 1
fact = 1
while i <= n:
    fact*=i
    i+=1
print("here it is", fact)
#M2
n = 5
fact = 1
A = range(1,n+1)
for i in A:
    fact*=i
print(fact)








































