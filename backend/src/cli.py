import random

from runner_sim.enums.workout import Workout
from runner_sim.enums.terrain import Terrain
from runner_sim.runner import Runner
from runner_sim.activity import Activity

def main():
    # Initialize runner
    runner_name = f"Runner{random.randint(1, 1000)}"
    runner = Runner(name=runner_name)
    print(f"Welcome, {runner.name}! Let's get started with your training and race schedule.")

    # Register for races
    register_for_races(runner)

    while True:
        # Check for injury
        if runner.check_for_injury():
            print(f"Oh no, {runner.name} got injured! Game over.")
            print(f"You survived for {runner.today - runner.start} days!")
            break

        # Check if it's race day
        next_race = None
        days_until_next_race = -1
        try:
            next_race, days_until_next_race = runner.race_calendar.next_race(runner.today)
        except ValueError as e:
            print(e)
        
        # Go for a run
        if next_race and days_until_next_race == 0:
            # Race day
            race_day(runner, next_race)
        else:
            # Training day
            training_day(runner, next_race)

        # Advance to the next day
        runner.sleep()

        # Check if it's a new year
        if runner.today.month == 1 and runner.today.day == 1:
            register_for_races(runner)

def register_for_races(runner):
    print(f"It's {runner.today.year}! Let's register for some races!")
    races = [race for race in list(runner.race_calendar.races.keys()) if race.date >= runner.today]
    for i, race in enumerate(races):
        month_day = race.date.strftime('%m/%d')
        print(f"{i + 1}. {month_day}  - {race.name} ({race.distance} km)")

    race_indices = input("Enter the numbers of the races you want to register for, separated by commas: ").strip().split(',')
    for index in race_indices:
        try:
            race_index = int(index) - 1
            if 0 <= race_index < len(races):
                runner.race_calendar.register(races[race_index])
            else:
                print(f"Invalid race number: {index}")
        except ValueError:
            print(f"Invalid input: {index}")

def training_day(runner, next_race):
    print(f"Today is {runner.today}.")
    if next_race:
        days_until_next_race = (next_race.date - runner.today).days
        print(f"Days until {next_race.name}: {days_until_next_race} days ({next_race.predict_odds_of_winning(runner)} odds of winning)")
    print(f"Chronic training load: {runner.chronic_training_load}")
    print(f"Training load ratio: {runner.training_load_ratio}")

    workout_type = input("What type of workout do you want to do today? (rest/recovery/tempo/interval/race) [01234]: ").strip().lower()
    workout_type = {
        '0': Workout.REST,
        '1': Workout.RECOVERY,
        '2': Workout.TEMPO,
        '3': Workout.INTERVAL,
        '4': Workout.RACE
    }.get(workout_type, Workout.REST)

    if workout_type != Workout.REST:
        terrain_type = input("What type of terrain do you want to run on? (flat/rolling/mountainous) [123]: ").strip().lower()
        terrain_type = {
            '1': Terrain.FLAT,
            '2': Terrain.ROLLING,
            '3': Terrain.MOUNTAINOUS
        }.get(terrain_type, Terrain.FLAT)
        duration = int(input("How many minutes do you want to run?: ").strip())
        activity = Activity(duration=duration, workout_type=workout_type, course_type=terrain_type)
        runner.add_training_load(activity)

def race_day(runner, race):
    print(f"Today is race day! You're running the {race.name} on {race.date}.")
    input("Press Enter to start the race...")

    percentile, placement = race.place_runner(runner)
    print(f"Race results: {placement}")

    input("Press Enter to continue...")

if __name__ == "__main__":
    main()