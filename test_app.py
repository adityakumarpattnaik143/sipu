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
from app import app
import builtins
import os

@pytest.fixture
def client(monkeypatch, tmp_path):
    # Set a temporary path for exam tasks so we do not overwrite the real one
    tmp_exam_tasks = tmp_path / "exam_tasks.py"
    monkeypatch.setattr('app.EXAM_TASKS_PATH', str(tmp_exam_tasks))

    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_run_tests_missing_payload(client):
    """Test missing JSON payload completely"""
    response = client.post('/run_tests')
    assert response.status_code == 415

def test_run_tests_empty_json(client):
    """Test empty JSON payload"""
    response = client.post('/run_tests', json={})
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
    """Test JSON payload missing 'code' key"""
    response = client.post('/run_tests', json={"task": "task1"})
    assert response.status_code == 400
    assert response.get_json() == {"error": "No code provided"}

def test_run_tests_success_all_tasks(client):
    """Test successful execution of all tasks"""
    response = client.post('/run_tests', json={"code": "def hello(): pass"})
    assert response.status_code == 200
    data = response.get_json()
    assert "stdout" in data
    assert "stderr" in data
    assert "returncode" in data

def test_run_tests_success_specific_task(client):
    """Test successful execution of a specific task"""
    response = client.post('/run_tests', json={"code": "def hello(): pass", "task": "task1"})
    assert response.status_code == 200
    data = response.get_json()
    assert "stdout" in data
    assert "stderr" in data
    assert "returncode" in data

def test_run_tests_save_failure(client, monkeypatch):
    """Test failure when saving code to file"""
    monkeypatch.setattr('app.EXAM_TASKS_PATH', '/invalid_dir_that_does_not_exist/exam_tasks.py')
    response = client.post('/run_tests', json={"code": "def hello(): pass"})
    assert response.status_code == 500
    assert "Failed to save code" in response.get_json()["error"]

def test_run_tests_subprocess_failure(client, monkeypatch):
    """Test failure when subprocess fails to run tests"""
    def mock_run(*args, **kwargs):
        raise Exception("Mock subprocess error")
    monkeypatch.setattr('app.subprocess.run', mock_run)

    response = client.post('/run_tests', json={"code": "def hello(): pass"})
    assert response.status_code == 500
    assert "Failed to run tests: Mock subprocess error" in response.get_json()["error"]
