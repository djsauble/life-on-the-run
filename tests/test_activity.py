import pytest
from src.activity import Activity
from enums.workout import Workout
from enums.terrain import Terrain

def test_activity_with_duration():
    activity = Activity(duration=60)
    assert activity.duration == 60
    assert activity.workout_type == Workout.RECOVERY
    assert activity.course_type == Terrain.FLAT

def test_activity_with_pace_and_distance():
    activity = Activity(pace=5, distance=10)
    assert activity.duration == 50
    assert activity.workout_type == Workout.RECOVERY
    assert activity.course_type == Terrain.FLAT

def test_activity_with_invalid_pace_and_distance():
    with pytest.raises(ValueError):
        Activity(pace=None, distance=10)
