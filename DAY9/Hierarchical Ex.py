class Teacher:
    def english(self):
        print("English Language")
class Student1(Teacher):
    pass

class Student2(Teacher):
    pass

obj1 = Student1()
obj2 = Student2()
obj1.english()
obj2.english()
