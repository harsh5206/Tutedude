dic= {'Alice':45, 'John':96}

name= input("Enter the student's name: ")

if name in dic:
    print("{}'s marks: {}".format(name, dic[name]))
else:
    print("Student not found.")