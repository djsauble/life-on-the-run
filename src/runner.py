from datetime import date, timedelta
from typing import List

class Runner:
    def __init__(self, name: str, birthday: date = None, age: int = None):
        self.name = name
        if birthday:
            self.birthday = birthday
        elif age:
            self.birthday = date.today() - timedelta(days=age*365)
        else:
            # Default is 21 years old
            self.birthday = date.today() - timedelta(days=21*365)
        self.daily_training_load = []
        self.next_race = None

    @property
    def age(self):
        today = date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

    # Add a new day's worth of training load
    def add_training_load(self, load: float):
        self.daily_training_load.append(load)

    @property
    def acute_training_load(self):
        return self._weighted_sum(self.daily_training_load[-7:], 7)

    @property
    def chronic_training_load(self):
        return self._weighted_sum(self.daily_training_load[-28:], 28)

    @property
    def training_load_ratio(self):
        if self.chronic_training_load == 0:
            return float('inf')
        return self.acute_training_load / self.chronic_training_load

    def _weighted_sum(self, loads: List[float], days: int):
        weights = [1/(i+1) for i in range(days)]
        weighted_loads = [load * weight for load, weight in zip(loads, weights)]
        return sum(weighted_loads)

    def set_next_race(self, race_id: int):
        self.next_race = race_id