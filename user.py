import pyperclip,string,random
class User:
     user_list=[] #a list to hold user details
     def __init__(self,f_name,l_name,password):
         "a method acting as constructor to initalize instances of a class"
         self.f_name=f_name
         self.l_name=l_name
         self.password=password
     def user_save(self):
        "a method to save a new user object when ceated"
        User.user_list.append(self)
class Credentials:
        "this class will hold users details including names and passwords for user's site plus funtions and method to alter those dtails"

        Credentials_list=[]
        user_credentials_list=[]
        @classmethod
        def user_auth(cls,f_name,password):
            '''this method will authenticate user'''
            loged_user=''
            for user in User.user_list:
                if(user.f_name==f_name and user.password==password):
                    loded_user=user.f_name
                    return loged_user

        def __init__(self,user_name,web_site,account_name,password):
             "this method initializes our credentials class with the propertis for user credentials"
             self.user_name=user_name
             self.web_site=web_site
             self.account_name=account_name
             self.password=password

        def save_credentials(self):
            "this method will save a newly user created credentials"
            Credentials.Credentials_list.append(self)
        def pass_gen(pass_size=6,char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
            "this function will generate a password if user chooses automatic pass word generation"
            pass_choice=''.join(random.choice(char) for _ in range(pass_size))
            return pass_choice

        @classmethod

        def show_credentials(cls,user_name):
            "this method will show all credentials stored for the loged user"
            for j in cls.user_credetials_list:
                if  j.user_name==user_name:
                    user_credetials_list.append(j)

            return user_credetials_list

        @classmethod
        def search_site_name(cls,web_site):
            "this method will search a web_site by name"
            for k in cls.Credentials_list:
                if k.web_site==web_site:
                    return k

        def copy_site(cls,web_site):
            "class methods to copy a site name to our clip board"
            copy_credentials=Credentials.search_site_name(web_site)
            return pyperclip.copy(copy_credentials.password)
