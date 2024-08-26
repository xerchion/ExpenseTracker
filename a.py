from rich.console import Console
from rich.table import Table

# Crear una consola de Rich
console = Console()

# Crear una tabla
table = Table(title="Mi Tabla")

# Añadir columnas
table.add_column("Nombre", justify="left", style="cyan", no_wrap=True)
table.add_column("Edad", justify="right", style="magenta")
table.add_column("País", justify="center", style="green")

# Añadir filas
table.add_row("Alice", "24", "Estados Unidos")
table.add_row("Bob", "30", "Reino Unido")
table.add_row("Charlie", "29", "Canadá")

# Mostrar la tabla
console.print(table)