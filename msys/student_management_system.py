class Student:
    # Constructor
    def __init__(self, firstName, lastName, age, yearLevel):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.yearLevel = yearLevel

    # Return to Menu
    def return_to_menu(self):
        valid_choices = {'y': self.StudentMenu, 'n': self.Exit}
        valid_choice = False
        while not valid_choice:
            choice = input("Return to menu?[y/n]: ")
            if choice not in valid_choices:
                print("ERROR | invalid_input")
            else:
                valid_choice = True
        valid_choices[choice]()

    # [1] | Add Student
    def AddStudent(self):
        print("adding student...")
        valid_student_first_name = False
        valid_student_last_name = False
        valid_student_age = False
        valid_student_year_level = False

        while valid_student_first_name == False:
            student_first_name = input("First Name: ")
            if student_first_name.strip():
                valid_student_first_name = True
            else:
                print("ERROR | invalid_student_first_name")

        valid_student_last_name = False

        while valid_student_last_name == False:
            student_last_name = input("Last Name: ")
            if student_last_name.strip():
                valid_student_last_name = True
            else:
                print("ERROR | invalid_student_last_name")

        while valid_student_age == False:
            student_age = int(input("Age: "))
            if student_age >= 5:
                valid_student_age = True
            else:
                print("ERROR | student_age_must_be_five_years_or_above")

        print("Eligible Year Level/s:")
        print("-----------------------------------")
        print("Elementary | Grade 1 - 6")
        print("High School | Grade 7 - 10")
        print("Senior High School | Grade 11 - 12")
        print("-----------------------------------")

        while valid_student_year_level == False:
            student_year_level = int(input("Year Level: "))
            if student_year_level >= 1 and student_year_level <= 12:
                valid_student_year_level = True
            else:
                print("ERROR | invalid_student_year_level")
            if student_year_level >= 1 and student_year_level <= 6:
                education_level = "Elementary"
            elif student_year_level >= 7 and student_year_level <= 10:
                education_level = "High School"
            elif student_year_level == 11 or student_year_level == 12:
                education_level = "Senior High School"
            else:
                education_level = "N/A" # Backup
        print("student added successfully!")
        self.return_to_menu()

    # [2] | Add Instructor
    def AddInstructor(self):
        print("adding instructor...")
        valid_instructor_name = False

        while valid_instructor_name == False:
            instructor_name = input("Name: ")
            if instructor_name.strip():
                valid_instructor_name = True
            else:
                print("ERROR | invalid_instructor_name")
        self.return_to_menu()

    # [3] | Add Department
    def AddDepartment(self):
        print("adding department...")
        self.return_to_menu()

    # [4] | Add Course
    def AddCourse(self):
        print("adding course...")
        self.return_to_menu()

    # [5] | Edit Student Info
    def EditStudentInfo(self):
        print("editing student info...")
        self.return_to_menu()

    # [6] | Edit Instructor Info
    def EditInstructorInfo(self):
        print("editing instructor info...")
        self.return_to_menu()

    # [7] | Edit Department Details
    def EditDepartmentDetails(self):
        print("editing department details...")
        self.return_to_menu()

    # [8] | Edit Course Details
    def EditCourseDetails(self):
        print("editing course details...")
        self.return_to_menu()

    # [9] | Assign Student
    def AssignStudent(self):
        print("assigning student...")
        self.return_to_menu()

    # [10] | Assign Instructor
    def AssignInstructor(self):
        print("assigning instructor...")
        self.return_to_menu()

    # [11] | Calculate Student Grades
    def CalculateStudentGrades(self):
        print("calculating student grades...")
        self.return_to_menu()

    # [12] | Release Grades
    def ReleaseGrades(self):
        print("releasing grades...")
        self.return_to_menu()

    # [13] | Exit
    def Exit(self):
        print("exiting system...")

    def calculateGrades(self):
        print("calculating grades...")
        
    def displayGrades(self):
        print("displaying grafes...")    
        
    def displayInfo(self):
        print("| STUDENT INFO |")
        print(f'First Name: {self.firstName}')
        print(f'Last Name: {self.lastName}')
        print(f'Age: {self.age}')
        print(f'Year Level: {self.yearLevel}')

    # Display Student Menu
    def StudentMenu(self):
        print("===+==+==+== iSMS ==+==+==+===")
        print("| -Student-Management-System- |")
        print(" -_-_-_-_-_[STUDENT]_-_-_-_-_-")
        print("-------------------------------")
        print("[1] | Add Student")
        print("[2] | Add Instructor")
        print("[3] | Add Department")
        print("[4] | Add Course")
        print("[5] | Edit Student Info")
        print("[6] | Edit Instructor Info")
        print("[7] | Edit Department Details")
        print("[8] | Edit Course Details")
        print("[9] | Assign Student")
        print("[10] | Assign Instructor")
        print("[11] | Calculate Student Grades")
        print("[12] | Release Grades")
        print("[13] | Exit")
        print("-------------------------------")

        # Function Library
        input_choice = {
            1: self.AddStudent,
            2: self.AddInstructor,
            3: self.AddDepartment,
            4: self.AddCourse,
            5: self.EditStudentInfo,
            6: self.EditInstructorInfo,
            7: self.EditDepartmentDetails,
            8: self.EditCourseDetails,
            9: self.AssignStudent,
            10: self.AssignInstructor,
            11: self.CalculateStudentGrades,
            12: self.ReleaseGrades,
            13: self.Exit
        }

        # Exception Handling
        try:
            choice = int(input(">> "))
            if choice in input_choice:
                input_choice[choice]()
            else:
                print("ERROR | out_of_bounds_input")

        except ValueError:
            print("ERROR | invalid_input")

default = Student("", "", 0, 0)
#default.Menu() # [PROGRAM]
default.StudentMenu() # [DEBUGGING]
