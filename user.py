
class User:
    """class that generates a new instance of users"""
    def __init__(self, user_name, password):
        """create initial user instance"""
        self.user_name = user_name
        self.password = password

    user_list = []

    def save_user(self):
        """saves user objects into user_list"""
        User.user_list.append(self)

    def del_user(self):
        User.user_list.remove(self)