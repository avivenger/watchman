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


def compare_watcher_persons(first: WatcherPerson, second: WatcherPerson):
    """
    Returns true if the ids are the same or all identifications.
    :param first:
    :param second:
    :return:
    """
    return \
        (first._id == second._id or
         (first.first_name == second.first_name and
          first.last_name == second.last_name and
          first.nickname == second.nickname and
          first.phone_number == second.phone_number)
         )
