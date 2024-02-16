import datetime

from python_implementation.dataclasses.watcher_list import WatcherList
from python_implementation.dataclasses.watcher_person import WatcherPerson
from python_implementation.dataclasses.watcher_slot import WatchSlot

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
