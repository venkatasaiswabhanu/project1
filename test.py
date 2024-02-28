import subprocess

def test_password_rotation():
    # Run the script and capture its output
    result = subprocess.run(['python', 'password_rotation.py'], capture_output=True, text=True)

    # Check if both expected outputs are present in the captured output
    assert "MySQL password changed successfully." in result.stdout
    assert "Successfully able to login with new password." in result.stdout
