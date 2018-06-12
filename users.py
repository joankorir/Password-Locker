class Users:
    """
    Class that generates new instances of users.
    """

    users_list = [] #empty 
    
    def __init__(self,username,Email,password):


        self.username = username
        self.Email = Email
        self.password = password


     def save_users(self):

        '''
        save_account method saves users objects into users_list
        '''



    

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in an username and returns a users that matches that username.

        Args:
            username: username to search for
        Returns :
            users that matches the username.
        '''

        for users in cls.users_list:
            if users.username == username:
                return username



     @classmethod
    def users_exist(cls,name):
        '''
        Method that checks if userlogin exists from the users list.
        Args:
            name: full_name to search if it exists
        Returns :
            Boolean: True or false depending if the users exists
        '''
        for users in cls.users_list:
            if users.username == name:
                    return True

        return False            

 