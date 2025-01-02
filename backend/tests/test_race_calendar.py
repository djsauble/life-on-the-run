import pytest
from datetime import date

from runner_sim.race_calendar import RaceCalendar
from runner_sim.enums.terrain import Terrain
from runner_sim.enums.competition import Competition
from runner_sim.race import Race

@pytest.fixture
def race_calendar():
    return RaceCalendar(2023)

def test_race_calendar_initialization(race_calendar):
    assert race_calendar.year == 2023
    assert len(race_calendar.races) > 0

def test_race_calendar_race_details(race_calendar):
    race = list(race_calendar.races.keys())[0]
    assert race.distance == 5
    assert race.date == date(2023, 1, 15)
    assert race.name == "New Year 5K"
    assert race.fee == 25
    assert race.prizes == [100, 50, 25]
    assert race.competition["mean"] > 0
    assert race.competition["stddev"] > 0
    assert race.course_type == Terrain.FLAT

def test_race_calendar_race_dates(race_calendar):
    dates = [race.date for race in race_calendar.races]
    assert dates == sorted(dates)

def test_race_calendar_course_types(race_calendar):
    course_types = {race.course_type for race in race_calendar.races}
    assert course_types == {Terrain.FLAT, Terrain.ROLLING, Terrain.MOUNTAINOUS}

def test_register_race(race_calendar):
    race = list(race_calendar.races.keys())[0]
    race_calendar.register(race)
    assert race_calendar.races[race] is True

def test_unregister_race(race_calendar):
    race = list(race_calendar.races.keys())[0]
    race_calendar.register(race)
    race_calendar.unregister(race)
    assert race_calendar.races[race] is False

def test_register_nonexistent_race(race_calendar):
    race = Race(5, date(2023, 1, 1), "Nonexistent Race", 25, [100, 50, 25], Competition.RECREATIONAL, Terrain.FLAT)
    with pytest.raises(ValueError, match="Race not found in calendar"):
        race_calendar.register(race)

def test_unregister_nonexistent_race(race_calendar):
    race = Race(5, date(2023, 1, 1), "Nonexistent Race", 25, [100, 50, 25], Competition.RECREATIONAL, Terrain.FLAT)
    with pytest.raises(ValueError, match="Race not found in calendar"):
        race_calendar.unregister(race)

def test_next_race(race_calendar):
    today = date(2023, 1, 1)
    race = list(race_calendar.races.keys())[0]
    race_calendar.register(race)
    next_race, days_until_next_race = race_calendar.next_race(today)
    assert next_race.date == date(2023, 1, 15)
    assert days_until_next_race == 14
    next_race, days_until_next_race = race_calendar.next_race(date(2023, 1, 15))
    assert days_until_next_race == 0

def test_no_more_races(race_calendar):
    today = date(2023, 12, 31)
    race = list(race_calendar.races.keys())[0]
    race_calendar.register(race)
    with pytest.raises(ValueError, match="You have no more races this year"):
        race_calendar.next_race(today)

def test_reset_new_year(race_calendar):
    today = date(2024, 1, 1)
    race_calendar.register(list(race_calendar.races.keys())[0])
    race_calendar.reset(today)
    assert race_calendar.year == 2024
    assert len(race_calendar.races) > 0
    assert all(registered == False for registered in race_calendar.races.values())
    assert all(race.date.year == 2024 for race in race_calendar.races.keys())
