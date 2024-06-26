import unittest
from main import Teacher, DisciplineTeacher


class TestTeacher(unittest.TestCase):
    teacher = Teacher('test_name', 'test_education', 'test_experience')

    def test_1_1_init(self):
        self.assertEqual(isinstance(self.teacher.employers_list, list), True)

    def test_1_2_teacher_get_discipline(self):
        self.assertEqual(self.teacher.get_name(), 'test_name')

    def test_1_3_get_education(self):
        self.assertEqual(self.teacher.get_education(), 'test_education')

    def test_1_4_get_experience(self):
        self.assertEqual(self.teacher.get_experience(), 'test_experience')

    def test_1_5_set_experience(self):
        self.assertEqual(self.teacher.set_experience('test_new_experience'), 'test_new_experience')

    def test_1_6_get_teacher_data(self):
        self.assertEqual(self.teacher.get_teacher_data(),
                         'test_name, образование test_education, опыт работы test_new_experience года.')

    def test_1_7_add_mark(self):
        self.assertEqual(self.teacher.add_mark('test_student', 5), 'test_name поставил оценку 5 студенту test_student.')

    def test_1_8_remove_mark(self):
        self.assertEqual(self.teacher.remove_mark('test_student', 5),
                         'test_name удалил оценку 5 студенту test_student.')

    def test_1_9_give_a_consultation(self):
        self.assertEqual(self.teacher.give_a_consultation('test_class'),
                         'test_name провел консультацию в классе test_class.')

    def test_1_91_fire_employer(self):
        self.assertEqual(self.teacher.fire_employer(),
                         'Сотрудник test_name, образование test_education, опыт работы test_new_experience года.'
                         ' был уволен.')


class TestDisciplineTeacher(unittest.TestCase):
    discipline_teacher = DisciplineTeacher('test_name', 'test_education', 'test_experience',
                                           'test_discipline', 'test_job_title')

    def test_2_1_init(self):
        self.assertEqual(isinstance(self.discipline_teacher.employers_list, list), True)

    def test_2_2_get_discipline(self):
        self.assertEqual(self.discipline_teacher.get_discipline(), 'test_discipline')

    def test_2_3_get_job_title(self):
        self.assertEqual(self.discipline_teacher.get_job_title(), 'test_job_title')

    def test_2_4_set_job_title(self):
        self.discipline_teacher.set_job_title('set_test_job_title')
        self.assertEqual(self.discipline_teacher.get_job_title(), 'set_test_job_title')

    def test_2_5_get_teacher_data(self):
        self.assertEqual(self.discipline_teacher.get_teacher_data(), 'test_name, образование test_education, опыт работы test_experience года.\nПредмет test_discipline, должность set_test_job_title')

    def test_2_6_add_mark(self):
        self.assertEqual(self.discipline_teacher.add_mark('test_mark', 'test_student_name', 'test_discipline'),  'test_name поставил оценку test_student_name студенту test_mark.\nПредмет: test_discipline')

    def test_2_7_remove_mark(self):
        self.assertEqual(self.discipline_teacher.remove_mark('test_student_name',  'test_mark'), 'test_name удалил оценку test_mark студенту test_student_name.\nПредмет: test_discipline')

    def test_2_8_give_a_consultation(self):
        self.assertEqual(self.discipline_teacher.give_a_consultation(
            'test_class_name'),
            'test_name провел консультацию в классе test_class_name.\nПо предмету test_discipline '
            'как set_test_job_title')
