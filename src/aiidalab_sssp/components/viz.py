import solara
from .periodic_table import PeriodicTableWidget



@solara.component
def PerioicTable():
    with solara.ColumnsResponsive(12) as main:
        solara.display(PeriodicTableWidget())

    return main


