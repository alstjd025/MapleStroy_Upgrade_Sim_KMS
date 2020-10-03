"""
ABS class file
"""


from abc import *
import random
import os
from time import sleep


class AbcClass(metaclass=ABCMeta):
    # console wait
    def sleepn(self, n):
        sleep(n)
        pass
    # console clear
    def clear(self):
        print('\n' * 100)
        """
        only on IDE
        os.system('cls') -- replace to this when running on cmd
        """
        pass

    def main_ui(self):
        self.clear()
        print("MapleStory Item Upgrade Simulator[kms] ver 0.1")
        print("-----------------------------------------------")
        print("1. Starfore Simulator")
        print("2. Scroll upgrade Simulator")
        print("3. Potential cube Simulator")
        print("4. Exit")
        select = input("Please Enter Command : ")
        return select

    def get_item_level(self):
        self.sim_status = 0
        while self.sim_status != 1:
            self.clear()
            print("1. 150lv")
            print("2. 160lv")
            print("3. 200lv")
            self.temp = input("Set Item Level : ")
            if self.temp == '1':
                return 150
                self.sim_status = 1
            elif self.temp == '2':
                return 160
                self.sim_status = 1
            elif self.temp == '3':
                return 200
                self.sim_status = 1
            else:
                print("Input error! Please check your command")
                self.sim_status = 0
                self.sleepn(1)

    def calc_pct(self, max):    # make random float number range 0.0~max
        rand_num = random.uniform(0, max)
        return rand_num

    @abstractmethod
    def calc_meso_used(self):    #clac current meso spent
        pass

    @abstractmethod
    def calc_stat(self):    #calc end stat
        pass

