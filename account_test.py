import unittest 
from account import Account 

class TestAccount(unittest.TestCase):

    '''
    Test class that defines test cases for the Account class behaviours.

    Args:
         unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
         '''
         Set up method to run before each test cases.
         '''
         self.new_account = Account("joankorirchemutai@gmail.com","Instagram","joan1234")
         # created account object
    
    
    def test__init(self):
        '''
        test__init test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.email,"joankorirchemutai@gmail.com",)
        self.assertEqual(self.new_account.Account_name,"Instagram")
        self.assertEqual(self.new_account.Password,"joan1234")



    def test_save_account(self):
           '''
           test_save_account test case to test if the account object is saved into the account list
           '''

           self.new_account.save_account()
           self.assertEqual(len(Account.account_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.account_list = []

    def test_delete_account(self):
            '''
            test_delete_account to test if we can delete an account  
   


if __name__ =='__main__':
    unittest.main()