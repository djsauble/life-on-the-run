from datetime import date, timedelta
import random
from typing import List

from enums.workout import Workout
from enums.terrain import Terrain
from race_calendar import RaceCalendar  # Assuming RaceCalendar is defined in race_calendar.py

class Runner:
    def __init__(self, name: str, birthday: date = None, age: int = None):
        self.name = name
        self.start = date.today()
        self.today = date.today()
        if birthday:
            self.birthday = birthday
        elif age:
            self.birthday = self.today - timedelta(days=age*365)
        else:
            # Default is 21 years old
            self.birthday = self.today - timedelta(days=21*365)
        self.daily_training_load = [0]
        self.race_calendar = RaceCalendar(self.today.year)

    @property
    def age(self):
        today = date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

    @property
    def acute_training_load(self):
        return self._weighted_sum(self.daily_training_load[-7:], 7)

    @property
    def chronic_training_load(self):
        return self._weighted_sum(self.daily_training_load[-28:], 28)

    @property
    def training_load_ratio(self):
        if self.chronic_training_load == 0:
            return 1 # If we don't have enough data to compute the ratio, assume a base value of 1
        return self.acute_training_load / self.chronic_training_load
    
    # Advance to the next day
    def sleep(self):
        self.today += timedelta(days=1)
        self.daily_training_load.append(0)

        # Check if it's January 1 of a new year
        if self.today.month == 1 and self.today.day == 1:
            self.race_calendar.reset(self.today)
            print(f"Happy New Year! It's time to register for races for {self.today.year}.")

        return self

    # Add training load to the current day
    def add_training_load(self, activity = None):
        if activity:
            rpe = self.estimate_rpe(activity)
            training_load = activity.duration * rpe
            self.daily_training_load[-1] += int(training_load)
        return self

    # Did an injury occur today?
    def check_for_injury(self):

        # Annualized injury rate of 1 per year when training_load_ratio is 1
        base_injury_rate = 1 / 365

        # Adjust injury rate based on training load ratio
        adjusted_injury_rate = base_injury_rate * self.training_load_ratio

        # Determine if injury occurs
        if random.random() < adjusted_injury_rate:
            return True
        return False

    def _weighted_sum(self, loads: List[float], days: int):
        weights = [1/(i+1) for i in range(days - 1, -1, -1)]
        weighted_loads = [load * weight for load, weight in zip(loads, weights)]
        return sum(weighted_loads)

    def estimate_rpe(self, activity):
        # Compute a base RPE based on workout type and terrain type
        workout_adjustment = {
            Workout.RECOVERY: 2.0,
            Workout.TEMPO: 3.0,
            Workout.INTERVAL: 4.0,
            Workout.RACE: 5.0
        }
        workout_factor = workout_adjustment.get(activity.workout_type, 1.0)

        terrain_adjustment = {
            Terrain.FLAT: 1.0,
            Terrain.ROLLING: 1.2,
            Terrain.MOUNTAINOUS: 1.5
        }
        terrain_factor = terrain_adjustment.get(activity.course_type, 1.0)

        base_rpe = terrain_factor * workout_factor

        # Rested runners get a lower RPE, tired runners get a higher one
        rest_adjustment = self.training_load_ratio - 1.0  # Adjust linearly based on fitness factor
        rest_adjustment = max(-1, min(rest_adjustment, 1))  # Clamp between -1 and 1

        # Experienced runners get a lower RPE, beginners get a higher one
        load_adjustment = -(self.chronic_training_load - 650) / 100  # Adjust linearly based on chronic load
        load_adjustment = max(-2, min(load_adjustment, 2))  # Clamp between -2 and 2

        adjusted_rpe = base_rpe + rest_adjustment + load_adjustment
        return max(1, min(adjusted_rpe, 10)) # Clamp between 1 and 10
