import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):

    """
    class that defines test cases
    """
    def setUp(self):
        """
        initializing an instance of credentials
        """
        self.new_credentials = Credentials("Instagram","45678")

    def test_credentials_instance(self):
        """Method testing whether the new_credentials have been correctly instantiated """
        self.assertEqual(self.new_credentials.account_name,"Instagram")
        self.assertEqual(self.new_credentials.account_pass,"45678")

    def test_save_credentials(self):
        """tests whether the new credential created is saved"""
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    
    def test_save_multiple_credentials(self):
        """saves multiple credentials to credentials_list"""
        self.new_credentials.save_credentials()
        new_test_credential = Credentials("Twitter","1234")
        new_test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def tearDown(self):
        """ clears the credentials_list after every test"""
        Credentials.credentials_list = []
    
    def test_del_credentials(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Gmail","12345")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    
    def test_find_credentials_by_name(self):
        """check if it can find credentials and display its info"""
        self.new_credentials.save_credentials()
        new_test_credentials = Credentials("Twitter","1234")
        new_test_credentials.save_credentials()
        found_credential = Credentials.find_by_name("Twitter")
        self.assertEqual(found_credential.account_name,new_test_credentials.account_name)

    def test_display_credentials(self):
        """ test if all contacts can be displayed"""
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == "__main__":
    unittest.main()

    

