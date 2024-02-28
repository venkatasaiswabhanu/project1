import unittest
import password_rotation

class TestPasswordRotation(unittest.TestCase):

    def test_password_rotation_success(self):
        # Path to old password file
        old_password_file = "pwd.txt"
        
        # Call the function
        result = password_rotation.change_mysql_password(old_password_file)
        
        # Assert that the result is "Success"
        self.assertEqual(result, "Success")

if __name__ == '__main__':
    unittest.main()
