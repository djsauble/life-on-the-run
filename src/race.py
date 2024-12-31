from enums.terrain import Terrain
from enums.competition import Competition
import random

class Race:
    COMPETITION_PARAMS = {
        Competition.ELITE: {'mean': 2000, 'stddev': 100},
        Competition.EXPERT: {'mean': 1800, 'stddev': 150},
        Competition.TRAINED: {'mean': 1600, 'stddev': 200},
        Competition.INTERMEDIATE: {'mean': 1400, 'stddev': 250},
        Competition.RECREATIONAL: {'mean': 1000, 'stddev': 300},
    }

    def __init__(self, distance, date, name, fee, prizes, competition_level, course_type=Terrain.FLAT):
        self.distance = distance
        self.date = date
        self.name = name
        self.course_type = course_type
        self.fee = fee
        self.prizes = prizes
        params = self.COMPETITION_PARAMS[competition_level]
        self.competition = random.gauss(params['mean'], params['stddev'])
        self.registered = False

    def place_runner(self, runner):
        # Calculate runner's performance score
        performance_score = runner.chronic_training_load + random.gauss(0, 100)

        # Determine placement based on performance score and competition level
        if performance_score > self.competition:
            percentile = 0
            placement = "Winner"
        else:
            # Calculate the percentile placement
            percentile = (1 - (performance_score / self.competition)) * 100
            placement = f"Top {int(100 - percentile)}%"

        return percentile, placement

    def predict_odds_of_winning(self, runner):
        # Calculate runner's performance score
        performance_score = runner.chronic_training_load + random.gauss(0, 100)

        # Calculate odds of winning
        odds_of_winning = 1 - (performance_score / self.competition)
        return max(0, min(odds_of_winning, 1))

    def determine_placement(self, runner):
        # Calculate runner's performance score
        performance_score = runner.chronic_training_load + random.gauss(0, 100)

        # Determine placement based on performance score and competition level
        if performance_score > self.competition:
            return 1, "Winner"
        else:
            # Calculate the percentile placement
            percentile = (1 - (performance_score / self.competition)) * 100
            placement = f"Top {int(100 - percentile)}%"