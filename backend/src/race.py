from enums.terrain import Terrain
from enums.competition import Competition
import random
from scipy.stats import norm

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
        self.competition = self.COMPETITION_PARAMS[competition_level]

    def place_runner(self, runner):
        # Calculate runner's performance score
        your_performance_score = random.gauss(runner.chronic_training_load, 100)
        top_competitor_score = random.gauss(self.competition["mean"], self.competition["stddev"])

        # Determine placement based on performance score and competition level
        percentile = norm.cdf(your_performance_score, self.competition["mean"], self.competition["stddev"])
        if your_performance_score > top_competitor_score:
            percentile = 1.00
            placement = f"You won! Enjoy your ${self.prizes[0]} of prize money!"
        elif percentile >= .5:
            # Calculate the percentile placement
            placement = f"You finished in the top {int(100 - (percentile * 100))}%"
        else:
            placement = f"You finished in the bottom {int(percentile * 100)}%"

        return percentile, placement

    def predict_odds_of_winning(self, runner):
        # Calculate runner's performance score
        your_estimated_score = random.gauss(runner.chronic_training_load, 100)

        # Calculate odds of winning
        odds_of_winning = norm.cdf(your_estimated_score, self.competition["mean"], self.competition["stddev"])
        return "{:.1f}%".format(odds_of_winning * 100)
