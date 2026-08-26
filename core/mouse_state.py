from dataclasses import dataclass, field
import time


@dataclass
class MouseState:
    """Represents the state of the mouse cursor at a specific point in time."""
    x: int
    y: int

    last_x: int
    last_y: int

    delta_x: int
    delta_y: int

    moving: bool

    timestamp: float = field(default_factory=time.time)