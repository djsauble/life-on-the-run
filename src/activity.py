from enums.workout import Workout
from enums.terrain import Terrain

class Activity:
    def __init__(self, duration=None, pace=None, distance=None, workout_type=Workout.RECOVERY, course_type=Terrain.FLAT):
        self.duration = duration if duration is not None else self.calculate_duration(pace, distance)
        self.workout_type = workout_type
        self.course_type = course_type

    def calculate_duration(self, pace, distance):
        if pace is not None and distance is not None:
            return pace * distance
        else:
            raise ValueError("Either duration or both pace and distance must be provided")