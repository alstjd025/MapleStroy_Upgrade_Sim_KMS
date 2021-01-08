"""
MapleStory(kms) upgrade system simulation

[Main Structure]
abc_class.py    (abstract class)
    method
        calc_pct   (calc percantage)
        calc_meso    (calc meso)
        calc_stat     (calc stat)

pot_sim.py  (potential sim function)
    method
        calc_pct_pot   (makes 3 lines of potentials)
        ck_strange_pot    (check strange potentials)
        ck_effective_pot    (check effective potentials)
        ck_useless_pot    (check useless potentials)
        count_cubes     (count cubes spent)
        calc_meso_pot       (calc meso (meso per cube))

list_potentials.py  (list of all potentials, not sorted with tiers)

starforce_sim.py (starforce sim function)
    method
        calc_pct_star   (calc percentages for adding(or removing) stars or destruction)
        calc_meso_star   (calc meso for ~)
        calc_stat_star   (calc additional stats)

scrolls_sim.py (scroll reinforcement sim function)
    method
        calc_pct_scroll  (calc success percentages of each kind of scrolls)
        calc_stat_scroll   (calc additional stats)
        calc_spell_trace    (calc spell traces)
        calc_meso_scroll     (calc meso (spent by white, innocent scrolls and spell traces))


main.py   (main file)

dev tips
    itertools?
"""

from abs_class import *
from starforce_sim import *
from scrolls_sim import *
from pot_sim import *
from ui import *

"""
status
0 wait
1 starforce
2 scroll
3 potential cube
4 exit
"""
def start(myWindow):
    sim = StarforceClass(myWindow)
    sim.starforce_starting_ui(myWindow)
    sim.main_simulation(myWindow)
    sim.clear()
    app.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    myWindow.st_start.clicked.connect(start(myWindow))







































