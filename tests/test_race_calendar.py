import pytest
from datetime import datetime
from race_calendar import RaceCalendar
from enums.terrain import Terrain
from enums.competition import Competition

@pytest.fixture
def race_calendar():
    return RaceCalendar(2023)

def test_race_calendar_initialization(race_calendar):
    assert race_calendar.year == 2023
    assert len(race_calendar.races) > 0

def test_race_calendar_race_details(race_calendar):
    race = race_calendar.races[0]
    assert race.distance == 5
    assert race.date == datetime(2023, 1, 15)
    assert race.name == "New Year 5K"
    assert race.fee == 25
    assert race.prizes == [100, 50, 25]
    assert race.competition > 0.0
    assert race.course_type == Terrain.FLAT

def test_race_calendar_race_dates(race_calendar):
    dates = [race.date for race in race_calendar.races]
    assert dates == sorted(dates)

def test_race_calendar_course_types(race_calendar):
    course_types = {race.course_type for race in race_calendar.races}
    assert course_types == {Terrain.FLAT, Terrain.ROLLING, Terrain.MOUNTAINOUS}