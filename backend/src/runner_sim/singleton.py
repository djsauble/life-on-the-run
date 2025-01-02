from .runner import Runner
from .activity import Activity
from .enums.workout import Workout
from .enums.terrain import Terrain

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.runner = None
        return cls._instance

    def initialize_runner(self):
        self.runner = Runner(name="John", age=25)

    def do_intervals(self):
        pace = 8  # Pace in min/mile
        distance = 4  # Distance in miles
        workout_type = Workout.INTERVAL
        course_type = Terrain.FLAT
        activity = Activity(pace=pace, distance=distance, workout_type=workout_type, course_type=course_type)
        return self.simulate_day(activity)

    def do_tempo_run(self):
        pace = 6  # Pace in min/mile
        distance = 6  # Distance in miles
        workout_type = Workout.TEMPO
        course_type = Terrain.FLAT
        activity = Activity(pace=pace, distance=distance, workout_type=workout_type, course_type=course_type)
        return self.simulate_day(activity)

    def do_recovery_run(self):
        pace = 10  # Pace in min/mile
        distance = 6  # Distance in miles
        workout_type = Workout.RECOVERY
        course_type = Terrain.FLAT
        activity = Activity(pace=pace, distance=distance, workout_type=workout_type, course_type=course_type)
        return self.simulate_day(activity)
    
    def simulate_day(self, activity):
        self.runner.add_training_load(activity)
        return self.day_summary()

    def day_summary(self):
        current_day = len(self.runner.daily_training_load)
        self.runner.sleep()
        return f"Day {current_day}: {self.runner.name}'s acute load: {self.runner.acute_training_load}"