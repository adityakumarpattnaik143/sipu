import pytest
from unittest.mock import patch, mock_open, MagicMock
from app import app
import os
import builtins

original_open = builtins.open

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_success(client):
    mock_md = "# Exam"
    mock_code = "def my_func(): pass"

    def mock_file_open(path, mode="r", *args, **kwargs):
        if "exam.md" in str(path):
            return mock_open(read_data=mock_md)(path, mode, *args, **kwargs)
        elif "exam_tasks.py" in str(path):
            return mock_open(read_data=mock_code)(path, mode, *args, **kwargs)
        return original_open(path, mode, *args, **kwargs)

    with patch('builtins.open', side_effect=mock_file_open):
        response = client.get('/')
        assert response.status_code == 200
        assert b"Code Editor" in response.data # index.html contains this
        assert b"<h1>Exam</h1>" in response.data
        assert b"def my_func(): pass" in response.data

def test_index_files_not_found(client):
    def mock_file_open_not_found(path, mode="r", *args, **kwargs):
        if "exam.md" in str(path) or "exam_tasks.py" in str(path):
            raise FileNotFoundError(f"File {path} not found")
        return original_open(path, mode, *args, **kwargs)

    with patch('builtins.open', side_effect=mock_file_open_not_found):
        response = client.get('/')
        assert response.status_code == 200
        assert b"Error: exam.md not found." in response.data
        assert b"Error: exam_tasks.py not found." in response.data

def test_run_tests_no_data(client):
    response = client.post('/run_tests', json={})
    assert response.status_code == 400
    assert response.get_json() == {"error": "No code provided"}

def test_run_tests_no_code_field(client):
    response = client.post('/run_tests', json={"task": "all"})
    assert response.status_code == 400
    assert response.get_json() == {"error": "No code provided"}

def test_run_tests_success_all_tasks(client):
    m_open = mock_open()
    def mock_file_open_write(path, mode="r", *args, **kwargs):
        if "exam_tasks.py" in str(path) and "w" in mode:
            return m_open(path, mode, *args, **kwargs)
        return original_open(path, mode, *args, **kwargs)

    with patch('builtins.open', side_effect=mock_file_open_write), \
         patch('subprocess.run') as mocked_run:

        mock_process = MagicMock()
        mock_process.stdout = "tests passed"
        mock_process.stderr = ""
        mock_process.returncode = 0
        mocked_run.return_value = mock_process

        response = client.post('/run_tests', json={"code": "print('hello')"})

        assert response.status_code == 200
        assert response.get_json() == {
            "stdout": "tests passed",
            "stderr": "",
            "returncode": 0
        }
        m_open.assert_called_once_with(os.path.join('EXAM', 'exam_tasks.py'), 'w')
        m_open().write.assert_called_once_with("print('hello')")
        mocked_run.assert_called_once_with(
            ["python3", "-m", "pytest", "EXAM/test_exam_tasks.py", "-v"],
            capture_output=True,
            text=True
        )

def test_run_tests_success_specific_task(client):
    m_open = mock_open()
    def mock_file_open_write(path, mode="r", *args, **kwargs):
        if "exam_tasks.py" in str(path) and "w" in mode:
            return m_open(path, mode, *args, **kwargs)
        return original_open(path, mode, *args, **kwargs)

    with patch('builtins.open', side_effect=mock_file_open_write), \
         patch('subprocess.run') as mocked_run:

        mock_process = MagicMock()
        mock_process.stdout = "task passed"
        mock_process.stderr = ""
        mock_process.returncode = 0
        mocked_run.return_value = mock_process

        response = client.post('/run_tests', json={"code": "pass", "task": "task_1"})

        assert response.status_code == 200
        mocked_run.assert_called_once_with(
            ["python3", "-m", "pytest", "EXAM/test_exam_tasks.py", "-v", "-k", "task_1"],
            capture_output=True,
            text=True
        )

def test_run_tests_save_fails(client):
    def mock_file_open_error(path, mode="r", *args, **kwargs):
        if "exam_tasks.py" in str(path) and "w" in mode:
            raise Exception("denied")
        return original_open(path, mode, *args, **kwargs)

    with patch('builtins.open', side_effect=mock_file_open_error):
        response = client.post('/run_tests', json={"code": "pass"})
        assert response.status_code == 500
        assert "Failed to save code: denied" in response.get_json()["error"]

def test_run_tests_subprocess_fails(client):
    m_open = mock_open()
    def mock_file_open_write(path, mode="r", *args, **kwargs):
        if "exam_tasks.py" in str(path) and "w" in mode:
            return m_open(path, mode, *args, **kwargs)
        return original_open(path, mode, *args, **kwargs)

    with patch('builtins.open', side_effect=mock_file_open_write), \
         patch('subprocess.run', side_effect=Exception("subprocess error")):
        response = client.post('/run_tests', json={"code": "pass"})
        assert response.status_code == 500
        assert "Failed to run tests: subprocess error" in response.get_json()["error"]
