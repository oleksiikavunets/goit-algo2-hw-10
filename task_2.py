class Teacher:

    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects


def create_schedule(subjects, teachers):
    chosen_teachers = []
    uncovered_subjects = subjects.copy()

    for _ in range(len(subjects)):
        _teacher = max(teachers, key=lambda subset: len(subset.can_teach_subjects & uncovered_subjects))

        chosen_teachers.append(_teacher)
        _teacher.assigned_subjects = _teacher.can_teach_subjects & uncovered_subjects
        uncovered_subjects -= _teacher.can_teach_subjects

        if not uncovered_subjects:
            return chosen_teachers

    return None


if __name__ == '__main__':
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія', }

    teachers = [
        Teacher('Олександр', 'Іваненко', 45, 'o.ivanenko@example.com', {'Математика', 'Фізика'}),
        Teacher('Марія', 'Петренко', 38, 'm.petrenko@example.com', {'Хімія'}),
        Teacher('Сергій', 'Коваленко', 50, 's.kovalenko@example.com', {'Інформатика', 'Математика'}),
        Teacher('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com', {'Біологія', 'Хімія'}),
        Teacher('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com', {'Фізика', 'Інформатика'}),
        Teacher('Олена', 'Гриценко', 42, 'o.grytsenko@example.com', {'Біологія'})
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("\nРозклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
