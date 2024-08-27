import pytest

from src.Expense import Expense
from src.Tracker import Tracker


@pytest.fixture
def tracker():
    data = [
        {"description": "Lunch", "amount": 20, "date": "2024-08-01", "category": ""},
        {
            "description": "Coffee",
            "amount": 5,
            "date": "2024-08-05",
            "category": "",
        },
    ]
    return Tracker(data)


def test_add_expense(tracker):
    new_expense = Expense("Dinner", 30, "2024-08-10", "")
    expense_id = tracker.add_expense(new_expense)
    assert expense_id == 3  # El nuevo ID debe ser 3 (2 existentes + 1 nuevo)
    assert len(tracker.storage_expense) == 3


def test_delete_expense(tracker):
    tracker.delete_expense(1)  # Eliminar el primer gasto
    assert len(tracker.storage_expense) == 1
    assert tracker.storage_expense[0].description == "Coffee"


def test_summary(tracker):
    assert tracker.sumary() == 25  # 20 (Lunch) + 5 (Coffee)


def test_get_all_expenses(tracker):
    expected_summary = [
        ["Lunch", 20, "2024-08-01", ""],
        ["Coffee", 5, "2024-08-05", ""],
    ]
    assert tracker.get_all_expenses() == expected_summary


def test_filter_by_month(tracker):
    filtered_expenses = tracker.filter_by_month(8)  # August
    assert len(filtered_expenses) == 2

    filtered_expenses = tracker.filter_by_month("all")
    assert len(filtered_expenses) == 2

    filtered_expenses = tracker.filter_by_month(7)  # No expenses in July
    assert len(filtered_expenses) == 0


def test_get_summary(tracker):
    # Get sumary of expenses directly using Tracker method
    assert tracker.get_summary(tracker.storage_expense) == 25


def test_to_dict(tracker):
    expected_dict = [
        {"description": "Lunch", "amount": 20, "date": "2024-08-01", "category": ""},
        {"description": "Coffee", "amount": 5, "date": "2024-08-05", "category": ""},
    ]
    assert tracker.to_dict() == expected_dict
