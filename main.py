import time

from core.mouse_tracker import MouseTracker
from core.word import Word
from core.word_index import WordIndex
from core.events import WordEvent


def main():

    tracker = MouseTracker()

    index = WordIndex()

    # Palabras de prueba
    index.add_word(Word("Hello", 400, 200, 120, 35))
    index.add_word(Word("World", 600, 300, 120, 35))
    index.add_word(Word("Python", 800, 450, 140, 35))

    print("=" * 60)
    print("Mueve el mouse sobre las palabras de prueba")
    print("Hello  -> (400,200)")
    print("World  -> (600,300)")
    print("Python -> (800,450)")
    print("=" * 60)

    while True:

        mouse = tracker.update()

        event = index.update(mouse.x, mouse.y)

        if event:

            print("\n" + "=" * 60)

            print(f"Evento    : {event.event_type.name}")
            print(f"Origen    : {event.source}")
            print(f"Timestamp : {event.timestamp}")

            print()

            print(f"Mouse X : {mouse.x}")
            print(f"Mouse Y : {mouse.y}")
            print(f"Delta   : ({mouse.delta_x},{mouse.delta_y})")
            print(f"Moving  : {mouse.moving}")

            print()

            if event.event_type == WordEvent.ENTER:

                print("Entró a la palabra")
                print(f"Actual : {event.data.current.text}")

            elif event.event_type == WordEvent.LEAVE:

                print("Salió de la palabra")
                print(f"Anterior : {event.data.previous.text}")
            
            elif event.event_type == WordEvent.CHANGE:

                print("Cambió de palabra")
                print(f"Anterior : {event.data.previous.text}")
                print(f"Actual   : {event.data.current.text}")

            print("=" * 60)

        time.sleep(0.02)

if __name__ == "__main__":
    main()