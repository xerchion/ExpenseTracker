# Version: 1.1.0

from typing import List

from colorama import Fore, init
from rich.console import Console
from rich.table import Table

init()


class View:
    def alert(self, msg: str) -> None:
        # Prints an alert message in red and resets color.

        print(Fore.RED + msg)
        self.reset()

    def info(self, msg: str) -> None:
        # Prints an informational message in blue and resets color.
        print(Fore.BLUE + msg)
        self.reset()

    def ok(self, msg: str) -> None:
        # Prints a success message in green with 'OK' appended and resets color.
        print("\n" + Fore.GREEN + msg + "...........................OK")
        self.reset()

    def reset(self) -> None:
        # Resets the color to default.
        print(Fore.RESET)

    def highlight_for_debugging(self, data: str) -> None:
        # Prints a debugging section with separators.
        self.alert("-" * 59)
        print(data)
        self.alert("-" * 59)

    def header(self, text: str) -> None:
        # Prints a header in blue with an underline.
        print("\n" + Fore.BLUE + text)
        self.info("_" * 70)

    def show_as_table(self, title: str, columns: List, data: List):
        # Crear una consola de Rich
        console = Console()

        # Crear una tabla
        table = Table(title=title)

        # Añadir columnas
        for col in columns:
            table.add_column(col, justify="left", style="cyan", no_wrap=True)
        # Añadir filas
        counter_row = 1

        for row in data:
            table.add_row(
                str(counter_row), str(row[0]), str(row[1]), str(row[2]), row[3]
            )
            counter_row += 1

        console.print(table)
