
from pymongo import MongoClient
class Student:
  def __init__(self, student_id, name, age):
       """
   Create a new student with ID, name, and age
       """
       self.student_id = student_id
       self.name = name
       self.age = age
  def to_dict(self): 
       """
    Convert student information to a dictionary for database storage
       """
       return {
        "student_id": self.student_id,
        "name": self.name,
        "age": self.age
        } 
class DatabaseConnection:
   def __init__(self, db_name="student_db", collection_name="students"):
           """
      Connect to the MongoDB database
           """
           self.client = MongoClient("mongodb://localhost:27017/")
           self.db = self.client[db_name]
           self.collection = self.db[collection_name]
   def get_collection(self):
          """
      Return the collection for database operations
          """
          return self.collection
class StudentDatabase:
   def __init__(self, db_connection):
         """
    Connect to the database collection
         """
         self.collection = db_connection.get_collection()
   def add_student(self, student):
         """
    Add a new student to the database
         """
         result = self.collection.insert_one(student.to_dict())
         return f"Student with ID {result.inserted_id} was successfully added."
   def remove_student(self, student_id):
         """
    Remove a student from the database using their ID
         """
         result = self.collection.delete_one({"student_id": student_id})
         if result.deleted_count > 0:
          return f"Student with ID {student_id} was removed."
         else:
          return "No student found with this ID."
   def search_student(self, student_id):
        """
    Search for a student using their ID
        """
        student = self.collection.find_one({"student_id": student_id})
        if student:
          return student
        else:
          return "No student found with this ID."
   def display_students(self):
       """
    Display all students stored in the database
       """
       students = self.collection.find()
       return list(students)
class Application:
   def __init__(self):
       self.db_connection = DatabaseConnection()
       self.student_db = StudentDatabase(self.db_connection)
   def run(self):
      while True:
          print("\nStudent Management System")
          print("1. Add Student")
          print("2. Remove Student")
          print("3. Search Student")
          print("4. Display All Students")
          print("5. Exit")
          choice = input("Choose an option: ")
          if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            student = Student(student_id, name, age)
            print(self.student_db.add_student(student))
          elif choice == "2":
            student_id = input("Enter Student ID to Remove: ")
            print(self.student_db.remove_student(student_id))
          elif choice == "3":
            student_id = input("Enter Student ID to Search: ")
            result = self.student_db.search_student(student_id)
            print(result)
          elif choice == "4":
            students = self.student_db.display_students()
            for student in students:
              print(student)
          elif choice == "5":
            print("Exit")
            break
          else:
            print("Invalid option. Please try again.")
