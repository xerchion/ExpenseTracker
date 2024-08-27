# TODO Allow users to set a budget for each month and show a warning when the user exceeds the budget.

# TODO Allow users to export expenses to a CSV file.

# TODO use update method in app

# TODO si pide un list y no hay ninguno, indicarlo con un mensaje alert

import calendar
from datetime import datetime

import click

from src.constants import (
    AMOUNT_HELP,
    CATEGORY_HELP,
    DESCRIPTION_HELP,
    HEADER,
    ID_HELP,
    INVALID_ID,
    MESSAGE,
    MONTH_HELP,
    NAME_FILE,
    TITLE,
    TOTAL_EXPENSES,
)
from src.Expense import Expense
from src.File import File
from src.Tracker import Tracker
from src.View import View


class ExpenseTrackerApp:
    def __init__(self) -> None:
        self.file = File(NAME_FILE)
        self.tracker = Tracker(self.file.extract_data())
        self.view = View()

    def add_expense(self, description: str, amount: float, category: str) -> None:
        date = str(datetime.now().date())
        category = category if category else "Uncategorized"
        expense = Expense(description, amount, date, category)
        id = self.tracker.add_expense(expense)
        self.file.save_data(self.tracker.to_dict())
        action = "added"
        self.view.ok(MESSAGE.format(action, id))

    def list_expenses(self, category) -> str:
        data = []
        if category:
            data = self.tracker.filter_by_category(category)
        else:
            data = self.tracker.get_all_expenses()
        if data:
            self.view.show_as_table(TITLE, HEADER, data)
        else:
            self.view.alert("No hay ningun gasto que mostrar")

    def get_summary(self, month: int) -> str:
        month = month if month else "all"
        month_name = calendar.month_name[month]
        filtered = self.tracker.filter_by_month(month)
        total = self.tracker.get_summary(filtered)
        self.view.info(TOTAL_EXPENSES + str(total) + f" ({month_name})")

    def delete_expense(self, id: int) -> str:
        # validate id
        if self.is_id_valid(id):
            self.tracker.delete_expense(id)
            self.file.save_data(self.tracker.to_dict())
            # self.view.alert(DELETE_MESSAGE + str(id))
            action = "deleted"
            self.view.ok(MESSAGE.format(action, id))
        else:
            self.view.alert(INVALID_ID)

    def is_id_valid(self, id):
        return id < self.tracker.get_size() + 1


@click.group()
def cli() -> None:
    pass


app = ExpenseTrackerApp()


@click.command()
@click.option("--description", type=click.STRING, help=DESCRIPTION_HELP, required=True)
@click.option("--amount", type=click.FLOAT, help=AMOUNT_HELP, required=True)
@click.option("--category", type=click.STRING, help=CATEGORY_HELP)
def add(description: str, amount: float, category: str) -> None:
    app.add_expense(description, amount, category)


@click.command()
@click.option("--category", type=click.STRING, help=CATEGORY_HELP)
def list(category) -> None:
    app.list_expenses(category)


@click.command()
@click.option("--month", type=click.INT, help=MONTH_HELP)
def summary(month: int) -> None:
    app.get_summary(month)


@click.command()
@click.option("--id", type=click.INT, help=ID_HELP, required=True)
def delete(id: int) -> None:
    app.delete_expense(id)


# Registramos los comandos al grupo cli
cli.add_command(add)
cli.add_command(list)
cli.add_command(summary)
cli.add_command(delete)

if __name__ == "__main__":
    cli()
