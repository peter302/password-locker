import pyperclip
from user import User, Credentials

def create_new_user(first_name,last_name,password):
   '''function to create a new user'''
   new_user=User(first_name,last_name,password)
   return new_user
def save_user(user):
     '''a function to save a newly created user'''
     User.user_save(user)
def authenticate_user(f_name,password):
      '''function to authenticate user before account login'''
      qualify_user=Credentials.user_auth(f_name,password)
      return qualify_user
def password_generation():
    '''a function to generate new password automatically'''

    new_pass=Credentials.pass_gen()
    return new_pass

def new_credentials(user_name,web_site,account_name,password):
    new_credential=Credentials(user_name,web_site,account_name,password)
    return new_credential

def save_new_credentials(credential):
    "' a function to save a new credential'"
    Credentials.save_credentials(credential)

def display_credentials(user_name):
    "'a function to display a newly created credentials'"
    Credentials.show_credentials(user_name)

def credential_copy(web_site):
    "function to copy new credentials to clipboard"
    return Credentials.copy_site(web_site)

def main():
    print(' ')
    print('welcome to pass word locker app')

    while True:
        print(' ')
        print("-"*70)

        print('use the following options to choose the action you want to perform:\n new-create a new acount\n log-Log in\n ex-Exit')
        code=input('Enter an option:').lower().strip()

        if code=='ex':
            break
        elif code=='new':
            print("-"*60)
            print(' ')
            print('new account creation:')
            f_name=input('Enter your first name -').strip()
            l_name=input('Enter your last name -').strip()
            password=input('Enter your password -').strip()
            save_user(create_new_user(f_name,l_name,password))
            print(" ")
            print(f'your acount details:First name:{f_name},last name: {l_name},password:{password}')

        elif code=='log':
            print("_"*70)
            print(' ')

            print('please log in here: ')

            user_name=input('Enter your First name -').strip()
            password=str(input('inpput password -'))
            user_exist=authenticate_user(user_name,password)
            if user_exist==user_name:

                print(" ")

                print(f'Hello {user_name}.choose an option to go next:')

                print(' ')
            while True:
                     print("-"*60)

                     print('Navigate codes:\n launch-create a credetial\n disp-to display credentials\n cop-copy credentials\n ex-exit')
                     code=input('Enter your choice:').lower().strip()
                     print("-"*60)
                     if code=='ex':

                          print(" ")
                          print(f"goodbye {user_name}")
                     elif code=='launch':
                          print(' ')
                          print('Enter your credentials:')
                          web_site=input('Enter your website\'s name-').strip()
                          account_name=input('Enter your account_name here:').strip()
                          while True:
                              print(" ")
                              print("-"*60)
                              print("please chose an option for entering password:\n ep-existing password\n gp-generate new password\n ex-exit")
                              password_choice=input('Enter an option:').lower().strip()
                              print("-"*60)
                              if password_choice=='ep':
                                 print(" ")
                                 password=input('Enter your password').strip()
                                 break
                              elif password_choice=='gp':
                                 password=password_generation()
                                 break
                              elif password_choice=='ex':
                                  break
                              else :
                                 print('oops!wrong option entered.Try again')
                           save_new_credentials(new_credentials(user_name,web_site,account_name,password))
                           print(' ')
                           print(f'Credential Credential: web_site: {web_site} -Account Name:{account_name}-password:{password})
                           print(' ')
                    elif code== 'disp':
                        print(' ')
                        if show_credentials(user_name):
                            print('here is a list of credentials')
                            print(' ')
                            for cre in show_credentials(user_name):
                                print(f'web_site Name:{cre.web_site} -Account Name:{cre.account_name}-password:{cre.password})
                                print (' ')
                    else:
                        print('')
                        print("you don't seem to have any credential saved yet")
                        print(' ')

          elif code=='copy':
              print(' ')
              name_site=input('enter the web_site for credential you woul like to copy')
              credential_copy(name_site)
              print(' ')
          else:
              print('incorrect option.Please try again')
     else:
         print(' ')
         print('wrong details.try again or create a new account')
else:
    print("-"*60)
    print(' ')
    print('wrong option.try again')


if __name__ == '__main__':
	      main()
