from abs_class import AbcClass

"""
[Flow]
set lev -> set starting -> set target -> simulate
"""

class StarforceClass(AbcClass):
    def __init__(self):
        self.start = 0
        self.target = 0
        self.item_lev = 0
        self.current_star = 0
        self.spent_meso = 0
        self.trials = 0
        self.chance = 0


    def starforce_starting_ui(self):
        self.clear()
        print("Starforce upgrade Simulation")
        print("-----------------------------------------------")
        self.item_lev = self.get_item_level()
        self.clear()
        print(self.item_lev, "Lv Item upgrade")
        print("-----------------------------------------------")
        self.start = input("Set Starting Star(min 0 ~ max 24) : ")
        print("Set Target Star(min", self.start+1, " ~ max 25) : ")
        self.target = input()
        pass

    def main_simulation(self):
        self.clear()
        self.current_star = self.start
        print("Starforce upgrade Simulation Start")
        print("-----------------------------------------------")
        while self.current_star != self.target:



    def calc_expectation(self, meso, target):   # calc expectation to target value
        pass

    def calc_meso_used(self, meso, trial):  # clac current meso spent
        pass

    def calc_stat(self):  # calc end stat
        pass

