import os
import pytest
from password_rotation import change_mysql_password, read_old_password


@pytest.fixture
def old_password_file(tmp_path):
    # Create a temporary file
    file_path = tmp_path / "pwd.txt"
    # Write a sample old password to the temporary file
    with open(file_path, 'w') as file:
        file.write("old_password123")
    return file_path


def test_change_mysql_password(old_password_file):
    # Change the MySQL password using the script
    result = change_mysql_password(old_password_file)
    
    # Check if the password change was successful
    assert result == "Success"
    
    # Check if the old password file has been updated
    new_password = read_old_password(old_password_file)
    assert len(new_password) == 20  # New password length should be 20 characters
    assert result == new_password


def test_change_mysql_password_failure(old_password_file):
    # Modify the MySQL configuration to use a non-existent password
    os.environ['MYSQL_PWD'] = "wrong_password"
    # Attempt to change the MySQL password using the script
    result = change_mysql_password(old_password_file)
    
    # Check if the password change failed
    assert result == "Failed"
