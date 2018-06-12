import unittest 
from credential import Credential
from uses import Users
import pyperclip

class TestUsers(unittest.TestCase):

    '''
    Test class that defines test cases for the Users class behaviours.

    Args:
         unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
         '''
         Set up method to run before each test cases.
         '''
         self.new_users = Users("joan korir","joankorirchemutai@gmail.com","wendy65")
         # created users object
    
    
    def test__init(self):
        '''
        test__init test if the object is initialized properly
        '''
        self.assertEqual(self.new_users.username,"Joan korir")
        self.assertEqual(self.new_users.Email,"joankorirchemutai@gmail.com",)
        self.assertEqual(self,new_users.password,"wendy65")
        


    def test_save_userlogin(self):
           '''
           test_save_userlogin test case to test if the userlogin object is saved into the userlogin list
           '''

           self.new_userlogin.save_userlogin()
           self.assertEqual(len(Userlogin.userlogin_list),1)


    def test_save_multiple_userlogin(self):
            '''
            test_save_multiple_userlogin to check if we can save multiple userlogin
            objects to our userlogin_list
            '''
            self.new_userlogin.save_userlogin()
            test_userlogin = Userlogin("user","") # new userlogin
            test_userlogin.save_userlogin()
            self.assertEqual(len(Userlogin.userlogin_list),2)


    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Userlogin.userlogin_list = []

# other test cases here
    def test_save_multiple_userlogin(self):
            '''
            test_save_multiple_userlogin to check if we can save multiple userlogin
            objects to our userlogin_list
            '''
            self.new_userlogin.save_userlogin()
            test_userlogin = Userlogin("joankorir44@gmail.com","Facebook","kyler@23") # new credential
            test_userlogin.save_userlogin()
            self.assertEqual(len(Userlogin.userlogin_list),2)

    


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''

   
    def test_find_userlogin_by_username(self):
        '''
        test to check if we can find a by  that
        '''

        self.new_userlogin.save_userlogin()
        test_userlogin = Userlogin("Joan korir","joankorirchemutai@gmail.com","wendy65")
        test_userlogin.save_userlogin()

        found_userlogin = Userlogin.find_by_username("Joan korir")

        self.assertEqual(found_userlogin.email,test_userlogin.email)




    def test_userlogin_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the userlogin.
        '''

        self.new_userlogin.save_userlogin()
        test_userlogin = Userlogin("Joan korir","joankorirchemutai@gmail.com")
        test_userlogin.save_userlogin()

        userlogin_exists = Userlogin.userlogin_exist("Joan korir")

        self.assertTrue(userlogin_exists)






