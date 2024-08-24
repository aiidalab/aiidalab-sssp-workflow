from __future__ import annotations

import typing as t

from reacton import use_state
from solara import Div, Style, Text, VBox
from solara.core import component

from aiidalab_sssp.assets.styles import css
from aiidalab_sssp.components.ptable.details import DetailsBox
from aiidalab_sssp.components.ptable.element import Element
from aiidalab_sssp.models.element import ElementModel


@component
def PTable(elements: list[ElementModel]):
    hovered_element, set_hovered_element = use_state(t.cast(ElementModel | None, None))

    def on_hover(element: ElementModel):
        set_hovered_element(element)

    def Placeholder(n: int):
        with Div(classes=["star-placeholder"]):
            Text("★" * n)

    def Table():
        def Elements(start, end):
            for element in elements[start:end]:
                Element(element=element, on_hover=on_hover)

        with VBox(classes=["container ptable"]):
            with Div(classes=["elements"]):
                Elements(0, 56)
                Placeholder(1)
                Elements(71, 88)
                Placeholder(2)
                Elements(103, 118)
            with Div(classes=["elements rare-earth"]):
                Placeholder(1)
                Elements(56, 71)
                Placeholder(2)
                Elements(88, 103)

    Style(css / "table.css")

    with Div(classes=["container ptable-outer"]):
        DetailsBox(element=hovered_element)
        Table()
