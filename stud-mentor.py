class Student:
    def __init__(self, name, surname, group_number):
        self.name = name
        self.surname = surname
        self.group_number = group_number
        self.continuing_courses = []
        self.courses_completed = []
        self.grades = {}
        students_list.append(self)

    def add_courses(self, course_name):
        self.courses_completed.append(course_name)

    def lecturer_score(self, lecturer, course_name, grade):
        if isinstance(lecturer, Lecturer) and course_name in self.continuing_courses \
                and course_name in lecturer.courses_belong and 1 <= grade <= 10:
            if course_name in lecturer.grades:
                    lecturer.grades[course_name] += [grade]
            else:
                lecturer.grades[course_name] = [grade]
        else:
            return 'Произошла ошибка. Лектор не читает данный курс.'

    def mid_grade(self):
        total_grade = 0
        grades_count = 0
        if len(self.grades) == 0:
            return 0
        else:
            for grades in self.grades.values():
                if len(grades) != 0:
                    for grade in grades:
                        total_grade += grade
                        grades_count += 1
            return total_grade / grades_count

    def __str__(self):
        return f"студент\n" \
               f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {round(self.mid_grade(), 1)}\n" \
               f"Курсы в процессе изучения: {', '.join(map(str, self.continuing_courses))}\n" \
               f"Завершенные курсы: {', '.join(map(str, self.courses_completed))}"

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.mid_grade() < other.mid_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_belong = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lecturers_list.append(self)

    def mid_grade(self):
        grades_list = []
        if not self.grades:
            return 0
        for value in self.grades.values():
            grades_list.extend(value)
        return round(sum(grades_list) / len(grades_list), 1)

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.mid_grade() < other.mid_grade()

    def __str__(self):
        return f"лектор\n" \
               f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {round(self.mid_grade(), 1)}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rating(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_belong and course in student.continuing_courses \
                and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Произошла ошибка. Студента нет на данном курсе.'

    def __str__(self):
        return f"рецензент\n" \
               f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}"

def mid_grade_all_lecturers(lecturers_list, course_name):
    all_lecturers_mid_grade = 0
    lecturers_count = 0
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course_name in lecturer.courses_belong:
            all_lecturers_mid_grade += lecturer.mid_grade()
            lecturers_count += 1
    if lecturers_count == 0:
        print('Произошла ошибка. Лектор не читает данный курс.')
    return round(all_lecturers_mid_grade / lecturers_count, 1)

def mid_grade_all_students(students_list, course_name):
    all_students_mid_grade = 0
    students_count = 0
    for student in students_list:
        if isinstance(student, Student) and course_name in student.continuing_courses:
            all_students_mid_grade += student.mid_grade()
            students_count += 1
    if students_count == 0:
        print('Произошла ошибка. Студента нет на данном курсе.')
    return round(all_students_mid_grade / students_count, 1)

students_list = []
lecturers_list = []

best_student = Student('Vasiya', 'Pupkin', 'group: Py-21-22')
bad_student = Student('Aliya', 'Vayzulina', 'group: Py-20-22')
best_student.continuing_courses += ['Python']
best_student.continuing_courses += ['Git']
best_student.add_courses('Java')
bad_student.continuing_courses += ['Python']
bad_student.continuing_courses += ['Git']
bad_student.add_courses('Java')

best_reviewer = Reviewer("Monty", "Python")
best_reviewer.courses_belong += ['Python']
best_reviewer.courses_belong += ['Git']

bad_reviewer = Reviewer("Bill", "Gates")
bad_reviewer.courses_belong += ['Python']
bad_reviewer.courses_belong += ['Java']

best_reviewer.rating(best_student, 'Python', 7)
best_reviewer.rating(best_student, 'Python', 9)
best_reviewer.rating(best_student, 'Python', 10)
best_reviewer.rating(best_student, 'Python', 8)
best_reviewer.rating(best_student, 'Git', 8)
best_reviewer.rating(best_student, 'Git', 9)
best_reviewer.rating(best_student, 'Git', 10)
best_reviewer.rating(best_student, 'Git', 7)

best_reviewer.rating(bad_student, 'Git', 5)
best_reviewer.rating(bad_student, 'Git', 4)
best_reviewer.rating(bad_student, 'Git', 6)
best_reviewer.rating(bad_student, 'Git', 3)
best_reviewer.rating(bad_student, 'Python', 3)
best_reviewer.rating(bad_student, 'Python', 3)
best_reviewer.rating(bad_student, 'Python', 6)
best_reviewer.rating(bad_student, 'Python', 7)

bad_reviewer.rating(best_student, 'Python', 5)
bad_reviewer.rating(best_student, 'Python', 6)
bad_reviewer.rating(best_student, 'Python', 6)
bad_reviewer.rating(best_student, 'Python', 7)
bad_reviewer.rating(best_student, 'Git', 7)
bad_reviewer.rating(best_student, 'Git', 6)
bad_reviewer.rating(best_student, 'Git', 5)
bad_reviewer.rating(best_student, 'Git', 6)

bad_reviewer.rating(bad_student, 'Git', 4)
bad_reviewer.rating(bad_student, 'Git', 3)
bad_reviewer.rating(bad_student, 'Git', 5)
bad_reviewer.rating(bad_student, 'Git', 3)
bad_reviewer.rating(bad_student, 'Python', 3)
bad_reviewer.rating(bad_student, 'Python', 3)
bad_reviewer.rating(bad_student, 'Python', 6)
bad_reviewer.rating(bad_student, 'Python', 5)

best_lecturer = Lecturer('Aristarh', 'Pitonov')
best_lecturer.courses_belong += ['Python', 'Git']
lecturers_list.append(best_lecturer)

bad_lecturer = Lecturer('Sinegurd', 'Popov')
bad_lecturer.courses_belong += ['Python', 'Java']
lecturers_list.append(bad_lecturer)

best_student.lecturer_score(best_lecturer, "Python", 6)
best_student.lecturer_score(best_lecturer, "Python", 8)
best_student.lecturer_score(best_lecturer, "Python", 7)
best_student.lecturer_score(best_lecturer, "Python", 9)
best_student.lecturer_score(bad_lecturer, "Python", 6)
best_student.lecturer_score(bad_lecturer, "Python", 5)
best_student.lecturer_score(bad_lecturer, "Python", 7)
best_student.lecturer_score(bad_lecturer, "Python", 8)

bad_student.lecturer_score(best_lecturer, "Python", 9)
bad_student.lecturer_score(best_lecturer, "Python", 8)
bad_student.lecturer_score(best_lecturer, "Python", 7)
bad_student.lecturer_score(best_lecturer, "Python", 9)
bad_student.lecturer_score(bad_lecturer, "Python", 6)
bad_student.lecturer_score(bad_lecturer, "Python", 7)
bad_student.lecturer_score(bad_lecturer, "Python", 6)
bad_student.lecturer_score(bad_lecturer, "Python", 5)

print("Лучший", best_lecturer, "\n")
print("Лучший", best_reviewer, "\n")
print("Лучший", best_student, "\n")
print(best_student > bad_student, "\n")
print(bad_lecturer > best_lecturer, "\n")
print("Средняя оценка лекторов", mid_grade_all_lecturers(lecturers_list, 'Python'), "\n")
print("Средняя оценка студентов", mid_grade_all_students(students_list, 'Python'))