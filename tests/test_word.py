from core.Word import Word
from core.Word_index import WordIndex

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