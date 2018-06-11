class Userlogin:
    """
    Class that generates new instances of userlogin.
    """

    userlogin_list = [] #empty 
    
    def __init__(self,full_name,Email):


        self.full_name = full_name
        self.Email = Email


     def save_userlogin(self):

        '''
        save_account method saves userlogin objects into userlogin_list
        '''

    @classmethod
    def find_by_full_name(cls,full_name):
        '''
        Method that takes in an full_name and returns a userlogin that matches that full_name.

        Args:
            ful_name: full_name to search for
        Returns :
            userlogin that matches the full_name.
        '''

        for userlogin in cls.userlogin_list:
            if userlogin.full_name == full_name:
                return full_name

 