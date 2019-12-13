import pyperclip
from user import User, Credentials

def create_new_user(first_name,last_name,password):
   '''function to create a new user'''
   new_user=user(first_name,last_name,password)
   return new_user
 def save_user(user):
     '''a function to save a newly created user'''
     User.user_save(user)
  def authenticate_user(f_name,password):
      '''function to authenticate user before account login'''
      qualify_user=Credentials.user_auth(f_name,password)
    return qualify_user
def password_generation():
    '''a function to generate new password automatically"

    new_pass=Credentials.pass_gen()
    return new_pass

def new_credentials(user_name,web_site,account_name,password):
    new_credential=Credentials(user_name,web_site,account_name,password)
    return new_credential    
