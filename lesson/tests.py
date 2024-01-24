from rest_framework import status
from rest_framework.test import APITestCase

from lesson.models import Lesson


class LessonTestCase(APITestCase):

    def test_case_lesson(self):
        """Test lesson"""
        data = {
            'title': 'Test',
            'description': 'Test',
            'link_video': 'https://youtube.com'
        }
        response = self.client.post(
            '/lesson/lesson/create/',
            data=data
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'pk': 1, 'title': 'Test', 'description': 'Test', 'course': None, 'user': None,
             'link_video': 'https://youtube.com'}
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_lesson(self):
        """Test List"""
        Lesson.objects.create(
            title='test1',
            description='test1',
            link_video='https://youtube.com'

        )
        response = self.client.get(
            '/lesson/lesson/'
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        print(response.json())
        self.assertEquals(
            response.json(),
            [{'count': 1, 'next': None, 'previous': None, 'results': [{'pk': 2, 'title': 'test1', 'description': 'test1', 'course': None, 'user': None, 'link_video': ''}]}])


