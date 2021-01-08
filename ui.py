import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from abs_class import *
from starforce_sim import *
from scrolls_sim import *
from pot_sim import *


form_class = uic.loadUiType("main_ui.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.tg_seq: int
        self.start: int
        self.target: int
        self.item_lev: int
        self.destroy_prevent: bool  # 1 or 0
        self.item_price: int
        self.mvp: int    # 0없음 1브론즈 2실버 3골드 4다이아 5레드
        self.pcroom: bool
        self.discount_event: bool
        self.st_progress.setValue(0)
        self.st_start.clicked.connect(self.sim_start)
        self.st_stop.clicked.connect(self.sim_stop)

    def sim_start(self):
        self.st_result.setPlainText("--------Start Simulation--------")
        self.tg_seq = int(self.st_sim_num.text())
        self.start = int(self.st_start_force.text())
        self.target = int(self.st_end_force.text())
        self.item_lev = int(self.st_item_lv.currentText())
        self.destroy_prevent = self.st_dst_prev.isChecked()
        self.item_price = int(self.st_item_price.text())
        self.mvp = self.st_mvp.currentIndex()
        self.pcroom = self.st_pcroom.isChecked()
        self.discount_event = self.st_eventB.isChecked()
        self.st_result.append("Parameter Setting Complete")
        sim = StarforceClass(myWindow)
        sim.starforce_starting_ui(myWindow)
        sim.main_simulation(myWindow)

    def append_screen(self, string):
        self.st_result.append(string)

    def setscreen(self, string):
        self.st_result.setPlainText(string)

    def sim_stop(self):
        self.st_result.setPlainText("Simulation Stopped by user")

    def updateprogress(self, cur):
        self.st_progress.setValue(cur/self.tg_seq * 100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
