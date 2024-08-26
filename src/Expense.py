from datetime import datetime


class Expense:

    def __init__(self, description, amount, date: str):
        self.description = description
        self.amount = amount
        self.date = date
        pass

    def update(self, new_description, new_amount, date):
        self.description = new_description
        self.amount = new_amount
        self.date = date

    def get_amount(self):
        return self.amount

    # No usado
    def to_string(self):
        return self.description + str(self.amount) + self.date

    def to_list(self):
        list = []

        list.append(self.description)
        list.append(self.amount)
        list.append(self.date)
        return list

    def to_dict(self) -> dict:
        return {
            "description": self.description,
            "amount": self.amount,
            "date": self.date,
        }

    def get_month(self) -> int:
        return datetime.strptime(self.date, "%Y-%m-%d").date().month
