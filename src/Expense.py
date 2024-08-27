from datetime import datetime


# todo añadiendo  category
class Expense:

    def __init__(self, description, amount, date: str, category: str):
        self.description = description
        self.amount = amount
        self.date = date
        self.category = category
        pass

    def update(self, new_description, new_amount, date, new_category):
        self.description = new_description
        self.amount = new_amount
        self.date = date
        self.category = new_category

    # No usado TODO borrar si no sirve
    def to_string(self):
        return self.description + str(self.amount) + self.date

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
