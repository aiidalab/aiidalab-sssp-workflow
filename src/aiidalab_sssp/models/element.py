from dataclasses import dataclass


@dataclass(frozen=True)
class ElementModel:
    number: int
    symbol: str
    dual: float = 0.0
    wfc: float = 0.0
    rho: float = 0.0
    md5: str = ""
    filename: str = ""
    pseudopotential: str = ""
    background: str = "#dddddd"
    disabled: bool = False
