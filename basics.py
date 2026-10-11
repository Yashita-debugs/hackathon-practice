age =19
name ="Yashita Singhal"
height = 5.9
isStudent= True
marks= int(input("Enter your marks: "))
if marks >= 90 and marks<70:
    print("Your grade is A")
elif marks >=70 and marks<50:
    print("Your grade is B")
elif marks>=50 and marks< 20:
    print("Your grade is C")
else:
    print("Fail")
print("\n Lists in python")
for i in range(10,2,50):
    print(i)

fruits=["cherry","kiwi"]
fruits.append("mango")
for i in fruits:
    print(i)
print("\n index based accessing in lists")
print(fruits[1])
print("\n Dictionaries in Python")
student={"Name":"Yashita","branch":"BCS","Year":"2nd"}
print(student["Name"])
student["cgpa"]=8.5
print(student)
for i in student:
    print(i, student[i])