import pytest
from source.school import Classroom, Student, Teacher, TooManyStudents, Person


@pytest.fixture
def sample_classroom():
    teacher = Teacher("Professor Snape")
    students = [Student(f"Student {i}") for i in range(5)]
    course_title = "Potions"
    return Classroom(teacher, students, course_title)


def test_classroom_initialization(sample_classroom):
    assert sample_classroom.teacher.name == "Professor Snape"
    assert len(sample_classroom.students) == 5
    assert sample_classroom.course_title == "Potions"


def test_add_student(sample_classroom):
    new_student = Student("Harry Potter")
    sample_classroom.add_student(new_student)
    assert len(sample_classroom.students) == 6


def test_add_student_raises_exception(sample_classroom):
    with pytest.raises(TooManyStudents):
        for i in range(6, 15):
            sample_classroom.add_student(Student(f"Student {i}"))
            print(sample_classroom.students)


def test_remove_student(sample_classroom):
    sample_classroom.remove_student("Student 3")
    assert len(sample_classroom.students) == 4

    # Interesting assert for all elements in a collection
    assert all(student.name != "Student 3" for student in sample_classroom.students)


def test_remove_nonexistent_student(sample_classroom):
    sample_classroom.remove_student("Nonexistent Student")
    assert len(sample_classroom.students) == 5


def test_change_teacher(sample_classroom):
    new_teacher = Teacher("Professor McGonagall")
    sample_classroom.change_teacher(new_teacher)
    assert sample_classroom.teacher.name == "Professor McGonagall"


def test_person_inheritance():
    person = Person("Random Person")
    assert person.name == "Random Person"


def test_student_inheritance():
    student = Student("Hermione Granger")
    assert student.name == "Hermione Granger"


def test_teacher_inheritance():
    teacher = Teacher("Professor Dumbledore")
    assert teacher.name == "Professor Dumbledore"


@pytest.mark.parametrize("initial_students, new_student, expected_count", [
    ([Student("Student 1"), Student("Student 2")], Student("Ron Weasley"), 3),
    ([Student("Student 1"), Student("Student 2"), Student("Student 3")], Student("Student 4"), 4),
])
def test_add_student_parameterized(sample_classroom, initial_students, new_student, expected_count):
    sample_classroom.students = initial_students
    sample_classroom.add_student(new_student)
    assert len(sample_classroom.students) == expected_count


def test_too_many_students_exception():
    teacher = Teacher("Professor Flitwick")
    students = [Student(f"Student {i}") for i in range(10)]

    for student in students:
        print(student.name)

    course_title = "Charms"
    classroom = Classroom(teacher, students, course_title)
    with pytest.raises(TooManyStudents):
        classroom.add_student(Student("Excess Student"))
