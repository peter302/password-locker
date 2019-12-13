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

             
