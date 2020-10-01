from abs_class import AbcClass


class StarforceClass(AbcClass):

    def starforce_starting_ui(self):
        print("Starforce upgrade Simulation")
        print("-----------------------------------------------")
        print("1. 150lv")
        print("2. 160lv")
        print("3. 200lv")
        self.item_lev = input("Set Item Level : ")


    def calc_expectation(self, meso, target):   # calc expectation to target value
        pass

    def calc_meso_used(self, meso, trial):  # clac current meso spent
        pass

    def calc_stat(self):  # calc end stat
        pass

