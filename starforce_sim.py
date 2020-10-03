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
        self.start = 0
        self.target = 0
        self.item_lev = 0
        self.current_star = 0
        self.meso_spent = 0
        self.star = []
        self.trials = 0
        self.success_count = 0
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
        while self.current_star != self.target:
            self.success_chance = datasheet.st_up[self.current_star]
            self.fail_chance = 100 - datasheet.st_up[self.current_star]
            self.destroy_chance = datasheet.st_des[self.current_star]
            self.chance = self.calc_pct(100)
            # Succeed
            if self.chancetime == 2:
                self.current_star += 1
                self.success_count += 1
                self.star.append("★")
                self.trials += 1
                self.chancetime = 0
            elif self.chance <= self.success_chance:
                self.current_star += 1
                self.success_count += 1
                self.star.append("★")
                self.trials += 1
            # Fail - Destroy
            elif self.chance > 100 - self.destroy_chance and self.current_star >= 12 and self.destroy_prevent == 0:
                self.current_star = 12
                self.destroyed += 1
                self.star = self.star[0:12]
                self.trials += 1
                self.meso_spent += self.item_price
                print("Item destroyed", self.destroyed, " th..")
            # Fail
            else:
                if self.current_star > 10 and self.current_star != 15 and self.current_star != 20:
                    self.current_star -= 1
                    self.star.pop()
                    self.trials += 1
                    self.chancetime += 1
                else:
                    self.trials += 1
                    self.chancetime += 1
            self.show_current_star()
            self.meso_spent += self.calc_meso_used(self.current_star)
            print("[★", self.current_star, "] Trial[", self.trials, "], success [", self.success_count, "] Fail [",
                  self.trials - self.success_count, "]")
        print("Upgrade Complete")
        print("Used Item Price :", self.item_price)
        print("Total destroy :", self.destroyed, ", Total Trials :", self.trials)
        print("Total Meso Spent :", format(self.meso_spent, ","))

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

