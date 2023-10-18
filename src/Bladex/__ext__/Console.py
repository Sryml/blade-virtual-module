# Module 'Console'
from __future__ import annotations

import Bladex.__sub__.b_types as __bt


def ConsoleOutput(text: str) -> __bt.Bool:
    """ConsoleOutput(string texto)
    Muestra texto por la consola."""
    ...


def ConsoleVisible() -> __bt.Bool:
    """ConsoleVisible()
    Indica si la consola es visible."""
    ...


def ShowConsole(sw: __bt.Bool) -> __bt.Bool:
    """ShowConsole(int sw)
    Muestra/oculta la consola."""
    ...
