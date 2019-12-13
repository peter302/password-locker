import pyperclip
from user import User, Credentials

def create_new_user(first_name,last_name,password):
   '''function to create a new user'''
   new_user=user(first_name,last_name,password)
   return new_user
