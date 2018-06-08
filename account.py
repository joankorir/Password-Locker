class  Account:
    """
    Class that generates new instances of accounts
    """
  
    account_list = [] #Empty

    def __init__(self,email,Account_name,Password):      
   
        self.email = email
        self.Account_name = Account_name
        self.Password = Password
        
    def save_account(self):

        '''
        save_account method saves account objects into account_list
        '''

        Account.account_list.append(self)

        
    