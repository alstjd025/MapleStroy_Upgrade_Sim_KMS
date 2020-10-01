"""
ABS class file
"""


from abc import *
import random


class AbcClass(metaclass=ABCMeta):

    def main_ui(self):
        print("MapleStory Item Upgrade Simulator[kms] ver 0.1")
        print("-----------------------------------------------")
        print("1. Starfore Simulator")
        print("2. Scroll upgrade Simulator")
        print("3. Potential cube Simulator")
        print("4. Exit")
        select = input("Please Enter Command : ")
        return select

    def calc_pct(self, max):    # make random integer range 1~max
        rand_num = random.randint(1, max)
        return rand_num

    @abstractmethod
    def calc_meso_used(self):    #clac current meso spent
        pass

    @abstractmethod
    def calc_stat(self):    #calc end stat
        pass

