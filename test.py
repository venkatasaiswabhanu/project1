import unittest
import mysql.connector
import os

class TestMySQLPasswordChange(unittest.TestCase):

    def read_password(self, file_path):
        with open(file_path, 'r') as file:
            return file.readline().strip()

    def test_mysql_login(self):
        try:
            
            # Read the password from pwd.txt
            old_password_file = "pwd.txt"
            old_password = self.read_password(old_password_file)

            # Attempt MySQL connection using the password from pwd.txt
            connection = mysql.connector.connect(host='localhost',
                                                 user='root',
                                                 password=old_password)
            connection.close()
            # If the connection is successful, the test passes
            self.assertTrue(True)
        except mysql.connector.Error as error:
            # If there's an error connecting, the test fails
            self.fail(f"Failed to connect to MySQL: {error}")

if __name__ == '__main__':
    unittest.main()
