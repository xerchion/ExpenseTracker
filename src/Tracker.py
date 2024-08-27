from .Expense import Expense


class Tracker:
    def __init__(self, data):
        self.storage_expense = []

        self.to_object_expenses(data)

    def add_expense(self, expense: Expense) -> int:
        # Add expense and return his id

        self.storage_expense.append(expense)
        # returns pos + 1, position [0] is id=1 for user
        return len(self.storage_expense)

    def delete_expense(self, id):
        del self.storage_expense[id - 1]

    def sumary(self):
        return sum(expense.get_amount() for expense in self.storage_expense)

    def get_all_expenses(self):
        sumary = []
        for expense in self.storage_expense:
            sumary.append(expense.to_list())
        return sumary

    def filter_by_month(self, month):
        if month == "all":
            return self.storage_expense
        filtered = []
        for expense in self.storage_expense:
            if month == expense.get_month():
                filtered.append(expense)
        return filtered

    def filter_by_category(self, category):
        filtered = []
        for expense in self.storage_expense:
            if category == expense.get_category():
                filtered.append(expense.to_list())
        return filtered if filtered else None

    def get_summary(self, data):
        total = 0
        for expense in data:
            total = total + expense.get_amount()
        return total

    def to_dict(self):
        data = []
        for element in self.storage_expense:
            data.append(element.to_dict())
        return data

    def to_object_expenses(self, data):
        for element in data:
            self.storage_expense.append(
                Expense(
                    element["description"],
                    element["amount"],
                    element["date"],
                    element["category"],
                )
            )

    def get_size(self):
        return len(self.storage_expense)
