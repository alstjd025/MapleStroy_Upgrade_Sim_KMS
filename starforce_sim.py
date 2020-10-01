from abs_class import AbcClass

"""
[Flow]
set lev -> set starting -> set target -> simulate
"""

class StarforceClass(AbcClass):

    def starforce_starting_ui(self):
        self.sim_status = 0
        while(self.sim_status != 1):
            self.clear()
            print("Starforce upgrade Simulation")
            print("-----------------------------------------------")
            print("1. 150lv")
            print("2. 160lv")
            print("3. 200lv")
            self.temp = input("Set Item Level : ")
            if self.temp == '1':
                self.item_lev = 150
                self.sim_status = 1
            elif self.temp == '2':
                self.item_lev = 160
                self.sim_status = 1
            elif self.temp == '3':
                self.item_lev = 200
                self.sim_status = 1
            else:
                print("Input error! Please check your command")
                self.sim_status = 0
                self.sleepn(1)
        self.clear()
        print(self.item_lev, "Lv Item upgrade")
        print("-----------------------------------------------")
        self.start = input("Set Starting Star(min 0 ~ max 24) : ")

    def calc_expectation(self, meso, target):   # calc expectation to target value
        pass

    def calc_meso_used(self, meso, trial):  # clac current meso spent
        pass

    def calc_stat(self):  # calc end stat
        pass

