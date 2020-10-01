"""
ABS class file
"""


from abc import *
import random
import os
from time import sleep


class AbcClass(metaclass=ABCMeta):
    # concole wait
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

    def calc_pct(self, max):    # make random integer range 1~max
        rand_num = random.randint(1, max)
        return rand_num

    @abstractmethod
    def calc_meso_used(self):    #clac current meso spent
        pass

    @abstractmethod
    def calc_stat(self):    #calc end stat
        pass

