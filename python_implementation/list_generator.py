import random
from datetime import datetime

from python_implementation.dataclasses.post_demand import PostDemand, PostDemandDuration
from python_implementation.dataclasses.watcher_list import WatcherList
from python_implementation.dataclasses.watcher_person import WatcherPerson
from python_implementation.dataclasses.watcher_slot import WatchSlot


def generate_watcher_list(post_demand: PostDemand, available_watchmen: list[WatcherPerson], **kwargs) -> WatcherList:
    """
    :param post_demand: The post that is required to generate the list for.
    :param available_watchmen: A list of available watchmen.
    :param kwargs: Available flags that will be added over time such as max/min duration, rounding, etc.
    :return: A watcher list for a given post.
    """
    # Start with basic implementation.
    number_of_watchers: int = len(available_watchmen)
    if number_of_watchers < 1:
        raise ValueError("Cannot generate a list with no watchmen.")
    shuffled_watchman = random.sample(available_watchmen, len(available_watchmen))
    # Verify person isn't listed twice.

    # Assume a single post with continues time.
    required_time: PostDemandDuration = post_demand.required_post_times[0]
    duration = required_time.post_duration
    time_for_each_watchman = duration/number_of_watchers
    watchlist: list[WatchSlot] = list()
    dynamic_time = required_time.watch_start
    for watchman in shuffled_watchman:
        new_slot = WatchSlot(watcher=watchman, watch_time_start=dynamic_time, watch_time_end=dynamic_time + time_for_each_watchman)
        watchlist.append(new_slot)
        dynamic_time += time_for_each_watchman
    return WatcherList(watchlist)


if __name__ == '__main__':
    demand: PostDemand = PostDemand(post_name="watchtower",
                                    required_post_times=(PostDemandDuration(datetime(year=1000, month=12, day=15, hour=12),
                                                                            datetime(year=1000, month=12, day=16, hour=12)), ))
    watcher_person_test1 = WatcherPerson(first_name="mark1")
    watcher_person_test2 = WatcherPerson(first_name="mark2")
    watcher_person_test3 = WatcherPerson(first_name="mark3")
    watcher_person_test4 = WatcherPerson(first_name="mark4")
    watcher_person_test5 = WatcherPerson(first_name="mark5")
    possible_watchmen: list[WatcherPerson] = [watcher_person_test1,
                                              watcher_person_test2,
                                              watcher_person_test3,
                                              watcher_person_test4,
                                              watcher_person_test5]

    da_list: WatcherList = generate_watcher_list(demand, possible_watchmen)
    da_list.pretty_print()
