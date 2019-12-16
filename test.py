import unittest
import pyperclip
from user import User,Credentials

class TestUser(unittest.TestCase):
    '''this class tests methods for user'''

    def setUp(self):
        '''this method runs before each test case'''

        self.new_user=User("peter","kuria","0000")
    def test_init_(self):
        "to test the initialization of the new user is correctly done"
        self.assertEqual(self.new_user.f_name,'peter')
        self.assertEqual(self.new_user.l_name,'kuria')
        self.assertEqual(self.new_user.password,'0000')
