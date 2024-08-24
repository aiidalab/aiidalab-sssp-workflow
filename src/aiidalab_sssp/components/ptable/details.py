from __future__ import annotations

from solara import Text, VBox
from solara.core import component

from aiidalab_sssp.models.element import ElementModel


@component
def DetailsBox(element: ElementModel | None):
    if element:
        with VBox(classes=["border details-box"]):
            Text(text=element.symbol)
            Text(text=element.number)
