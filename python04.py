#WAP to ask  the user to  enter names  of their 3  fav  movies & store  them in a list
a = input("1st movie")
b = input("2nd movie")
c = input("3rd movie")

movies = [a,b,c]
print(movies)


#WAP to check if a list  contains a palindrome  of elements.
list1 = [1,2,3,2,1]
list2 = [1,2,3]

A = list1.copy()
A.reverse()
if(list2 == A):
    print("True")
else:
    print("false")


#WAP to count the number  of studenswith grade"A"  in the following table 
tup = ("C","D","A","A","B","B","A")
 
print(tup.count("A"))

#tup = ("C","D","A","A","B","B","A")#store it in ascending order

grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)






















