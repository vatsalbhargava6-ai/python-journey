#WAP to store the following word meaning in a python dictionary
# tabl:a piece of furniture","list of facts & figures,
# cat:a small animal

dictionary = {
    "table" : ["a piece of furniture","list of facts & figures"],
    "cat" : "a small animal"
}
print(dictionary)

# you a given a list of the subjects for students, Assume  one classroom is required for 1 subject. Howmany classrooms  are needed for the students.
#"python","java","C++","python","javascript","java","python","java","C++","C"

set = {
    "python", "python", "python", "java", "java",
      "java", "C++", "C++", "C", "javascript"
       
       }
       
print(len(set))

#WAP to enter marks of 3 subjects  from the user and store themin a dictionary.
 #start with and empty dictionary & add one by one. Use subject name as key &  marks as value

marks = {}

x = int(input("enter phy"))

marks.update({"physics" : x})



y = int(input("enter chem"))
marks.update({"chem" : y})
z = int(input("enter math"))
marks.update({"math" : z})


print(marks)

#figure out a way to store  9&9.0 as separate values in the set.
values = {9,"9.0"}
print(values)

#method 2
SET = {
    ("float", 9), ("int", 9.0)
    
}

print(SET)





























