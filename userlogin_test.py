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
