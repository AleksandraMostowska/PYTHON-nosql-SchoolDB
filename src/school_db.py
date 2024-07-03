from mongoengine import (
    connect,
    Document,
    StringField,
    EmailField,
    ReferenceField,
    ListField,
    FloatField,
    IntField,
)

connect('users_db', host='localhost', port=27017)

# School Management System


class Student(Document):
    name = StringField(required=True)
    age = IntField()
    email = EmailField(max_length=35)
    courses = ListField(ReferenceField('Course'))

    def __str__(self):
        return f'{self.name} {self.age} {self.email}'

    def __repr__(self):
        return str(self)


class Teacher(Document):
    name = StringField(required=True)
    department = StringField(required=True)
    email = EmailField(max_length=35)
    courses = ListField(ReferenceField('Course'))

    def __str__(self):
        return f'{self.name} {self.department} {self.email} {self.courses}'

    def __repr__(self):
        return str(self)


class Course(Document):
    name = StringField(required=True)
    code = StringField(required=True, max_length=10)
    teacher = ReferenceField('Teacher')
    students = ListField(ReferenceField('Student'))

    def __str__(self):
        return f'{self.name} {self.code} {self.teacher} {self.students}'

    def __repr__(self):
        return str(self)


class Grade(Document):
    student = ReferenceField('Student')
    course = ReferenceField('Course')
    grade = FloatField()

    def __str__(self):
        return f'{self.student} {self.course} {self.grade}'

    def __repr__(self):
        return str(self)



