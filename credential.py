import pyperclip
import string
import random
class  Credential:
    """
    Class that generates new instances of credentials
    """

     credent_list = [] #Empty

        def __init__(self,email,Account_name,Password):


            self.email = email
            self.Account_name = Account_name
            self.Password = Password


        def save_credential(self):

            '''
            save_account method saves credential objects into credent_list
            '''

        @classmethod
        def find_by_Account_name(cls,Account_name):
            '''
            Method that takes in an Account_name and returns a credential that matches that Account_name.

            Args:
                Account_name: Account_name to search for
            Returns :
                Credential that matches the Account_name.
            '''

            for credential in cls.credent_list:
                if credential.Account_name == Account_name:
                    return Account_name

        @classmethod
        def credential_exist(cls,name):
             '''
             Method that checks if a credential exists from credent List.
             Args:
               name : Account_name to search if it exists
             Returns:
               Boolean: True or false depending if the credential exists
             '''
             for credential in cls.credent_list:
                 if credential.Account_name == name :
                     return True
             return False


        @classmethod
        def display_credential(cls):
              '''
              method that returns the credent list
              '''
              return cls.credent_List

        @classmethod
        def generatePassword(num):
            password = ''

                  for n in range(num):
             x = random.randint(0,94)
            password += string.printable[x]

            return password



        @classmethod
        def copy_email(cls,Password):
            credential_found = Credential.find_by_Account_name(Account_name)
            pyperclip.copy(credential_found.Password)
