from abs_class import AbcClass


class StarforceClass(AbcClass):

    def starforce_starting_ui(self):
        self.clear()
        print("Starforce upgrade Simulation")
        print("-----------------------------------------------")
        print("1. 150lv")
        print("2. 160lv")
        print("3. 200lv")
        self.temp = input("Set Item Level : ")
        if self.temp == 1:
            self.item_lev = 150
        elif self.temp == 2:
            self.item_lev = 160
        elif self.temp == 3:
            self.item_lev = 200
        else:
            print("Input error! Please check your command")
        self.clear()
        print(self.item_lev, "Lv Item upgrade")
        print("-----------------------------------------------")
        self.start = input("Set Start Star(min 0 ~ max 24) : ")

    def calc_expectation(self, meso, target):   # calc expectation to target value
        pass

    def calc_meso_used(self, meso, trial):  # clac current meso spent
        pass

    def calc_stat(self):  # calc end stat
        pass

