from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class SystemEvent:

    event_type: object

    source: str

    data: object = None

    timestamp: datetime = field(default_factory=datetime.now)