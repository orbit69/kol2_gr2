#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
from __future__ import division

class Student(object):
    def __init__(self, stud_id, name = " ", surname = " "):
        self.stud_id = stud_id
        self.name = name
        self.surname = surname
        self.scores = []
        self.lessons = []


    def add_score(self, score):
        if isinstance(score, int) and score <=6 and score >=1:
            self.scores.append(score)
        else:
            raise ValueError("Score value is incorrect, should be int <= 6 and >= 1")


    def add_attendance(self, is_attend):
        self.lessons.append(bool(is_attend))


    def get_attendance_percent(self):
        if self.lessons.__len__() == 0:
            return 0
        else:
            return (sum(self.lessons) / self.lessons.__len__()) * 100


    def get_average_score(self):
        if self.scores.__len__() == 0:
            return 0
        else:
            return sum(self.scores) / self.scores.__len__()


    def __str__(self):
        return "Student's id: " + str(self.stud_id)\
               + ", Name: " + self.name + " " + self.surname\
               + " Attendance %: " + str(self.get_attendance_percent())\
               + "% scores average: " + str(self.get_average_score())


class StudentsGroup(object):
    def __init__(self, group_id, group_name = " "):
        self.students = []
        self.name = group_name
        self.id = group_id


    def add_student(self, stud):
        self.students.append(stud)
        print stud.name, " ", stud.surname, " Has been added to StudentGroup ", self.name


    def remove_student(self, id):
        for i in range(self.students.__len__()):
            if self.students[i].stud_id == id:
                print "Student with id: ", id, "Has been removed"
                self.students.remove(self.students[i])
                return
        raise Exception("Student with that id doesnt exist")


    def get_group_average_score(self):
        if self.students.__len__() != 0:
            avr = 0
            for i in range(self.students.__len__()):
                avr += self.students[i].get_average_score()
            return avr / self.students.__len__()
        else:
            return 0


    def __str__(self):
        res = "StudentGroup id: " + str(self.id)\
              + " name: " + self.name\
              + " number of students: " + str(self.students.__len__())
        for i in range(self.students.__len__()):
            res += "\n" + str(self.students[i])
        res += "\nAverage score of students in " + self.name + " is: " + str(self.get_group_average_score())
        return res


if __name__ == "__main__":
    st1 = Student(1, "Jan", "Kowalski")
    st2 = Student(2, "Ola", "Mak")
    st3 = Student(3, "Ala", "Baca")

    sg = StudentsGroup(1, "Klasa")

    sg.add_student(st1)
    sg.add_student(st2)
    sg.add_student(st3)

    st1.add_score(3)
    st1.add_score(4)
    st1.add_attendance(0)
    st1.add_attendance(0)
    st1.add_attendance(1)
    print st1

    st2.add_score(1)
    st2.add_score(4)
    st2.add_attendance(True)
    st2.add_attendance(1)
    print st2

    print sg
