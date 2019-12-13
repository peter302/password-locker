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
        user_credetials_list=[]
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
