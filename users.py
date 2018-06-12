class Userlogin:
    """
    Class that generates new instances of userlogin.
    """

    userlogin_list = [] #empty 
    
    def __init__(self,username,Email,password):


        self.username = username
        self.Email = Email
        self.password = password


     def save_userlogin(self):

        '''
        save_account method saves userlogin objects into userlogin_list
        '''



    

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in an full_name and returns a userlogin that matches that full_name.

        Args:
            username: username to search for
        Returns :
            userlogin that matches the username.
        '''

        for userlogin in cls.userlogin_list:
            if userlogin.username == username:
                return username



     @classmethod
    def userlogin_exist(cls,name):
        '''
        Method that checks if userlogin exists from the userlogin list.
        Args:
            name: full_name to search if it exists
        Returns :
            Boolean: True or false depending if the userlogin exists
        '''
        for userlogin in cls.userlogin_list:
            if userlogin.username == name:
                    return True

        return False            

 