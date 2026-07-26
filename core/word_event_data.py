from dataclasses import dataclass
from typing import Optional
from core.word import Word

@dataclass
class WordEventData:

    current: Optional[Word] = None

    previous: Optional[Word] = None