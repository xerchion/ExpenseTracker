from .Expense import Expense


class Tracker:
    def __init__(self, data):
        self.storage_expense = []
        self.budgets = {}
        self.extract_data(data)
        self.err_msg = []

    def add_expense(self, expense: Expense) -> int:
        # Add expense and return his id
        self.storage_expense.append(expense)
        # returns pos + 1, position [0] is id=1 for user
        return len(self.storage_expense)

    def update_expense(self, id: int, expense: Expense) -> int:
        # comprobar id válido
        # HACK el nombre de size no esta logrado, cambialo, es el size del storage
        if id < 1 or id > self.size():
            self.err_msg = "El id no corresponde con ningun gasto"
            return False, self.err_msg
        # comprobar si todos los campos están vacios
        if not expense.category and not expense.amount and not expense.description:
            self.err_msg = "Debe ingresar alguna caracteristica a modificar"
            return False, self.err_msg
        # buscar el gasto
        old_expense = self.storage_expense[id - 1]
        if expense.category:
            old_expense.set_category(expense.category)
        if expense.amount:
            old_expense.set_amount(expense.amount)
        if expense.description:
            old_expense.set_description(expense.description)
        self.storage_expense[id - 1] = old_expense
        return True, None

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
            if int(month) == expense.get_month():

                filtered.append(expense)
        return filtered

    def filter_by_category(self, category):
        filtered = []
        for expense in self.storage_expense:
            if category == expense.get_category():
                filtered.append(expense.to_list())
        return filtered

    def get_summary(self, data):
        total = 0
        for expense in data:
            total = total + expense.get_amount()
        return total

    def to_dict(self):
        expenses = []

        for element in self.storage_expense:
            expenses.append(element.to_dict())
        data = {"expenses": expenses, "budgets": self.budgets}
        return data

    def extract_data(self, data):
        self.to_expenses_storage(data["expenses"])
        self.budgets = data["budgets"]

    def to_expenses_storage(self, data):
        for element in data:
            self.storage_expense.append(
                Expense(
                    element["description"],
                    element["amount"],
                    element["date"],
                    element["category"],
                )
            )

    def size(self):
        return len(self.storage_expense)

    def get_budget_month(self, month):
        # pre: month debe estar entre 1-12 ambos inclusive
        return self.budgets[str(month)] if self.has_budget(str(month)) else False

    def has_budget(self, month):
        return True if str(month) in self.budgets.keys() else False

    def is_over_budget(self, month):

        if self.has_budget(month):
            month_expenses = self.filter_by_month(month)
            month_sumary = self.get_summary(month_expenses)
            if month_sumary > self.get_budget_month(month):
                return True
            return False
        return None

    def set_budget(self, month, amount):
        # pre: month debe estar entre 1-12 ambos inclusive
        self.budgets[str(month)] = amount
        self.budgets[str(month)] = amount
