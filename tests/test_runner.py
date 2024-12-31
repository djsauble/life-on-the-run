import math
from datetime import date, timedelta
from enums.terrain import Terrain
from enums.workout import Workout
from runner import Runner

class MockActivity:
    def __init__(self, duration, workout_type, course_type):
        self.duration = duration
        self.workout_type = workout_type
        self.course_type = course_type

def test_runner_initialization():
    runner = Runner(name="John", birthday=date(2000, 1, 1))
    assert runner.name == "John"
    assert runner.birthday == date(2000, 1, 1)

    runner = Runner(name="Jane", age=25)
    assert runner.name == "Jane"
    assert runner.birthday == date.today() - timedelta(days=25*365)

    runner = Runner(name="Jeff")
    assert runner.name == "Jeff"
    assert runner.birthday == date.today() - timedelta(days=21*365)

def test_runner_age():
    runner = Runner(name="John", birthday=date(2000, 1, 1))
    assert runner.age == date.today().year - 2000 - ((date.today().month, date.today().day) < (1, 1))

def test_add_training_load():
    runner = Runner(name="John")
    activities = generate_mock_activities()
    expected_loads = []
    for activity in activities:
        # Calculate the estimated load manually
        if activity is None:
            expected_loads.append(0)
        else:
            expected_loads.append(int(activity.duration * runner.estimate_rpe(activity)))

        # Use the add_training_load method to add the activity
        runner.add_training_load(activity).sleep()
    
    assert runner.daily_training_load[:-1] == expected_loads

def test_acute_training_load():
    runner = Runner(name="John")
    activities = generate_mock_activities()
    for activity in activities:
        runner.add_training_load(activity).sleep()
    acute_training_load = 0
    for i, load in enumerate(runner.daily_training_load[-7:]):
        acute_training_load += load * (1 / (i+1))
    assert math.isclose(runner.acute_training_load, acute_training_load)

def test_chronic_training_load():
    runner = Runner(name="John")
    activities = generate_mock_activities()
    for activity in activities:
        runner.add_training_load(activity).sleep()
    chronic_training_load = 0
    for i, load in enumerate(runner.daily_training_load[-28:]):
        chronic_training_load += load * (1 / (i+1))
    assert math.isclose(runner.chronic_training_load, chronic_training_load)

def test_training_load_ratio():
    runner = Runner(name="John")
    activities = generate_mock_activities()
    for activity in activities:
        runner.add_training_load(activity).sleep()
    assert math.isclose(runner.training_load_ratio, runner.acute_training_load / runner.chronic_training_load)

def test_race_calendar_initialization():
    runner = Runner(name="John", birthday=date(2000, 1, 1))
    assert runner.race_calendar.year == date.today().year
    assert len(runner.race_calendar.races) > 0

def test_check_for_injury():
    # Set a high training load ratio
    runner = Runner(name="John")
    activities = [MockActivity(2 ** i, Workout.RACE, Terrain.FLAT) for i in range(28)]
    for activity in activities:
        runner.add_training_load(activity).sleep()
    injuries = [runner.check_for_injury() for _ in range(365)].count(True)
    assert injuries > 0  # Should be at least one injury in a year

    # Set a low training load ratio
    runner = Runner(name="John")
    activities = [MockActivity(2 ** i, Workout.RACE, Terrain.FLAT) for i in range(28, 0, -1)]
    for activity in activities:
        runner.add_training_load(activity).sleep()
    injuries = [runner.check_for_injury() for _ in range(365)].count(True)
    assert injuries == 0  # Should be zero injuries in a year

def test_sleep_method():
    runner = Runner(name="John")
    initial_date = runner.today
    assert len(runner.daily_training_load) == 1
    runner.sleep()
    assert runner.today == initial_date + timedelta(days=1)
    assert len(runner.daily_training_load) == 2

def generate_mock_activities():
    activities = []
    for i in range(28):
        if i % 7 == 0:
            # Insert one rest day per week
            activities.append(None)
            continue
        duration = (i % 3 + 1) * 30  # 30, 60, 90 minutes
        workout_type = [Workout.RECOVERY, Workout.TEMPO, Workout.INTERVAL, Workout.RACE][i % 4]
        course_type = [Terrain.FLAT, Terrain.ROLLING, Terrain.MOUNTAINOUS][i % 3]
        activities.append(MockActivity(duration, workout_type, course_type))
    return activities
