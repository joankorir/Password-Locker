import unittest
from credential import Credential
import pyperclip

class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the Credential class behaviours.

    Args:
         unittest.TestCase: TestCase class that helps in creating test cases
    '''

   def setUp(self):
                 '''
                 Set up method to run before each test cases.
                 '''
                 self.new_credential = Credential("joankorirchemutai@gmail.com","Instagram","joan1234")
                 # created account object


    def test__init(self):
                '''
                test__init test if the object is initialized properly
                '''

                self.assertEqual(self.new_credential.email,"joankorirchemutai@gmail.com",)
                self.assertEqual(self.new_credential.Account_name,"Instagram")
                self.assertEqual(self.new_credential.Password,"joan1234")



   def test_save_credential(self):
                   '''
                   test_save_credential test case to test if the credential object is saved into the credent list
                   '''

                   self.new_credential.save_credential()
                   self.assertEqual(len(Credential.credent_list),1)


   def test_save_multiple_credential(self):
                    '''
                    test_save_multiple_credential to check if we can save multiple credential
                    objects to our credent_list
                    '''
                    self.new_credential.save_credential()
                    test_credential = Credential("joankorir44@gmail.com","Facebook","kyler@23") # new credential
                    test_credential.save_credential()
                    self.assertEqual(len(Credential.credent_list),2)


            # setup and class creation up here
   def tearDown(self):
                    '''
                    tearDown method that does clean up after each test case has run.
                    '''
                    Credential.credent_list = []

        # other test cases here
   def test_save_multiple_credentia(self):
                    '''
                    test_save_multiple_credential to check if we can save multiple credential
                    objects to our credent_list
                    '''
                    self.new_credential.save_credential()
                    test_credential = Credential("joankorir44@gmail.com","Facebook","kyler@23") # new credential
                    test_credential.save_credential()
                    self.assertEqual(len(Credential.credent_list),2)




        def test_find_credential_by_Account_name(self):
                '''
                test to check if we can find a credential by Account_name and display information
                '''

                self.new_credential.save_credential()
                test_credential = Credential("joankorir44@gmail.com","Facebook","kyler@23")
                test_credential.save_credential()

                found_credential = Credential.find_by_Account_name("Facebook")

                self.assertEqual(found_credential.Account_name,test_credential.Account_name)

        def test_credential_exists(self):
                '''
                test to check if we can return a Boolean  if we cannot find the credential.
                '''

                self.new_credential.save_credential()
                test_credential = Credential("joankorir44@gmail.com","Facebook","kyler@23")
                test_credential.save_credential()

                credential_exists = Credential.credential_exist("Facebook")

                self.assertTrue(credential_exists)


        def test_display_credential(self):
                 '''
                 method that returns credential saved
                 '''

                 self.assertEqual(Credential.display_credentials(),Credential.credent_list)


        def test_copy_Password(self):
                '''
                Test to confirm that we are copying the Password from a found credential
                '''

                self.new_credential.save_credential()
                Credential.copy_Password("joan 1234")

                self.assertEqual(self.new_credential.Password,pyperclip.paste())


if __name__ =='__main__':
    unittest.main()
