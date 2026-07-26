from core.word import Word
from core.events import WordEvent
from core.event import SystemEvent
from dataclasses import dataclass
from core.word_event_data import WordEventData

class WordIndex:

    def __init__(self):

        self.words = []
        
        self.current_word = None
        
        self.previous_word = None

    def clear(self):

        self.words.clear()
        
        self.current_word = None
        
        self.previous_word = None

    def add_word(self, word: Word):

        self.words.append(word)

    def add_words(self, words):

        self.words.extend(words)

    def find_word(self, x, y):

        for word in self.words:

            if (

                word.x <= x <= word.x + word.width

                and

                word.y <= y <= word.y + word.height

            ):

                return word

        return None
    
    def update(self, x, y):

        self.previous_word = self.current_word
        self.current_word = self.find_word(x, y)

        # Entró a una palabra
        if self.previous_word is None and self.current_word is not None:

            return SystemEvent(
                event_type=WordEvent.ENTER,
                source="WordIndex",
                data=WordEventData(
                    current=self.current_word,
                    previous=None
                )
            )

        # Salió de una palabra
        if self.previous_word is not None and self.current_word is None:

            return SystemEvent(
                event_type=WordEvent.LEAVE,
                source="WordIndex",
                data=WordEventData(
                    current=None,
                    previous=self.previous_word
                )
            )

        # Cambió de palabra
        if (
            self.previous_word is not None
            and self.current_word is not None
            and self.previous_word != self.current_word
        ):

            return SystemEvent(
                event_type=WordEvent.CHANGE,
                source="WordIndex",
                data=WordEventData(
                    current=self.current_word,
                    previous=self.previous_word
                )
            )

        return None

