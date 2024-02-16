import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass
class PostDemandDuration:
    _id: str
    watch_start: datetime
    watch_end: datetime

    def __init__(self, watch_start: datetime, watch_end: datetime):
        self._id = str(uuid.uuid4())
        if watch_end <= watch_start:
            raise ValueError(f"End time: {watch_end} cannot be before start time: {watch_start}")
        self.watch_start = watch_start
        self.watch_end = watch_end

    @property
    def post_duration(self):
        return self.watch_end - self.watch_start


@dataclass
class PostDemand:
    _id: str
    post_name: str
    required_post_times: tuple[PostDemandDuration]

    def __init__(self, post_name: str, required_post_times: tuple[PostDemandDuration]):
        self.post_name = post_name
        self._id = str(uuid.uuid4())
        if len(required_post_times) < 1:
            raise ValueError("Cannot start declare a demand without start and finish time.")
        for post_time_demand in required_post_times:
            for post_time_demand_comparison in required_post_times:
                if post_time_demand._id == post_time_demand_comparison._id:
                    continue
                if (post_time_demand.watch_start <= post_time_demand_comparison.watch_start <= post_time_demand.watch_end) or \
                     (post_time_demand.watch_start <= post_time_demand_comparison.watch_end <= post_time_demand.watch_end):
                    raise ValueError("Received watch times for single post with intersection.")
        self.required_post_times = required_post_times
