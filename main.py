






class student:
    def__init__(self,name,roll_number,CGPA):
self.name=Name
self.roll number=roll_number
self.cgpa=cgpa
def sort_students(student_lists):
  #sort the list of students in des order of cgpa
  sorted_students=sorted (student lists,key=lambda student: student,cgpa,reverser=true)
  #syntax=lambda arg.exp
  return sorted_students#eg usage
students=[
        student("hari","a123",7.8),
      student("srikanth","a124",8.9)
      student ("Sowmya","a124",9.9)]
sorted_students=sort_students (students)
#print the sorted list of students
for student in sorted_students:
  print ("name={},roll no:{}, CGPA:{},format (student.name, student.roll no, student.cgpa"))