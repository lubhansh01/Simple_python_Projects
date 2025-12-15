# School Management System

class Student:

  def __init__(self,name,student_id):
    self.name = name
    self.student_id = student_id
    self.enrolled_courses = []

  def enroll(self, course):
    if course not in self.enrolled_courses:
      success = course.add_student(self)
      if success:
        self.enrolled_courses.append(course)
        print(f"{self.name} enrolled in {course.course_name}")
      else:
        print(f"{self.name} is already enrolled in {course.course_name}")

  def drop(self, course):
    if course in self.enrolled_courses:
      course.remove_student(self)
      self.enrolled_courses.remove(course)
      print(f"{self.name} dropped {course.course_name}")
    else:
      print(f"{self.name} is not enrolled in {course.course_name}")
  
  def display_courses(self):
    if not self.enrolled_courses:
      print(f"{self.name} is not enrolled in any courses")
    else:
      print(f"{self.name}'s enrolled courses:")
      for course in self.enrolled_courses:
        print(f"- {course.course_name}")

class Course:
  def __init__(self, course_name, course_code, max_students):
    self.course_name = course_name
    self.course_code = course_code
    self.max_students = max_students
    self.enrolled_students = []

  def add_student(self, student):
    if len(self.enrolled_students) >= self.max_students:
      print(f"Course {self.course_name} is full. Cannot add {student.name}")
      return False
    if student not in self.enrolled_students:
      self.enrolled_students.append(student)
      return True

  def remove_student(self, student):
    if student in self.enrolled_students:
      self.enrolled_students.remove(student)
  
  def display_info(self):
    print("f\nCourse: {self.course_name}")
    print(f"Course Code: {self.course_code}")
    print(f"Max Students: {self.max_students}")
    print("Enrolled Students:")
    if not self.enrolled_students:
      print("No students enrolled")
    else:
      for student in self.enrolled_students:
        print(f"- {student.name}")

# Testing the System

# Create students
s1 = Student("Alice", 101)
s2 = Student("Bob", 102)
s3 = Student("Charlie", 103)

# Create courses
c1 = Course("Python Programming", "CS101", 2)
c2 = Course("Data Structures", "CS102", 1)

# Enroll students
s1.enroll(c1)
s2.enroll(c1)
s3.enroll(c1)   # should fail (capacity full)

s1.enroll(c2)
s2.enroll(c2)   # should fail

# Display information
s1.display_courses()
c1.display_info()

# Drop course
s1.drop(c1)
c1.display_info()
