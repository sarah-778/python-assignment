students_name= ['sandra', "patricia","phionah","Anitah" ]
student_marks = [80,56,78,90]
data = ["sandra",90, "kamokya"]
print(students_name,type(students_name))
# APPENDING adding new item in the list.
students_name.append('michel')
print(students_name)
#print patricia, faith, phionah"
print('specific names:')
print(students_name[1])
print("faith(not in list)")
print(students_name[2])

#add marsha at the fouth position
students_name.insert(3 , "marsha")
print(students_name)

#update the name  phionah to aladina
students_name.index("phionah")
index_phionah ="aladina"
print('\nlst afterupdating phiona to aladina:')

#display length of the students list
length_of_the_students = len(students_name)
print("\nLength of the students list:",length_of_the_students)
#print all the student names using a for loop
print("\nAll students' names:" for students in students_name)
#calculate the tetal marks for the student mark variable [80,56,70,90]
marks = [80,56,78,90]
total_marks = sum(marks)
print("n/total marks for the students:",total_marks)