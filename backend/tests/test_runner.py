import math
from datetime import date, timedelta
import math

from runner_sim.enums.terrain import Terrain
from runner_sim.enums.workout import Workout
from runner_sim.runner import Runner
from runner_sim.constants import TRAINING_DECAY

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

    # Generate weights using the decay factor
    weights = [math.exp(-TRAINING_DECAY * i) for i in range(7)]
    
    # Normalize the weights
    weight_sum = sum(weights)
    normalized_weights = [w / weight_sum for w in reversed(weights)]
    
    # Calculate the weighted load
    last_seven_days = runner.daily_training_load[-7:]
    weighted_load = sum(load * weight for load, weight in zip(last_seven_days, normalized_weights))

    # Assert the calculated value matches the acute training load
    assert math.isclose(runner.acute_training_load, weighted_load)

def test_chronic_training_load():
    runner = Runner(name="John")
    activities = generate_mock_activities()
    for activity in activities:
        runner.add_training_load(activity).sleep()

    # Generate weights using the decay factor
    weights = [math.exp(-TRAINING_DECAY * i) for i in range(28)]
    
    # Normalize the weights
    weight_sum = sum(weights)
    normalized_weights = [w / weight_sum for w in reversed(weights)]
    
    # Calculate the weighted load
    last_twenty_eight_days = runner.daily_training_load[-28:]
    weighted_load = sum(load * weight for load, weight in zip(last_twenty_eight_days, normalized_weights))

    # Assert the calculated value matches the chronic training load
    assert math.isclose(runner.chronic_training_load, weighted_load)

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
    injuries = [runner.check_for_injury() for _ in range(90)].count(True)
    assert injuries > 0  # Should be at least one injury in a three-month period

    # Set a low training load ratio
    runner = Runner(name="John")
    activities = [MockActivity(2 ** i, Workout.RACE, Terrain.FLAT) for i in range(28, 0, -1)]
    for activity in activities:
        runner.add_training_load(activity).sleep()
    injuries = [runner.check_for_injury() for _ in range(90)].count(True)
    assert injuries == 0  # Should be zero injuries in a three-month period

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

def test_training_load_ratio_no_history():
    runner = Runner(name="John")
    assert runner.training_load_ratio == 1

def test_weighted_sum():
    runner = Runner(name="John")
    decay = [7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
    growth = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    days = len(decay)
    decay_weighted_sum = runner._weighted_sum(decay, days)
    growth_weighted_sum = runner._weighted_sum(growth, days)
    assert growth_weighted_sum > decay_weighted_sum  # Ensure the last elements are weighted more heavily than the first elements