#!/usr/bin/env/ python3.6
from credential import Credential
from userlogin import Userlogin

def create_credential(email,Account_name,Password):
        '''
        Function to create a new credential
        '''
        new_credential = Credential(email,Aname,Password)
        return new_credential


def save_credential(Credential):
        '''
        Function to save credential
        '''
        credential.save_credential()


def find_credential(Account_name):
         '''
         Function that finds a credential by Account_name and returns the credential
         '''
         return Credential.find_by_Account_name(Account_name)


def check_existing_credential(Account_name):
        '''
        Function that check if a credential exists with that Account_name and returns a Boolean
        '''
        return Credential.credential_exist(Account_name) 


def display_credential():
        '''
        Function that returns the saved credential
        '''
        return Credential.display_credential() 


def generatepassword():
        '''
        Function that generates password
        '''
        return Credential.generatepassword(16)



#user login 
def save_userlogin(userlogin):
        '''
        Function to save userlogin
        '''
        userlogin.save_userlogin()


def find_userlogin(full_name):
         '''
         Function that finds userlogin by full_name and returns the 
         '''
         return userlogin.find_by_full_name(full_name)


def check_existing_userlogin(full_name):
        '''
        Function that check if userlogin exists with that full_name and returns a Boolean
        '''
        return Userlogin.userlogin_exist(full_name) 






def main():
    print("Welcome to credent list. What is your name?")
            user_name= input()

            print(f"Hello {user_name}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential, ex -exit the credent list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Credential")
                            print("-"*10)

                            print ("email ....")
                            email = input()

                            
                            print("A_name ...")
                            A_number = input()

                            print("Password ...")
                            Password = input()


                            save_contacts(create_contact(email,A_name,Password)) # create and save new contact.
                            print ('\n')
                            print(f"New Credential {email} {Password} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all your credentials")
                                    print('\n')

                                    for contact in display_contacts():
                                            print(f"{credential.email} {credential.Account_name} .....{credential.Password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the email you want to search for")

                            search_number = input()
                            if check_existing_credential(search_email):
                                    search_credential = find_credential(search_email)
                                    print(f"{search_credential.email} {search_credential.Account_name}")
                                    print('-' * 20)

                                    print(f"email.......{search_credential.email}")
                                    print(f"Password.......{search_credential.Password}")
                            else:
                                    print("The password is incorrect")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
   



