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
    def credential_exist(cls,number):
         '''
         Method that checks if a credential exists from credent List.
         Args:
           number : Account_name to search if it exists
         Returns:
           Boolean: True or false depending if the credential exists
         '''
         for credential in cls.credent_list:
             if credential.Account_name == name :
                 return True
         return False    

        
    