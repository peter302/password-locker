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
    def test_user_save(self):
        '''this methods checks if the new user has been succesfuly saved in to the users list'''
        self.new_user.user_save()
        self.assertEqual(len(user.user_list),1)
class TestCredential(unittest.TestCase):
    "this test class defines twst cases for credentials class behaviours"
    def test_user_auth(self):
        '''this method will verify whether the authentication method is working succesfuly'''
        self.new_user=User('peter','kuria','0000')
        self.new_user.user_save()
        w_user=User('moses','kuria','0000')
        w_user.user_save()

        for user in User.user_list:
            if user.f_name==w_user.f_name and user.password==w_user.password:
                current_user=user.first_name
        return current_user
        self.assertEqual(current_user,Credentials.user_auth(w_user.password,w_user.f_name))
                
