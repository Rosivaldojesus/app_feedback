import tempfile
from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Profile

# Create your tests here.

class ProfileTestCase(TestCase):

    def setUp(self):
        joao = User.objects.create(first_name='João', username='joao')
        maria = User.objects.create(first_name='Maria', username='maria')
        Profile.objects.create(
            user=joao,
            photo=tempfile.NamedTemporaryFile(suffix='.jpg').name,
            bio = 'Biografia',
            birthday = '1989-11-13',
            genre = 'M',
            cell_phone = '(11)91122-3344'
        )
        
        Profile.objects.create(
            user=maria,
            photo=tempfile.NamedTemporaryFile(suffix='.jpg').name,
            bio = 'Biografia',
            birthday = '1989-11-13',
            genre = 'M',
            cell_phone = '(11)91122-3344'
        )
    
    def test_create_new_profile(self):
        p1 = Profile.objects.get(user__username='joao')
        p2 = Profile.objects.get(user__username='maria')
        self.assertEqual(p1.__str__(), 'joao')
        self.assertEqual(p2.__str__(), 'maria')
        
    

