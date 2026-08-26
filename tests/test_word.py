import sys
from pathlib import Path

# Agrega la carpeta raíz al path de Python
sys.path.append(str(Path(__file__).resolve().parent.parent))

from core.word import Word
from core.word_index import WordIndex

index = WordIndex()

index.add_word(

    Word(

        "Hello",

        100,

        100,

        80,

        30

    )

)

index.add_word(

    Word(

        "Python",

        250,

        220,

        100,

        30

    )

)

while True:

    x = int(input("X: "))

    y = int(input("Y: "))

    word = index.find_word(x, y)

    if word:

        print(word.text)

    else:

        print("No encontrada")