from dataclasses import dataclass
import time
import win32api #currently depends on the Windows API through pywin32.
from core.mouse_state import MouseState

class MouseTracker:
    """Track the Windows cursor position and movement state."""
    def __init__(self):

        x, y = win32api.GetCursorPos()

        self.state = MouseState(
            x=x,
            y=y,
            last_x=x,
            last_y=y,
            delta_x=0,
            delta_y=0,
            moving=False,
            timestamp=time.time()
        )

    def update(self):
        """Update the mouse state with the current cursor position and movement information."""
        new_x, new_y = win32api.GetCursorPos()

        last_x = self.state.x
        last_y = self.state.y

        delta_x = new_x - last_x
        delta_y = new_y - last_y

        moving = delta_x != 0 or delta_y != 0

        self.state = MouseState(
            x=new_x,
            y=new_y,
            last_x=last_x,
            last_y=last_y,
            delta_x=delta_x,
            delta_y=delta_y,
            moving=moving,
            timestamp=time.time()
        )

        return self.state

    def get_state(self):
        """Return the lastest tracked mouse state."""
        return self.state