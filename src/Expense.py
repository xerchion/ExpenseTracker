from datetime import datetime


# todo añadiendo  category
class Expense:

    def __init__(self, description, amount, date: str, category: str):
        self.description = description
        self.amount = amount
        self.date = date
        self.category = category
        pass

    def to_list(self):
        list = []
        list.append(self.description)
        list.append(self.amount)
        list.append(self.date)
        list.append(self.category)
        return list

    def to_dict(self) -> dict:
        return {
            "description": self.description,
            "amount": self.amount,
            "date": self.date,
            "category": self.category,
        }

    def get_month(self) -> int:
        return datetime.strptime(self.date, "%Y-%m-%d").date().month

    def get_amount(self):
        return self.amount

    def get_category(self):
        return self.category

    def set_category(self, category):
        self.category = category

    def set_amount(self, amount):
        self.amount = amount

    def set_description(self, description):
        self.description = description
