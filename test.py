import subprocess
import pytest
from pathlib import Path
from app import change_mysql_password


@pytest.fixture
def old_password_file(tmp_path):
    # Create a temporary file for the old password
    file_path = tmp_path / "pwd.txt"
    with open(file_path, "w") as f:
        f.write("old_password")
    return file_path


def test_change_mysql_password_success(old_password_file, monkeypatch):
    # Mocking subprocess.run to prevent actual password change
    def mock_subprocess_run(command, check, stderr):
        # Simulate successful password change
        return None

    # Mocking check_mysql_connection to simulate successful connection
    def mock_check_mysql_connection(password):
        return True

    # Apply monkeypatching
    monkeypatch.setattr("subprocess.run", mock_subprocess_run)
    monkeypatch.setattr("app.check_mysql_connection", mock_check_mysql_connection)

    result = change_mysql_password(old_password_file)
    assert result == "Success"


def test_change_mysql_password_failure(old_password_file, monkeypatch):
    # Mocking subprocess.run to prevent actual password change
    def mock_subprocess_run(command, check, stderr):
        # Simulate failed password change
        raise subprocess.CalledProcessError(returncode=1, cmd=command)

    # Mocking check_mysql_connection to simulate unsuccessful connection
    def mock_check_mysql_connection(password):
        return False

    # Apply monkeypatching
    monkeypatch.setattr("subprocess.run", mock_subprocess_run)
    monkeypatch.setattr("app.check_mysql_connection", mock_check_mysql_connection)

    result = change_mysql_password(old_password_file)
    assert result == "Failed"
