import subprocess

def test_password_rotation():
    # Run the script and capture its output
    result = subprocess.run(['python', 'password_rotation.py'], capture_output=True, text=True)

    # Check if the script execution was successful
    assert result.returncode == 0, f"Script execution failed with return code {result.returncode}.\nstderr: {result.stderr}"

    # Check if the script output contains success or failure messages
    assert "MySQL password changed successfully." in result.stdout or "Failed to change MySQL password:" in result.stdout
    if "MySQL password changed successfully." in result.stdout:
        assert "Successfully able to login with new password." in result.stdout
    elif "Failed to change MySQL password:" in result.stdout:
        assert "Something went wrong." in result.stdout
