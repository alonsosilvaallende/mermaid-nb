import importlib.metadata
import pathlib

import anywidget
import traitlets
from typing import Literal

try:
    __version__ = importlib.metadata.version("mermaid-nb")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"

class Mermaid(anywidget.AnyWidget):
    """
    Mermaid diagram widget.

    Parameters
    ----------
    diagram : str
        Mermaid diagram definition string.
    theme : str
        One of: "default", "neutral", "dark", "forest", "base".
    look : str
        One of: "classic", "handDrawn".
    theme_variables : dict
        Override theme variables, e.g. {"fontFamily": "Arial"}.
    """
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    _css = pathlib.Path(__file__).parent / "static" / "widget.css"
    diagram         = traitlets.Unicode("flowchart LR\n A --> B").tag(sync=True)
    theme           = traitlets.Unicode("default").tag(sync=True)
    look            = traitlets.Unicode("classic").tag(sync=True)
    theme_variables = traitlets.Dict({}).tag(sync=True)

    def __init__(
        self,
        diagram: str = "flowchart LR\n Hello --> World",
        theme: Literal["default", "neutral", "dark", "forest", "base"] = "default",
        look: Literal["classic", "handDrawn"] = "classic",
        theme_variables: dict = {},
        **kwargs
    ):
        super().__init__(
            diagram=diagram,
            theme=theme,
            look=look,
            theme_variables=theme_variables,
            **kwargs
        )
