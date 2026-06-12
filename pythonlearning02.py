#WAP  to input  user first name  and  print its length

A = input("whats your name  sir/Ma'am")
print("lenth of your name is", len(A))  

#WAP  to find  the occurence of the $ symbol 
 
B = "Hey, im $symbol of the $company of net worth of $999999"
print(B.count("$")) 

#conditional statements 
#Grade students based on marks
# marks >= 90, grade = "A"
# 90 > marks >= 80, grade = "B"
# 80 > marks >= 70, grade = "C"
# 70 > marks, grade = "D"

marks = int(input("what is your marks, we will grade it"))

if(marks >= 90):
    grade = "A"
   
elif(marks >= 80 and marks < 90):
    grade ="B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else: 
    grade = "D"

print("grade of the students is", grade)



#lets  see if u can  drive  car or not write your age as input !
age = int(input("write your age sir"))




if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")


else:
    print("cannot drive nigger")
    


    










































































