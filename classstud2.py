class student :
    Grade = 10
    Name = "Ariya"

    def introduction(self):
        print("Hi, I am a student")

    def details(self):
        print("My name is", self.Name)
        print("I study in grade", self.Grade)


ob = student()
ob.introduction()
ob.details()