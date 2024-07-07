import pathlib

import anywidget
import traitlets as tl

class PeriodicTableWidget(anywidget.AnyWidget):
    # clicked = tl.Unicode('').tag(sync=True)
    my_vector = tl.Int(0).tag(sync=True)

    _esm = pathlib.Path(__file__).parent / "bundle.js"
    _css = pathlib.Path(__file__).parent / "widget.css"

