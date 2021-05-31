import unittest
from user import User

class TestUser(unittest.TestCase):
    """ class that defines the blueprint to user test case"""
    def setUp(self):
        """ runs before each test case and check if the class has been instantiated correctly"""
        self.new_user = User("newUser","123456")

    def test_init(self):
        """Test to ensure object's initialized"""
        self.assertEqual(self.new_user.user_name,"newUser")
        self.assertEqual(self.new_user.password,"123456")
    
    def test_save_user(self):
        """test if a user is successfully saved"""
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        """ clears the user_list after every test """
        User.user_list = []

    def test_del_user(self):
        self.new_user.save_user()
        test_user = User("ben","12345")
        test_user.save_user()
        self.new_user.del_user()
        self.assertEqual(len(User.user_list),1)

if __name__== '__main__':
    unittest.main()
