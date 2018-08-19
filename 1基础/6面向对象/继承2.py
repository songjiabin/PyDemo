from 继承1 import Person


class Student(Person):
    studentId = 0

    def __init__(self, food, studentId):
        Person.__init__(self, food)
        self.__studentId = studentId

    def getStudentId(self):
        return self.__studentId


    def eat(self):
        print("Student")

