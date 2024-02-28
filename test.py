import unittest
import mysql.connector
import os
import subprocess

class TestMySQLPasswordChange(unittest.TestCase):

    def read_password(self, file_path):
        with open(file_path, 'r') as file:
            return file.readline().strip()

    def start_mysql_server(self):
        try:
            # Attempt to connect to MySQL server
            connection = mysql.connector.connect(host='localhost',
                                                 user='root',
                                                 password='',
                                                 database='',
                                                 port=3306)
            connection.close()
        except mysql.connector.Error as error:
            # MySQL server is not running, start it
            if 'Connection refused' in str(error):
                print("MySQL server is not running. Starting MySQL server...")
                subprocess.run(['sudo', 'mysql.server', 'start'], check=True)
                print("MySQL server started successfully.")
            else:
                print("Failed to connect to MySQL:", error)

    def test_mysql_login(self):
        # Start MySQL server if not already running
        self.start_mysql_server()

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
