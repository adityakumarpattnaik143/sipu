import pytest
from unittest.mock import patch, mock_open
import os
import sys

# Add EXAM to path so we can import exam_web
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from exam_web import parse_exam_tasks

def test_parse_exam_tasks_file_not_found():
    with patch('exam_web.os.path.exists', return_value=False):
        tasks = parse_exam_tasks()
        assert tasks == []

def test_parse_exam_tasks_empty_file():
    with patch('exam_web.os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data="")):
            tasks = parse_exam_tasks()
            assert tasks == []

def test_parse_exam_tasks_valid_functions():
    mock_data = """def task1():
    pass

def task2(arg1):
    return arg1
"""
    with patch('exam_web.os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data=mock_data)):
            tasks = parse_exam_tasks()
            assert len(tasks) == 2

            assert tasks[0]["title"] == "Task 1: task1"
            assert tasks[0]["func_name"] == "task1"
            assert tasks[0]["code"] == "def task1():\n    pass"

            assert tasks[1]["title"] == "Task 2: task2"
            assert tasks[1]["func_name"] == "task2"
            assert tasks[1]["code"] == "def task2(arg1):\n    return arg1"

def test_parse_exam_tasks_malformed_functions():
    mock_data = """def ():
    pass

def valid_task():
    pass

def
"""
    with patch('exam_web.os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data=mock_data)):
            tasks = parse_exam_tasks()
            assert len(tasks) == 1

            assert tasks[0]["title"] == "Task 1: valid_task"
            assert tasks[0]["func_name"] == "valid_task"
            assert tasks[0]["code"] == "def valid_task():\n    pass"
