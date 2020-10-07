from abs_class import AbcClass
import chance_datasheet as datasheet
import math
"""
[Flow]
set lev -> set starting -> set target -> simulate
성공
실패 - 유지 10성까지
실패 - 하락 11성부터
실패 - 파괴 12성부터 ->포스 12성으로 조정
"""

class StarforceClass(AbcClass):
    def __init__(self):
        self.tg_seq = 0
        self.seq_itr = 0
        self.start = 0
        self.target = 0
        self.item_lev = 0
        self.current_star = 0
        self.meso_spent = 0
        self.star = []
        self.trials = 0
        self.success_count = 0
        self.success_cont_temp = 0
        self.success_chance = 0
        self.fail_chance = 0
        self.destroy_chance = 0
        self.destroyed = 0
        self.destroy_prevent = 2
        self.item_price = 0
        self.chancetime = 0
        self.money_temp = 0

    def reset_var(self):
        self.current_star = 0
        self.meso_spent = 0
        self.star = []
        self.trials = 0
        self.success_count = 0
        self.success_cont_temp = 0
        self.success_chance = 0
        self.fail_chance = 0
        self.destroy_chance = 0
        self.destroyed = 0
        self.destroy_prevent = 2
        self.item_price = 0
        self.chancetime = 0
        self.money_temp = 0


    def starforce_starting_ui(self):
        self.clear()
        print("Starforce upgrade Simulation")
        print("-----------------------------------------------")
        self.item_lev = self.get_item_level()
        self.clear()
        print(self.item_lev, "Lv Item upgrade")
        print("-----------------------------------------------")
        self.clear()
        print("Input Item Price")
        print("-----------------------------------------------")
        self.item_price = int(input())
        self.clear()
        self.start = int(input("Set Starting Star(min 0 ~ max 24) : "))
        print("Set Target Star(min", self.start, "~ max 25) : ")
        self.target = int(input())
        while self.destroy_prevent == 2:
            print("Use Destroy Prevention? [y/n]")
            answer = input()
            if answer == 'y':
                self.destroy_prevent = 1
            elif answer == 'n':
                self.destroy_prevent = 0
            else:
                self.destroy_prevent = 2
        pass

    def main_simulation(self):
        self.clear()
        self.current_star = self.start
        print("Starforce upgrade Simulation Start")
        print("-----------------------------------------------")
        print("How many time do you want to Simulate?")
        self.tg_seq = int(input())   # setting target sequence
        self.clear()
        while self.seq_itr != self.tg_seq:
            while self.current_star != self.target:
                self.success_chance = datasheet.st_up[self.current_star]
                self.fail_chance = 100 - datasheet.st_up[self.current_star]
                self.destroy_chance = datasheet.st_des[self.current_star]
                self.chance = self.calc_pct(100)
                # Succeed
                if self.chancetime == 2:
                    self.success_cont_temp += 1
                    self.current_star += 1
                    self.success_count += 1
                    self.star.append("★")
                    self.trials += 1
                    self.chancetime = 0
                elif self.chance <= self.success_chance:
                    self.success_cont_temp += 1
                    self.current_star += 1
                    self.success_count += 1
                    self.star.append("★")
                    self.trials += 1
                # Fail - Destroy
                elif self.chance > 100 - self.destroy_chance and self.current_star >= 12 and self.destroy_prevent == 0:
                    self.success_cont_temp = 0
                    self.current_star = 12
                    self.destroyed += 1
                    self.star = self.star[0:12]
                    self.trials += 1
                    self.meso_spent += self.item_price
                    print("Item destroyed", self.destroyed, " th..")
                # Fail
                else:
                    if self.current_star > 10 and self.current_star != 15 and self.current_star != 20:
                        self.success_cont_temp = 0
                        self.current_star -= 1
                        self.star.pop()
                        self.trials += 1
                        self.chancetime += 1
                    else:
                        self.success_cont_temp = 0
                        self.trials += 1
                        self.chancetime += 1
                self.show_current_star()
                self.meso_spent += self.calc_meso_used(self.current_star)
                #print("[★", self.current_star, "] Trial[", self.trials, "], success [", self.success_count, "] Fail [",
                #      self.trials - self.success_count, "]")
                self.compair_continuous(self.seq_itr, self.success_cont_temp)
            AbcClass.sim_result.append([[] * 6])
            AbcClass.sim_result[self.seq_itr][0] = self.seq_itr
            AbcClass.sim_result[self.seq_itr][1] = self.trials
            AbcClass.sim_result[self.seq_itr][2] = self.success_count
            AbcClass.sim_result[self.seq_itr][4] = self.destroyed
            AbcClass.sim_result[self.seq_itr][5] = self.meso_spent
            print("Seq [", self.seq_itr, "] Trial: ", self.trials)
            self.reset_var()
            self.seq_itr += 1
        # end of simulation sequence


    def result_caculation_starforce(self):
        print("Simulation Complete")
        print("Starting calculation")
        self.calc_average(self.tg_seq, 0, 1)
        print("Average trial calculation complete")
        self.calc_average(self.tg_seq, 1, 5)
        print("Average meso calculation complete")
        self.calc_average(self.tg_seq, 2, 4)
        print("Average destroy calculation compelte")
        self.find_maximum(self.tg_seq, 3, 1)
        print("Maximum trial calculation complete")
        self.find_maximum(self.tg_seq, 4, 3)
        print("Maximum continuous success calculation complete")
        self.find_maximum(self.tg_seq, 5, 4)
        print("Maximum destroy calculation complete")
        self.find_maximum(self.tg_seq, 6, 5)
        print("Maximum meso calculation complete")
        self.find_minimum(self.tg_seq, 7, 5)
        print("Minimum meso calculation complete")
        print("-----------------------------------------------")
        print("Simulation Result")
        print("Used Item Price :", format(self.item_price), ",")
        print("Average Trial :", AbcClass.sim_ststic_result[0])
        print("Average Meso :", AbcClass.sim_ststic_result[1])
        print("Average Destroy :", AbcClass.sim_ststic_result[2])
        print("Maximum Trial :", AbcClass.sim_ststic_result[3])
        print("Maximum continuous Success :", AbcClass.sim_ststic_result[4])
        print("Maximum Destroy :", AbcClass.sim_ststic_result[5])
        print("Maximum Meso :", AbcClass.sim_ststic_result[6])
        print("Minimum Meso :", AbcClass.sim_ststic_result[7])
        print("-----------------------------------------------")

    def show_current_star(self):
        for i in self.star:
            print(i, end='')
        for i in range(25 - len(self.star)):
            print('☆',end='')
        pass

    def calc_meso_used(self, star):  # clac current meso spent
        if star < 10:
            self.money_temp = math.trunc(1000 + (self.item_lev ** 3) * (star + 1)/25)
            return self.money_temp - self.money_temp % 10
        elif star < 15:
             self.money_temp = math.trunc(1000 + (self.item_lev ** 3) * ((star + 1)**2.7)/400)
             return self.money_temp - self.money_temp % 10
        else:
            self.money_temp = math.trunc(1000 + (self.item_lev ** 3) * ((star + 1)**2.7)/200)
            return self.money_temp - self.money_temp % 10
        pass

    def calc_stat(self):  # calc end stat
        pass

