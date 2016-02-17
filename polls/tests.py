import datetime
from django.test import TestCase
from django.utils import timezone

from polls.models import Question


class QuestionMethodTests(TestCase):

    def test_was_publishsed_recently_with_future_question(self):
        """
        was_published_recently() should return false for future questions
        """
        time = timezone.now() + timezone.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_questions(self):
        """
        was_published_recently() should return flase for question published older that 1 day
        """

        time = timezone.now() - timezone.timedelta(days=2)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(), False)

    def test_was_published_recently_with_normal_question(self):
        """
        was_published_recently() should return true for question published less than 1 day ago
        """

        time = timezone.now() - timezone.timedelta(hours=2)
        normal_question = Question(pub_date = time)
        self.assertEqual(normal_question.was_published_recently(), True)