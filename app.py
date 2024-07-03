import logging
from service.school_service import add_student_to_course, get_all_students_from_course, get_student_average_grade, add_grade
from src.school_db import Student, Teacher, Course

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)
    return logger

def main() -> None:
    setup_logging()

    # s1 = Student(name="John Doe", age=20, email="john.doe@example.com").save()
    # s2 = Student(name="Jane Smith", age=22, email="jane.smith@example.com").save()
    # s3 = Student(name="Michael Brown", age=21, email="michael.brown@example.com").save()
    # s4 = Student(name="Emily Davis", age=19, email="emily.davis@example.com").save()
    # s5 = Student(name="David Lee", age=23, email="david.lee@example.com").save()
    #
    # t1 = Teacher(name="John Smith", department="Mathematics", email="john.smith@example.com").save()
    # t2 = Teacher(name="Emily Brown", department="Physics", email="emily.brown@example.com").save()
    # t3 = Teacher(name="Michael Davis", department="Computer Science", email="michael.davis@example.com").save()
    #
    # c1 = Course(name="Introduction to Calculus", code="CAL101", teacher=t1).save()
    # c2 = Course(name="General Physics", code="PHY201", teacher=t2).save()
    # c3 = Course(name="Introduction to Python Programming", code="PYT301", teacher=t3).save()




    # Adding a Student to a Course: A function to enroll a student in a selected course.
    add_student_to_course('66853fe0639954fe839e9174', '6685428fabe082c9eaf1ab91')
    add_student_to_course('66853fe0639954fe839e9177', '6685428fabe082c9eaf1ab92')
    add_student_to_course('66853fe0639954fe839e9176', '6685428fabe082c9eaf1ab93')
    add_student_to_course('66853fe0639954fe839e9176', '6685428fabe082c9eaf1ab92')
    add_student_to_course('66853fe0639954fe839e9178', '6685428fabe082c9eaf1ab93')


    # Display List of Students from Course: A function that retrieves all students enrolled in a course.
    course_students = get_all_students_from_course('6685428fabe082c9eaf1ab93')
    for s in course_students:
        logging.info(s)


    # Adding Grade: A function that allows the teacher to grade a student for a given course.
    add_grade('66853fe0639954fe839e9176', '6685428fabe082c9eaf1ab92', 4.5)
    add_grade('66853fe0639954fe839e9176', '6685428fabe082c9eaf1ab92', 3.5)
    add_grade('66853fe0639954fe839e9176', '6685428fabe082c9eaf1ab93', 4.0)



    # Average Student Grade: A function that calculates a student's average grade for all courses in which the student is enrolled.
    logging.info(get_student_average_grade('66853fe0639954fe839e9176'))




if __name__ == '__main__':
    main()

