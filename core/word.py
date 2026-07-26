from dataclasses import dataclass


@dataclass
class Word:

    text: str

    x: int

    y: int

    width: int

    height: int

    confidence: float = 1.0