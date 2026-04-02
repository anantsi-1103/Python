from abc import ABC, abstractmethod

File_name = "Project2/students.txt"


#abstract class
class Person(ABC):

    @abstractmethod
    def display(self):
        pass


# Inheritance + Encapsulate
class Student(Person):

    def __init__(self, roll , name , marks):
        self.__roll = roll
        self.__name = name
        self.__marks = marks

    def get_roll(self):
        return self.__roll
    
    def get_name(self):
        return self.__name
    
    def get_marks(self):
        return self.__marks


    # setter method 
    def set_marks(self,marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        
    # Polymorhphism
    def display(self):
        print(f" Roll: {self.__roll}")
        print(f" Name: {self.__name}")
        print(f" Marks: {self.__marks}")
        print(f" Grade: {self.calculate_grade()}")
        print("--------------------------")
        #

    def calculate_grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75:
            return "B"
        elif self.__marks >= 60:
            return "C"
        else:
            return "D"
        

class GraduateStudent(Student):

    def __init__(self, roll, name, marks , specilization):
        super().__init__(roll, name, marks)
        self.specilization = specilization

    
    def display(self):

        super().display() # remaining wale print 
        print(f" Specilization: {self.specilization}")
        print("--------------------------")


# store krne k liye
def save_student(student):
        with open(File_name, 'a') as file:
            if isinstance(student, GraduateStudent):
                data = f"G, {student.get_roll()}, {student.get_name()} , {student.get_marks()}, {student.specilization}\n"

            else:
                 data = f"S, {student.get_roll()}, {student.get_name()} , {student.get_marks()}\n"


            file.write(data)

# retireve
def load_Students():

    students = []

    try:
        with open(File_name, 'r') as file:

            for line in file:

                data = line.strip().split(',')

                # remove spaces
                data = [d.strip() for d in data]

                if data[0] == "G":

                    student = GraduateStudent(
                        int(data[1]),
                        data[2],
                        int(data[3]),
                        data[4]
                    )

                else:

                    student = Student(
                        int(data[1]),
                        data[2],
                        int(data[3])
                    )

                students.append(student)   

    except FileNotFoundError:
        pass

    return students

def main():
    while True:

        print("\n -------- Student Management System --------- ")
        print("1. Add Student")
        print("2. Add Graduate Student")
        print("3. View Students")
        print("4. Exit")


        choice = int(input("Enter your Choice!!!"))

        if choice == 1:
            roll = int(input("Enter your Roll No : "))
            name = (input("Enter your Name : "))
            marks = int(input("Enter your Marks : "))

            student = Student(roll, name, marks)
            save_student(student)

            print("Student Data Saved !!!")

        elif choice == 2:

            roll = int(input("Enter your Roll No : "))
            name = (input("Enter your Name : "))
            marks = int(input("Enter your Marks : "))
            sp = (input("Enter your Specialization : "))

            student = GraduateStudent(roll, name, marks,sp)
            save_student(student)

            print("Graduate Student Data Saved !!!")


        elif choice == 3:

            students = load_Students()


            if not students:
                print("No Records Found")

            else:
                for s in students:
                    s.display()

        elif choice == 4:
            print("Exit")
            break

        else:
            print("Invalid Choice")



# starter hai
if __name__ == "__main__":
    main()
