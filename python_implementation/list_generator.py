import random
from datetime import datetime

from python_implementation.dataclasses.post_demand import PostDemand, PostDemandDuration
from python_implementation.dataclasses.watcher_list import WatcherList
from python_implementation.dataclasses.watcher_person import WatcherPerson, compare_watcher_persons
from python_implementation.dataclasses.watcher_slot import WatchSlot


def are_watchers_unique(watcher_list: list[WatcherPerson]) -> bool:
    """
    Given a list, returns true if all items are unique, as defined by having unique ids and at least 1 property is
    different
    :param watcher_list:
    :return:
    """
    for prime_watchman_index in range(len(watcher_list)):
        for other_watchman_index in range(len(watcher_list)):
            if prime_watchman_index == other_watchman_index:
                continue
            if compare_watcher_persons(watcher_list[prime_watchman_index], watcher_list[other_watchman_index]):
                return False
    return True


def generate_simple_list(post_demand: PostDemand, available_watchmen: list[WatcherPerson]):
    number_of_watchers: int = len(available_watchmen)
    shuffled_watchman = random.sample(available_watchmen, len(available_watchmen))
    required_time: PostDemandDuration = post_demand.required_post_times[0]
    duration = required_time.post_duration
    time_for_each_watchman = duration / number_of_watchers
    watchlist: list[WatchSlot] = list()
    dynamic_time = required_time.watch_start
    for watchman in shuffled_watchman:
        new_slot = WatchSlot(watcher=watchman, watch_time_start=dynamic_time,
                             watch_time_end=dynamic_time + time_for_each_watchman)
        watchlist.append(new_slot)
        dynamic_time += time_for_each_watchman
    return WatcherList(post_name=post_demand.post_name, watcher_list=watchlist)


def generate_watcher_list(post_demand: PostDemand, available_watchmen: list[WatcherPerson], **kwargs) -> WatcherList:
    """
    :param post_demand: The post that is required to generate the list for.
    :param available_watchmen: A list of available watchmen.
    :param kwargs: Available flags that will be added over time such as max/min duration, rounding, etc.
    :return: A watcher list for a given post.
    """
    # Start with basic implementation.
    if len(available_watchmen) < 1:
        raise ValueError("Cannot generate a list with no watchmen.")
    if not are_watchers_unique(available_watchmen):
        raise ValueError(f"Available watchmen contains duplicates or 2 people have the same identifications. "
                         f"watchmen_list: {available_watchmen}")
    if len(post_demand.required_post_times) > 1:
        raise ValueError("Non-continues watch times are not supported.")

    # Assume a single post with continues time.
    return generate_simple_list(post_demand, available_watchmen)


if __name__ == '__main__':
    demand: PostDemand = PostDemand(post_name="watchtower",
                                    required_post_times=(PostDemandDuration(datetime(year=1000, month=12, day=15, hour=12),
                                                                            datetime(year=1000, month=12, day=16, hour=12)), ))
    watcher_person_test1 = WatcherPerson(first_name="mark111")
    watcher_person_test2 = WatcherPerson(first_name="mark222")
    watcher_person_test3 = WatcherPerson(first_name="mark333")
    watcher_person_test4 = WatcherPerson(first_name="mark444")
    watcher_person_test5 = WatcherPerson(first_name="mark555")
    watcher_person_test6 = WatcherPerson(first_name="mark666")
    watcher_person_test7 = WatcherPerson(first_name="mark777")
    watcher_person_test8 = WatcherPerson(first_name="mark888")
    watcher_person_test9 = WatcherPerson(first_name="mark999")
    watcher_person_test10 = WatcherPerson(first_name="mark000")

    possible_watchmen: list[WatcherPerson] = [watcher_person_test1,
                                              watcher_person_test2,
                                              watcher_person_test3,
                                              watcher_person_test4,
                                              watcher_person_test5,
                                              watcher_person_test6,
                                              watcher_person_test7,
                                              watcher_person_test8,
                                              watcher_person_test9,
                                              watcher_person_test10]

    da_list: WatcherList = generate_watcher_list(demand, possible_watchmen)
    da_list.pretty_print()
