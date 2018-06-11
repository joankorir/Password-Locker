import unittest 
from userlogin import Userlogin
# import pyperclip

class TestUserlogin(unittest.TestCase):

    '''
    Test class that defines test cases for the Userlogin class behaviours.

    Args:
         unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
         '''
         Set up method to run before each test cases.
         '''
         self.new_userlogin = Userlogin("joan korir","joankorirchemutai@gmail.com")
         # created account object
    
    
    def test__init(self):
        '''
        test__init test if the object is initialized properly
        '''
        self.assertEqual(self.new_userlogin.full_name,"Joan korir")
        self.assertEqual(self.new_userlogin.Email,"joankorirchemutai@gmail.com",)
        


    def test_save_userlogin(self):
           '''
           test_save_userlogin test case to test if the userlogin object is saved into the userlogin list
           '''

           self.new_userlogin.save_userlogin()
           self.assertEqual(len(Userlogin.userlogin_list),1)


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''

   
    def test_find_userlogin_by_full_name(self):
        '''
        test to check if we can find a by  that
        '''

        self.new_userlogin.save_userlogin()
        test_userlogin = Userlogin("Joan korir","joankorirchemutai@gmail.com")
        test_userlogin.save_userlogin()

        found_userlogin = Userlogin.find_by_full_name("Joan korir")

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






