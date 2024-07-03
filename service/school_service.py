from src.school_db import Student, Course, Grade

# Adding a Student to a Course: A function to enroll a student in a selected course.
def add_student_to_course(student_id: str, course_id: str) -> None:
    student = Student.objects(id=student_id).first()
    course = Course.objects(id=course_id).first()

    if student and course:
        if course not in student.courses:
            student.courses.append(course)
            student.save()
        if student not in course.students:
            course.students.append(student)
            course.save()


# Display List of Students from Course: A function that retrieves all students enrolled in a course.
def get_all_students_from_course(course_id: str) -> [str]:
    course = Course.objects(id=course_id).first()
    if course:
        return [str(student) for student in course.students]

    raise ValueError("Course not found.")


# Adding Grade: A function that allows the teacher to grade a student for a given course.
def add_grade(student_id: str, course_id: str, grade_value: float) -> None:
    s = Student.objects(id=student_id).first()
    course = Course.objects(id=course_id).first()
    if s not in course.students:
        raise ValueError('Student is not in the given course. Cannot add grade.')

    grade = Grade(student=s, course=course, grade=grade_value)
    grade.save()


# Average Student Grade: A function that calculates a student's average grade for all courses in which the student is enrolled.
def get_student_average_grade(student_id: str) -> float:
    student = Student.objects(id=student_id).first()

    if student:
        return Grade.objects(student=student).average('grade')