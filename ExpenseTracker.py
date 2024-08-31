import calendar
from datetime import datetime

import click

from src.constants import (
    AMOUNT_HELP,
    BUDGET_OVER,
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
        month = str(datetime.now().date().month)
        # HACK Esto es cosa del objeto gastos, deberia encargarse esa clase
        category = category if category else "Uncategorized"
        expense = Expense(description, amount, date, category)
        id = self.tracker.add_expense(expense)

        self.file.save_data(self.tracker.to_dict())
        action = "added"
        self.view.ok(MESSAGE.format(action, id))
        if self.tracker.is_over_budget(month):
            month_name = calendar.month_name[int(month)]
            self.view.alert(BUDGET_OVER.format(month_name))

    def update(self, id: int, description: str, amount: float, category: str) -> None:
        date = str(datetime.now().date())
        month = str(datetime.now().date().month)
        expense = Expense(description, amount, date, category)
        result, err = self.tracker.update_expense(id, expense)
        if result:
            self.file.save_data(self.tracker.to_dict())
            action = "updated"
            self.view.ok(MESSAGE.format(action, id))

        if err:
            self.view.alert(err)
        else:
            if self.tracker.is_over_budget(month):
                month_name = calendar.month_name[int(month)]
                self.view.alert(BUDGET_OVER.format(month_name))

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

    def budget(self, month: int, amount: float) -> None:
        self.tracker.set_budget(month, amount)
        self.file.save_data(self.tracker.to_dict())

    def is_id_valid(self, id):
        return id < self.tracker.size() + 1

    def export(self):
        data = self.tracker.to_dict()
        self.file.to_csv(data["expenses"])


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
@click.option("--id", type=click.INT, help=ID_HELP, required=True)
@click.option("--description", type=click.STRING, help=DESCRIPTION_HELP, required=False)
@click.option("--amount", type=click.FLOAT, help=AMOUNT_HELP, required=False)
@click.option("--category", type=click.STRING, help=CATEGORY_HELP, required=False)
def update(id, description: str, amount: float, category: str) -> None:
    app.update(id, description, amount, category)


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


@click.command()
@click.option("--month", type=click.INT, help=MONTH_HELP, required=True)
@click.option("--amount", type=click.FLOAT, help=AMOUNT_HELP, required=True)
def budget(month: int, amount: float) -> None:
    app.budget(month, amount)


@click.command()
def export() -> None:
    app.export()


# Registramos los comandos al grupo cli
cli.add_command(add)
cli.add_command(update)
cli.add_command(list)
cli.add_command(summary)
cli.add_command(delete)
cli.add_command(budget)
cli.add_command(export)


if __name__ == "__main__":
    cli()
