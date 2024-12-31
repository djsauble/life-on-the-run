from datetime import datetime
from race import Race
from enums.terrain import Terrain
from enums.competition import Competition

class RaceCalendar:
    def __init__(self, year):
        self.year = year
        self.races = self._populate_races()

    def _populate_races(self):
        races = [
            Race(5, datetime(self.year, 1, 15), "New Year 5K", 25, [100, 50, 25], Competition.RECREATIONAL, Terrain.FLAT),
            Race(5, datetime(self.year, 1, 25), "Winter Wonderland 5K", 25, [100, 50, 25], Competition.RECREATIONAL, Terrain.FLAT),
            Race(10, datetime(self.year, 2, 20), "Winter 10K", 35, [200, 100, 50], Competition.INTERMEDIATE, Terrain.ROLLING),
            Race(21.1, datetime(self.year, 3, 10), "Spring Half Marathon", 50, [300, 150, 75], Competition.TRAINED, Terrain.FLAT),
            Race(10, datetime(self.year, 3, 15), "Shamrock 10K", 35, [200, 100, 50], Competition.INTERMEDIATE, Terrain.ROLLING),
            Race(42.2, datetime(self.year, 4, 17), "Boston Marathon", 150, [5000, 2500, 1000], Competition.ELITE, Terrain.ROLLING),
            Race(42.2, datetime(self.year, 4, 23), "London Marathon", 150, [5000, 2500, 1000], Competition.ELITE, Terrain.FLAT),
            Race(5, datetime(self.year, 5, 5), "Cinco de Mayo 5K", 25, [100, 50, 25], Competition.RECREATIONAL, Terrain.FLAT),
            Race(21.1, datetime(self.year, 5, 20), "Memorial Day Half Marathon", 50, [300, 150, 75], Competition.TRAINED, Terrain.FLAT),
            Race(10, datetime(self.year, 6, 10), "Summer 10K", 35, [200, 100, 50], Competition.INTERMEDIATE, Terrain.ROLLING),
            Race(100, datetime(self.year, 6, 24), "Western States 100", 400, [10000, 5000, 2500], Competition.ELITE, Terrain.MOUNTAINOUS),
            Race(21.1, datetime(self.year, 7, 4), "Independence Half Marathon", 50, [300, 150, 75], Competition.TRAINED, Terrain.FLAT),
            Race(42.2, datetime(self.year, 7, 15), "Summer Heat Marathon", 100, [1000, 500, 250], Competition.EXPERT, Terrain.ROLLING),
            Race(42.2, datetime(self.year, 8, 20), "Summer Marathon", 100, [1000, 500, 250], Competition.EXPERT, Terrain.MOUNTAINOUS),
            Race(160.9, datetime(self.year, 8, 25), "Ultra-Trail du Mont-Blanc", 500, [15000, 7500, 3000], Competition.ELITE, Terrain.MOUNTAINOUS),
            Race(5, datetime(self.year, 9, 10), "Fall 5K", 25, [100, 50, 25], Competition.RECREATIONAL, Terrain.FLAT),
            Race(42.2, datetime(self.year, 9, 24), "Berlin Marathon", 150, [5000, 2500, 1000], Competition.ELITE, Terrain.FLAT),
            Race(5, datetime(self.year, 9, 25), "Harvest 5K", 25, [100, 50, 25], Competition.RECREATIONAL, Terrain.FLAT),
            Race(42.2, datetime(self.year, 10, 8), "Chicago Marathon", 150, [5000, 2500, 1000], Competition.ELITE, Terrain.FLAT),
            Race(10, datetime(self.year, 10, 15), "Autumn 10K", 35, [200, 100, 50], Competition.INTERMEDIATE, Terrain.ROLLING),
            Race(42.2, datetime(self.year, 10, 15), "Amsterdam Marathon", 150, [5000, 2500, 1000], Competition.ELITE, Terrain.FLAT),
            Race(21.1, datetime(self.year, 11, 5), "Thanksgiving Half Marathon", 50, [300, 150, 75], Competition.TRAINED, Terrain.FLAT),
            Race(42.2, datetime(self.year, 11, 5), "New York City Marathon", 150, [5000, 2500, 1000], Competition.ELITE, Terrain.ROLLING),
            Race(42.2, datetime(self.year, 11, 12), "Athens Marathon", 150, [5000, 2500, 1000], Competition.ELITE, Terrain.ROLLING),
            Race(10, datetime(self.year, 11, 20), "Turkey Trot 10K", 35, [200, 100, 50], Competition.INTERMEDIATE, Terrain.ROLLING),
            Race(42.2, datetime(self.year, 12, 3), "Honolulu Marathon", 150, [5000, 2500, 1000], Competition.ELITE, Terrain.ROLLING),
            Race(42.2, datetime(self.year, 12, 10), "Winter Marathon", 100, [1000, 500, 250], Competition.EXPERT, Terrain.MOUNTAINOUS),
            Race(21.1, datetime(self.year, 12, 31), "New Year's Eve Half Marathon", 50, [300, 150, 75], Competition.TRAINED, Terrain.FLAT),
        ]
        return races