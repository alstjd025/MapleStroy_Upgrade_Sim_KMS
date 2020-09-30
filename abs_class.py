"""
ABS class file
"""


from abc import *
import random

class abc_class(metaclass=ABCMeta):

    def main_ui(self):
        print("MapleStory Item Upgrade Simulator[kms] ver 0.1\n")
        print("-----------------------------------------------\n")
        print("1. Starfore Simulator\n")
        print("2. Scroll upgrade Simulator\n")
        print("3. Potential cube Simulator\n")
        print("4. Exit\n")
        print("Please Enter Command : ")
        select = input()
        return select

    def calc_pct(self, max):    # make random int range 1~max
        rand_num = random.randint(1, max)
        return rand_num

    @abstractmethod
    def calc_meso(self):    #clac meso spent
        pass

    @abstractmethod
    def calc_stat(self):    #calc stat
        pass

