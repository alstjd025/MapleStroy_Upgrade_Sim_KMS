"""
ABS class file
"""


from abc import *
import random
import os
from time import sleep


class AbcClass(metaclass=ABCMeta):
    # [0 sequence][1 trial][2 suc][3 suc_continued][4 destroy][5 meso]
    sim_result = [[0]*6]
    # [0 mean_trial, 1 mean_meso, 2 mean_des, 3 maximum_trial, 4 continuous_success,
    #  5 max_destroy, 6 max_meso, 7 min_meso]
    sim_ststic_result = [0]*10
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

    def append_sim_result(self):
        a = [[0]*6]
        AbcClass.sim_result.append(a)
        pass

    def compair_continuous(self, seq, temp):
        if AbcClass.sim_result[seq][3] < temp:
            AbcClass.sim_result[seq][3] = temp
        pass

    def calc_average(self, seq, result_idx, ref_idx):
        temp = 0
        for i in range(seq):
            temp += AbcClass.sim_result[i][ref_idx]
        AbcClass.sim_ststic_result[result_idx] = temp/seq
        pass

    def find_maximum(self, tg_seq, result_idx, ref_idx):
        temp = AbcClass.sim_result[0][ref_idx]
        for i in range(0, tg_seq):
            if temp < AbcClass.sim_result[i][ref_idx]:
                temp = AbcClass.sim_result[i][ref_idx]
        AbcClass.sim_ststic_result[result_idx] = temp
        pass

    def find_minimum(self, tg_seq, result_idx, ref_idx):
        temp = AbcClass.sim_result[0][ref_idx]
        for i in range(0, tg_seq):
            if temp > AbcClass.sim_result[i][ref_idx]:
                temp = AbcClass.sim_result[i][ref_idx]
        AbcClass.sim_ststic_result[result_idx] = temp
        pass


    @abstractmethod
    def calc_meso_used(self):    #clac current meso spent
        pass

    @abstractmethod
    def calc_stat(self):    #calc end stat
        pass

