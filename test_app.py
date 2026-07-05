import pytest
from unittest.mock import patch, mock_open
from app import app, EXAM_TASKS_PATH

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_run_tests_missing_json(client):
    response = client.post("/run_tests", json={})
    assert response.status_code == 400
    assert response.get_json() == {"error": "No code provided"}

def test_run_tests_missing_code(client):
    response = client.post("/run_tests", json={"task": "all"})
    assert response.status_code == 400
    assert response.get_json() == {"error": "No code provided"}

@patch("app.subprocess.run")
@patch("builtins.open", new_callable=mock_open)
def test_run_tests_success(mock_file, mock_run, client):
    # Setup mock for subprocess.run
    mock_run.return_value.stdout = "Tests passed"
    mock_run.return_value.stderr = ""
    mock_run.return_value.returncode = 0

    response = client.post("/run_tests", json={"code": "print('hello')", "task": "task1"})

    assert response.status_code == 200
    assert response.get_json() == {
        "stdout": "Tests passed",
        "stderr": "",
        "returncode": 0
    }
    mock_file.assert_called_once_with(EXAM_TASKS_PATH, "w")
    mock_file().write.assert_called_once_with("print('hello')")
    mock_run.assert_called_once_with(
        ["python3", "-m", "pytest", "EXAM/test_exam_tasks.py", "-v", "-k", "task1"],
        capture_output=True,
        text=True
    )

@patch("builtins.open", side_effect=Exception("Disk full"))
def test_run_tests_file_write_exception(mock_file, client):
    response = client.post("/run_tests", json={"code": "print('hello')"})

    assert response.status_code == 500
    assert response.get_json() == {"error": "Failed to save code: Disk full"}

@patch("app.subprocess.run", side_effect=Exception("Subprocess failed"))
@patch("builtins.open", new_callable=mock_open)
def test_run_tests_subprocess_exception(mock_file, mock_run, client):
    response = client.post("/run_tests", json={"code": "print('hello')"})

    assert response.status_code == 500
    assert response.get_json() == {"error": "Failed to run tests: Subprocess failed"}
