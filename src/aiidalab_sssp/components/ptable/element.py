from __future__ import annotations

import typing as t

from solara import HTML, Div, Text
from solara.core import component

from aiidalab_sssp.models.element import ElementModel


@component
def Element(
    element: ElementModel,
    on_hover: t.Callable[[ElementModel], None],
):
    classes = ["element", f"element-{element.number}"]
    if element.disabled:
        classes.append("disabled")

    with Div(
        classes=classes,
        style={"background-color": element.background},
    ) as element_box:
        Text(text=element.symbol, classes=["element-symbol"])
        if not element.disabled:
            with Div(classes=["element-info"]):
                HTML("span", f"{int(element.wfc)}", classes=["element-wfc"])
                HTML("sub", f"({int(element.rho)})", classes=["element-rho"])

    if not element.disabled:
        element_box.on("mouseover", lambda: on_hover(element))

    return element_box
