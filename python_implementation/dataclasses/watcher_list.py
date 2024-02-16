from dataclasses import dataclass

from python_implementation.dataclasses.watcher_slot import WatchSlot


@dataclass
class WatcherList:
    watcher_list: list[WatchSlot]

    def pretty_print(self):
        stringed_list: list[str] = self.get_stringed_list()
        for stringed_slot in stringed_list:
            print(stringed_slot)

    def get_stringed_list(self) -> list[str]:
        stringed_list: list[str] = list()
        watch_slot_format: str = "{watcher}, {watch_start}-{watch_finish}, Duration: {duration}"
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
