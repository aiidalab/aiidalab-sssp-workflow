from __future__ import annotations

import json
from pathlib import Path

from solara import HTML, Div, Style, Text, VBox
from solara.core import component

from aiidalab_sssp.assets.styles import css
from aiidalab_sssp.components.ptable.table import PTable
from aiidalab_sssp.models.element import ElementModel


@component
def Page():
    symbols: list[str] = json.loads(Path("data/symbols.json").read_text())
    data: dict[str, dict] = json.loads(Path("data/sssp_efficiency.json").read_text())
    metadata: dict[str, dict] = json.loads(Path("data/metadata.json").read_text())

    elements = [
        ElementModel(
            number=number,
            symbol=symbol,
            wfc=data[symbol]["cutoff"],
            rho=data[symbol]["rho_cutoff"],
            dual=data[symbol]["dual"],
            md5=data[symbol]["md5"],
            filename=data[symbol]["filename"],
            pseudopotential=data[symbol]["pseudopotential"],
            background=metadata[data[symbol]["pseudopotential"]]["background_color"],
            disabled=data[symbol]["disabled"] if "disabled" in data[symbol] else False,
        )
        if symbol in data
        else ElementModel(
            number=number,
            symbol=symbol,
            disabled=True,
        )
        for number, symbol in enumerate(symbols, 1)
    ]

    def Legend():
        with Div(classes=["legend"]):
            for pp in metadata.values():
                with Div(classes=["legend-item"]):
                    HTML(
                        classes=["legend-item-marker"],
                        style={"background-color": pp["background_color"]},
                    )
                    Text(text=pp["display_name"])

    Style(css / "explore.css")

    with VBox():
        Text(text="SSSP Efficiency (v1.3.0)", classes=["title"])
        Legend()
    PTable(elements)
