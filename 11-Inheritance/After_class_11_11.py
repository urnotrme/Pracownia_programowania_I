class Student():
    def __init__(self, name, surname, field):
        self.name = name
        self.surname = surname
        self.field = field
        self.uni = "UEK Kraków"   
    def __str__(self):
        return f"{self.name} {self.surname} ({store_ID.ID}), {self.field}, {self.uni}"
        
class store_ID(Student):
    ID = 100000
    def store(self, ID):
        self.ID = ID
        
s1 = Student("Alina", "Markina", "Informatyka Stosowana")
print(s1)
store_ID.ID +=1
s2 = Student("Elżbieta", "Kowalska", "Organizacja i zarządzanie")
print(s2)
store_ID.ID +=1
s3 = Student("Małgorzata", "Wiśniewska", "Marketing")
print(s3)
    