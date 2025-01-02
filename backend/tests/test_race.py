import pytest
from datetime import datetime
from race import Race
from enums.terrain import Terrain
from enums.competition import Competition

class MockRunner:
    def __init__(self, chronic_training_load):
        self.chronic_training_load = chronic_training_load

@pytest.fixture
def race():
    return Race(10, datetime(2023, 10, 15), "Autumn 10K", 35, [200, 100, 50], Competition.INTERMEDIATE, Terrain.ROLLING)

def test_race_initialization(race):
    assert race.distance == 10
    assert race.date == datetime(2023, 10, 15)
    assert race.name == "Autumn 10K"
    assert race.fee == 35
    assert race.prizes == [200, 100, 50]
    assert race.course_type == Terrain.ROLLING
    assert race.competition["mean"] > 0
    assert race.competition["stddev"] > 0

def test_place_runner_winner(race):
    runner = MockRunner(chronic_training_load=2000)
    percentile, placement = race.place_runner(runner)
    assert "You won!" in placement
    assert percentile == 1.0

def test_place_runner_top_percentile(race):
    runner = MockRunner(chronic_training_load=1000)
    percentile, placement = race.place_runner(runner)
    assert "You finished in the bottom" in placement
    assert 0 < percentile < 100

def test_predict_odds_of_winning(race):
    runner = MockRunner(chronic_training_load=1500)
    odds = race.predict_odds_of_winning(runner)
    assert "%" in odds
