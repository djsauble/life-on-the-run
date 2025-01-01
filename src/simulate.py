import random
import sys
from datetime import timedelta
from runner import Runner
from activity import Activity
from enums.workout import Workout
from enums.terrain import Terrain

def simulate(max_activities=100):
    runner = Runner(name="John Doe", age=25)
    activities = 1

    while activities <= max_activities:
        # Generate a random activity
        pace = random.uniform(5, 10)  # Pace in min/mile
        distance = random.uniform(3, 20)   # Distance in miles
        workout_type = random.choice(list(Workout))
        course_type = random.choice(list(Terrain))

        activity = Activity(pace=pace, distance=distance, workout_type=workout_type, course_type=course_type)
        runner.add_training_load(activity).sleep()

        print(f"Activity {activities}: Acute Load={int(runner.acute_training_load)}, Chronic Load={int(runner.chronic_training_load)}, Load Ratio={runner.training_load_ratio}, Duration={int(activity.duration)} min, Workout={activity.workout_type.value}, Terrain={activity.course_type.value}")

        if runner.check_for_injury():
            print(f"Runner got injured!")
            break

        activities += 1

    print(f"Simulation ended after {activities} activities.")

if __name__ == "__main__":
    max_activities = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    simulate(max_activities)
