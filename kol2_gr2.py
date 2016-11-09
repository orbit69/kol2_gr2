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

class Student(object):
    def __init__(self, stud_id, name = " ", surname = " "):
        self.stud_id = stud_id
        self.name = name
        self.surname = surname

        self.scores = []
        self.scores_sum = 0
        self.average_score = 0

        self.lesson_num = []    #numer lekcji to indeks a obecnosc to boolean
        self.curr_lesson = 0

    def add_score(self, score):
        self.scores_counter += 1
        self.scores_sum += score
        self.average_score = self.scores_sum / self.scores_counter

    def add_attendance(self, lesson_num, is_attend):
        self.curr_lesson += 1
        self.lesson_num[self.curr_lesson] = bool(is_attend)

    def get_attandance_percent(self):
        if self.curr_lesson != 0:
            res = sum(self.lesson_num) / self.curr_lesson
        else:
            res = 0
        return res

    def __str__(self):
        str = "Student id: " + self.student_id " name: " + self.name + " surname: " + self.surname, "/n"\
            "score average: " + self.average_score + "attandance %: " + self.get_attandance_percent()
        return str

class StudentsGroup(object):
    def __init__(self, group_id, group_name = " "):
        self.group = []
        self.name = group_name
        self.id = group_id
        self.size = 0

    def add_student(self, stud):
        self.group[self.size] = stud
        self.size += 1

    def __str__(self):
        str = "StudentGroup id: ", self.id, " name: ", self.name, " number of students: ", self.size
        for i in range(self.group.__len__()):
            str += self.group[i]
        return str


a = Student(1, "Jan", "Naj")
b = Student(2, "Ola", "Alo")

print a


