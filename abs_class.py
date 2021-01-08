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

    def calc_pct(self, max):    # make random float number range 0.0~max
        rand_num = random.uniform(0, max)
        return rand_num

    def append_sim_result(self):
        a = [0]*6
        self.sim_result.append(a)
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

