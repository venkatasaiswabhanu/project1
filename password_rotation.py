import subprocess
import string
import random
import mysql.connector

# Function to generate a new random password
def generate_password(length=20):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Function to read old password from file
def read_old_password(file_path):
    with open(file_path, 'r') as file:
        return file.readline().strip()

# Function to write new password to file
def write_new_password(file_path, new_password):
    with open(file_path, 'w') as file:
        file.write(new_password)

def check_mysql_connection(password):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password=password)
        connection.close()
        return True
    except mysql.connector.Error as error:
        print("Failed to connect to MySQL: {}".format(error))
        return False

def change_mysql_password(old_password_file):
    # Read old password from file
    old_password = read_old_password(old_password_file)

    # Generate a new password
    new_password = generate_password()

    # Change MySQL password
    command = ['mysql', '-u', 'root', '-p' + old_password, '-e', f"ALTER USER 'root'@'localhost' IDENTIFIED BY '{new_password}';"]
    subprocess.run(command, check=True)

    # Write new password to the same file
    write_new_password(old_password_file, new_password)

    print("MySQL password changed successfully.")
    print(f"New password: {new_password}")

    # Check if connection can be established with the new password
    if check_mysql_connection(new_password):
        print("Successfully able to login with new password.")
    else:
        print("Something went wrong.")

# Get path to old password file from user input
old_password_file = "pwd.txt"
change_mysql_password(old_password_file)
