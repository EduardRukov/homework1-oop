class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Ошибка")

        return self.counting() == other.counting()

    def __ne__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Ошибка")

        return self.counting() != other.counting()

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Ошибка")

        return self.counting() < other.counting()

    def __le__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Ошибка")

        return self.counting() <= other.counting()

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Ошибка")

        return self.counting() > other.counting()

    def __ge__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Ошибка")

        return self.counting() >= other.counting()

    def __str__(self):
        progress = ""
        finish = ""
        for i in self.courses_in_progress:
            progress += i + ", "
        for i in self.finished_courses:
            finish += i + ", "
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.counting()}\n" \
               f"Курсы в процессе изучения: {progress[:-2]}\nЗавершенные курсы: {finish[:-2]}"

    def counting(self):
        summa, count = 0, 0
        for i in self.grades:
            summa += sum(self.grades[i])
            count += len(self.grades[i])
        return summa / count

    def rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # список закрепленных курсов
        self.grades = {}


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Ошибка")

        return self.counting() == other.counting()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Ошибка")

        return self.counting() != other.counting()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Ошибка")

        return self.counting() < other.counting()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Ошибка")

        return self.counting() <= other.counting()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Ошибка")

        return self.counting() > other.counting()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Ошибка")

        return self.counting() >= other.counting()

    def counting(self):
        summa, count = 0, 0
        for i in self.grades:
            summa += sum(self.grades[i])
            count += len(self.grades[i])
        return summa / count

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.counting()}"


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Java']

cool_mentor.rate(best_student, 'Python', 10)
cool_mentor.rate(best_student, 'Java', 2)

cool_lecturer = Lecturer('SSS', 'BBB')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Java']

best_student.rate(cool_lecturer, 'Python', 9)

student = Student('Ruoy', 'Eman', 'your_gender')
student.courses_in_progress += ['Java']
student.rate(cool_lecturer, 'Java', 1)

cool_mentor.rate(student, 'Java', 2)

print(best_student < cool_mentor)
