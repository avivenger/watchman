from dataclasses import dataclass
from datetime import datetime

from python_implementation.dataclasses.watcher_person import WatcherPerson


@dataclass
class WatchSlot:
    watcher: WatcherPerson
    watch_time_start: datetime
    watch_time_end: datetime

    @property
    def watch_duration(self):
        return self.watch_time_end - self.watch_time_start
