from enum import Enum, auto


class MouseEvent(Enum):
    NONE = auto()

    # Movimiento
    MOVE = auto()
    STOP = auto()

    # Botones
    LEFT_CLICK = auto()
    RIGHT_CLICK = auto()
    DOUBLE_CLICK = auto()

    # Scroll
    WHEEL = auto()

    # Contexto
    WINDOW_CHANGED = auto()
    MONITOR_CHANGED = auto()


class ScreenEvent(Enum):
    NONE = auto()

    SCREEN_CHANGED = auto()
    SCREEN_STABLE = auto()


class OCR_Event(Enum):
    NONE = auto()

    OCR_STARTED = auto()
    OCR_COMPLETED = auto()
    OCR_FAILED = auto()


class WordEvent(Enum):
    NONE = auto()

    ENTER = auto()

    LEAVE = auto()

    CHANGE = auto()


class TranslationEvent(Enum):
    NONE = auto()

    TRANSLATION_STARTED = auto()
    TRANSLATION_COMPLETED = auto()
    TRANSLATION_FAILED = auto()


class PopupEvent(Enum):
    NONE = auto()

    SHOW = auto()
    HIDE = auto()
    MOVE = auto()