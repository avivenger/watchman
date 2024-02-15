import datetime
import uuid
from dataclasses import dataclass


@dataclass
class WatcherPerson:
    _id: str
    first_name: str
    last_name: str
    nickname: str
    phone_number: str

    def __init__(self,
                 first_name: str = "",
                 last_name: str = "",
                 nickname: str = "",
                 phone_number: str = ""):
        if not first_name and not last_name and not nickname:
            raise ValueError("Must provide first name, last name or nickname.")
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.phone_number = phone_number
        self._id = str(uuid.uuid4())

    def pretty_str(self):
        return f"{self.first_name} {self.last_name} {self.nickname}".strip(" ")


@dataclass
class WatchSlot:
    watcher: WatcherPerson
    watch_time_start: datetime.datetime
    watch_time_end: datetime.datetime

    @property
    def watch_duration(self):
        return self.watch_time_end - self.watch_time_start
@dataclass
class WatcherList:
    watcher_list: list[WatchSlot]

    def pretty_print(self):
        stringed_list: list[str] = self.get_stringed_list()
        for stringed_slot in stringed_list:
            print(stringed_slot)

    def get_stringed_list(self) -> list[str]:
        stringed_list: list[str] = list()
        watch_slot_format: str = "{watcher}, {watch_start}-{watch_finish}, duration: {duration}"
        for watcher_slot in self.watcher_list:
            watch_finish_str = watcher_slot.watch_time_end.strftime("%H:%M")
            if watcher_slot.watch_time_end.day != watcher_slot.watch_time_start.day:
                watch_finish_str = watcher_slot.watch_time_end.strftime("%H:%M %Y-%m-%d")
            stringed_list.append(
                watch_slot_format.format(
                    watcher=watcher_slot.watcher.pretty_str(),
                    watch_start=watcher_slot.watch_time_start.strftime("%Y-%m-%d %H:%M"),
                    watch_finish=watch_finish_str,
                    duration=watcher_slot.watch_duration
                )
            )
        return stringed_list


if __name__ == '__main__':
    watcher_person_test1 = WatcherPerson(first_name="mark1")
    watcher_person_test2 = WatcherPerson(first_name="mark2")
    watcher_person_test3 = WatcherPerson(first_name="mark3")
    watcher_person_test4 = WatcherPerson(first_name="mark4")
    watcher_person_test5 = WatcherPerson(first_name="mark5")

    slot1 = WatchSlot(watcher=watcher_person_test1,
                      watch_time_start=datetime.datetime(year=2016, month=12, day=10, hour=10, minute=0, second=0),
                      watch_time_end=datetime.datetime(year=2016, month=12, day=10, hour=10, minute=45, second=0),
                      )
    slot2 = WatchSlot(watcher=watcher_person_test2,
                      watch_time_start=datetime.datetime(year=2016, month=12, day=10, hour=10, minute=45, second=0),
                      watch_time_end=datetime.datetime(year=2016, month=12, day=10, hour=11, minute=30, second=0),
                      )
    slot3 = WatchSlot(watcher=watcher_person_test3,
                      watch_time_start=datetime.datetime(year=2016, month=12, day=10, hour=11, minute=30, second=0),
                      watch_time_end=datetime.datetime(year=2016, month=12, day=10, hour=12, minute=15, second=0),
                      )
    slot4 = WatchSlot(watcher=watcher_person_test4,
                      watch_time_start=datetime.datetime(year=2016, month=12, day=10, hour=23, minute=30, second=0),
                      watch_time_end=datetime.datetime(year=2016, month=12, day=11, hour=00, minute=15, second=0),
                      )
    slot5 = WatchSlot(watcher=watcher_person_test5,
                      watch_time_start=datetime.datetime(year=2016, month=12, day=11, hour=11, minute=30, second=0),
                      watch_time_end=datetime.datetime(year=2016, month=12, day=11, hour=12, minute=15, second=0),
                      )
    watchlist = WatcherList([slot1, slot2, slot3, slot4, slot5])
    watchlist.pretty_print()
