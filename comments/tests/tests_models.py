from turtle import circle
from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Circle, Comment

# Create your tests here.

class CircleTestCase(TestCase):
    def setUp(self) -> None:
        Circle.objects.create(name='Familia')
        Circle.objects.create(name='Amigos')
    
    def test_create_new_circle(self):
        family = Circle.objects.get(name='Familia')
        friends = Circle.objects.get(name='Amigos')
        self.assertEqual(family.__str__(), 'Familia')
        self.assertEqual(friends.__str__(), 'Amigos')

class CommentTestCase(TestCase):

    def setUp(self):
        joao = User.objects.create(first_name='João', username='joao')
        maria = User.objects.create(first_name='Maria', username='maria')

        family = Circle.objects.create(name='Família')
        friends = Circle.objects.create(name='Amigos')

        Comment.objects.create(user=joao, comment='Uma boa pessoa', circle=family)
        Comment.objects.create(user=maria, comment='Faz coisas boas', circle=friends)

    def test_create_new_comment(self):
        c1 = Comment.objects.get(user__first_name='João')
        c2 = Comment.objects.get(user__first_name='Maria')

        #self.assertEqual(c1.__str__(), 'Uma boa pessoa')
        #self.assertEqual(c2.__str__(), 'Faz coisas boas')