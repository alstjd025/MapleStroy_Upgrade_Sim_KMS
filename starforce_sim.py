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
    def __init__(self, myui):
        self.tg_seq = myui.tg_seq
        self.seq_itr = 0
        self.start = myui.start
        self.target = myui.target
        self.item_lev = myui.item_lev
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
        self.destroy_prevent = myui.destroy_prevent
        self.item_price = myui.item_price
        self.chancetime = 0
        self.money_temp = 0
        print("init complete")

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
        self.chancetime = 0
        self.money_temp = 0


    def starforce_starting_ui(self, myui):
        pass

    def main_simulation(self, myui):
        self.current_star = self.start
        self.append_sim_result()
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
                #self.show_current_star()
                self.meso_spent += self.calc_meso_used(self.current_star)
                self.compair_continuous(self.seq_itr, self.success_cont_temp)
            AbcClass.sim_result[self.seq_itr][0] = self.seq_itr
            AbcClass.sim_result[self.seq_itr][1] = self.trials
            AbcClass.sim_result[self.seq_itr][2] = self.success_count
            AbcClass.sim_result[self.seq_itr][4] = self.destroyed
            AbcClass.sim_result[self.seq_itr][5] = self.meso_spent
            #myui.append_screen(f"Seq [{self.seq_itr} ] Trial: {self.trials}")
            self.reset_var()
            self.seq_itr += 1
            self.append_sim_result()
            myui.updateprogress(self.seq_itr)

        # end of simulation sequence, calculate result
        self.result_caculation_starforce(myui)
        pass


    def result_caculation_starforce(self, myui):
        myui.append_screen("Simulation Complete")
        self.calc_average(self.tg_seq, 0, 1)
        myui.append_screen("Average trial calculation complete")
        self.calc_average(self.tg_seq, 1, 5)
        myui.append_screen("Average meso calculation complete")
        self.calc_average(self.tg_seq, 2, 4)
        myui.append_screen("Average destroy calculation compelte")
        self.find_maximum(self.tg_seq, 3, 1)
        myui.append_screen("Maximum trial calculation complete")
        self.find_maximum(self.tg_seq, 4, 3)
        myui.append_screen("Maximum continuous success calculation complete")
        self.find_maximum(self.tg_seq, 5, 4)
        myui.append_screen("Maximum destroy calculation complete")
        self.find_maximum(self.tg_seq, 6, 5)
        myui.append_screen("Maximum meso calculation complete")
        self.find_minimum(self.tg_seq, 7, 5)
        myui.append_screen("Minimum meso calculation complete")
        myui.append_screen("-----------------------------------------------")
        myui.append_screen("Simulation Result")
        myui.append_screen(f"Used Item Price :{format(self.item_price)}")
        myui.append_screen(f"Average Trial : {AbcClass.sim_ststic_result[0]}")
        myui.append_screen(f"Average Meso :, {AbcClass.sim_ststic_result[1]}")
        myui.append_screen(f"Average Destroy :, {AbcClass.sim_ststic_result[2]}")
        myui.append_screen(f"Maximum Trial :, {AbcClass.sim_ststic_result[3]}")
        myui.append_screen(f"Maximum continuous Success : {AbcClass.sim_ststic_result[4]}")
        myui.append_screen(f"Maximum Destroy :, {AbcClass.sim_ststic_result[5]}")
        myui.append_screen(f"Maximum Meso :, {AbcClass.sim_ststic_result[6]}")
        myui.append_screen(f"Minimum Meso :, {AbcClass.sim_ststic_result[7]}")
        myui.append_screen("-----------------------------------------------")
        pass

    def show_current_star(self):
        for i in self.star:
            print(i, end='')
        for i in range(25 - len(self.star)):
            print('☆', end='')
        print('\n')
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

