import math
from datetime import date, timedelta
from runner import Runner

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
    for load in [5.0, 7.0, 9.0]:
        runner.add_training_load(load)
    assert runner.daily_training_load == [5.0, 7.0, 9.0]

def test_acute_training_load():
    runner = Runner(name="John")
    for i in range(7):
        runner.add_training_load(10.0)
    assert math.isclose(runner.acute_training_load, sum([10.0 / (i + 1) for i in range(7)]), rel_tol=1e-9)

def test_chronic_training_load():
    runner = Runner(name="John")
    for i in range(28):
        runner.add_training_load(10.0)
    assert math.isclose(runner.chronic_training_load, sum([10.0 / (i + 1) for i in range(28)]))

def test_training_load_ratio():
    runner = Runner(name="John")
    for i in range(28):
        runner.add_training_load(10.0)
    assert math.isclose(runner.training_load_ratio, runner.acute_training_load / runner.chronic_training_load)

def test_set_next_race():
    runner = Runner(name="John")
    runner.set_next_race(123)
    assert runner.next_race == 123
