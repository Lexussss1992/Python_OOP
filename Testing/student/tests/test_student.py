from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student_without_courses = Student('Ivo')
        self.student_with_courses = Student('Ivo', {'Math': ['some note']})

    def test_init(self):
        self.assertEqual('Ivo', self.student_without_courses.name)
        self.assertEqual({}, self.student_without_courses.courses)
        self.assertEqual({'Math': ['some note']}, self.student_with_courses.courses)

    def test_enrolling_if_course_name_in_courses(self):

        result = self.student_with_courses.enroll('Math', ['note1', 'note2'])

        self.assertEqual(['some note', 'note1', 'note2'], self.student_with_courses.courses['Math'])
        self.assertEqual('Course already added. Notes have been updated.', result)

    def test_enrolling_if_add_notes_is_y(self):
        result = self.student_without_courses.enroll('History', ['note1', 'note2'], 'Y')

        self.assertEqual(['note1', 'note2'], self.student_without_courses.courses['History'])
        self.assertEqual('Course and course notes have been added.', result)

    def test_enrolling_if_add_notes_is_nothing(self):
        result = self.student_without_courses.enroll('History', ['note1', 'note2'])

        self.assertEqual(['note1', 'note2'], self.student_without_courses.courses['History'])
        self.assertEqual('Course and course notes have been added.', result)

    def test_enrolling(self):
        result = self.student_without_courses.enroll('History', ['note1', 'note2'], 'something else')

        self.assertEqual([], self.student_without_courses.courses['History'])
        self.assertEqual('Course has been added.', result)

    def test_adding_notes_if_course_name_in_courses(self):

        result = self.student_with_courses.add_notes('Math', ['note1', 'note2'])

        self.assertEqual('Notes have been updated', result)

    def test_adding_notes_if_course_name_not_in_courses(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_courses.add_notes('History', ['note1', 'note2'])

        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))

    def test_leaving_course_if_course_in_courses(self):

        result = self.student_with_courses.leave_course('Math')

        self.assertEqual('Course has been removed', result)

    def test_leaving_course_if_course_not_in_courses(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_courses.leave_course('History')

        self.assertEqual('Cannot remove course. Course not found.', str(ex.exception))


if __name__ == '__main__':
    main()