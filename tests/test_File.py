import json
import os

import pytest

from src.File import File


@pytest.fixture
def temp_file(tmp_path):
    file_path = tmp_path / "test_file.json"
    return File(file_path)


def test_file_creation(temp_file):
    assert temp_file.exists()


def test_save_data(temp_file):
    data = [{"name": "John", "age": 30}]
    temp_file.save_data(data)

    with open(temp_file.name) as file:
        loaded_data = json.load(file)

    assert loaded_data == data


def test_extract_data(temp_file):
    data = [{"name": "John", "age": 30}]
    temp_file.save_data(data)

    extracted_data = temp_file.extract_data()
    assert extracted_data == data


def test_delete_file(temp_file):
    temp_file.delete()
    assert not os.path.exists(temp_file.name)


def test_delete_non_existent_file(temp_file):
    temp_file.delete()
    assert temp_file.delete() is False
