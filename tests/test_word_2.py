import sys
from pathlib import Path

# Agrega la carpeta raíz al path de Python
sys.path.append(str(Path(__file__).resolve().parent.parent))

from core.mouse_tracker import MouseTracker
from core.word import Word
from core.word_index import WordIndex

import time

tracker = MouseTracker()

index = WordIndex()

index.add_word(

    Word(

        text="Hello",

        x=400,

        y=200,

        width=100,

        height=30

    )

)

index.add_word(

    Word(

        text="World",

        x=600,

        y=300,

        width=120,

        height=30

    )

)

last_word = None

while True:

    mouse = tracker.update()

    word = index.find_word(

        mouse.x,

        mouse.y

    )

    if word != last_word:

        if word:

            print(

                f"Entraste en: {word.text}"

            )

        else:

            print(

                "Fuera de cualquier palabra"

            )

        last_word = word

    time.sleep(0.02)