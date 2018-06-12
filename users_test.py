import unittest 
from credential import Credential
from users import Users
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
        


    def test_save_users(self):
           '''
           test_save_users test case to test if the users object is saved into the users list
           '''
           

           self.new_users.save_users()
           self.assertEqual(len(Users.users_list),1)


     def test_save_multiple_users(self):
            '''
            test_save_multiple_users to check if we can save multiple users
            objects to our users_list
            '''
            self.new_users.save_users()
            test_save_multiple_users = Users("username","Email","kyre34") # new users
            test_users.save_users()
            self.assertEqual(len(Users.users_list),2)


    # setup and class creation up here
     def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Users.users_list = []

# other test cases here
     def test_save_multiple_users(self):
            '''
            test_save_multiple_users to check if we can save multiple users
            objects to our userlogin_list
            '''
            self.new_users.save_users()
            test_users = Users("username","Email","kyre34") # new user data
            test_users.save_users()
            self.assertEqual(len(Users.users_list),2)

    


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''

   
    def test_find_users_by_username(self):
        '''
        test to check if we can find a credential detail by username and display the info
        '''

        self.new_users.save_users()
        test_users= Users("Joan korir","joankorirchemutai@gmail.com","wendy65")
        test_users.save_users()

        found_users = Users.find_by_username("Joan korir")

        self.assertEqual(found_users.email,test_users.email)




    def test_users_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the userlogin.
        '''

        self.new_users.save_users()
        test_users = Users("Joan korir","joankorirchemutai@gmail.com")
        test_users.save_userlogin()

        userlogin_exists = Users.users_exist("Joan korir")

        self.assertTrue(userlogin_exists)






