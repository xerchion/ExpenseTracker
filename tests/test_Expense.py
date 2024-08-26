from datetime import datetime

import pytest

from src.Expense import Expense


@pytest.fixture
def expense():
    return Expense("Dinner", 50, "2024-08-24")


def test_initialization(expense):
    assert expense.description == "Dinner"
    assert expense.amount == 50
    assert expense.date == "2024-08-24"


def test_update(expense):
    expense.update("Lunch", 30, "2024-08-25")
    assert expense.description == "Lunch"
    assert expense.amount == 30
    assert expense.date == "2024-08-25"


def test_get_amount(expense):
    assert expense.get_amount() == 50


def test_to_list(expense):
    expected_list = ["Dinner", 50, "2024-08-24"]
    assert expense.to_list() == expected_list


def test_to_dict(expense):
    expected_dict = {"description": "Dinner", "amount": 50, "date": "2024-08-24"}
    assert expense.to_dict() == expected_dict


def test_get_month(expense):
    assert expense.get_month() == 8
