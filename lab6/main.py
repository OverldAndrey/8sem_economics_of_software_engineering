import sys

import numpy as np
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QLineEdit

params_table = {
    'RELY': [0.75, 0.86, 1.0, 1.15, 1.40],
    'DATA': [0.94, 1.0, 1.08, 1.16],
    'CPLX': [0.70, 0.85, 1.0, 1.15, 1.30],
    'TIME': [1.0, 1.11, 1.50],
    'STOR': [1.0, 1.06, 1.21],
    'VIRT': [0.87, 1.0, 1.15, 1.30],
    'TURN': [0.87, 1.0, 1.07, 1.15],
    'ACAP': [1.46, 1.19, 1.0, 0.86, 0.71],
    'AEXP': [1.29, 1.15, 1.0, 0.91, 0.82],
    'PCAP': [1.42, 1.17, 1.0, 0.86, 0.70],
    'VEXP': [1.21, 1.10, 1.0, 0.90],
    'LEXP': [1.14, 1.07, 1.0, 0.95],
    'MODP': [1.24, 1.10, 1.0, 0.91, 0.82],
    'TOOL': [1.24, 1.10, 1.0, 0.91, 0.82],
    'SCED': [1.23, 1.08, 1.0, 1.04, 1.10],
}


project_modes = {
    'c1': [3.2, 3.0, 2.8],
    'p1': [1.05, 1.12, 1.2],
    'c2': [2.5, 2.5, 2.5],
    'p2': [0.38, 0.35, 0.32]
}


def common_PM(EAF, SIZE):
    return 3.2 * EAF * (SIZE ** 1.05)


def common_TM(PM):
    return 2.5 * (PM ** 0.38)


def calc_EAF(params: list):
    return np.prod(params)


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = uic.loadUi("lab6.ui", self)

        self.RELY = self.ui.comboBox_1
        self.DATA = self.ui.comboBox_2
        self.CPLX = self.ui.comboBox_3
        self.TIME = self.ui.comboBox_4
        self.STOR = self.ui.comboBox_5
        self.VIRT = self.ui.comboBox_6
        self.TURN = self.ui.comboBox_7
        self.ACAP = self.ui.comboBox_8
        self.AEXP = self.ui.comboBox_9
        self.PCAP = self.ui.comboBox_10
        self.VEXP = self.ui.comboBox_11
        self.LEXP = self.ui.comboBox_12
        self.MODP = self.ui.comboBox_13
        self.TOOL = self.ui.comboBox_14
        self.SCED = self.ui.comboBox_15

        self.SIZE: QLineEdit = self.ui.sizeEdit

        self.project_mode = self.ui.comboBox_16

        print(self.ui.comboBox_1.currentIndex())

    def eaf(self):
        RELY = params_table['RELY'][self.RELY.currentIndex()]
        DATA = params_table['DATA'][self.DATA.currentIndex()]
        CPLX = params_table['CPLX'][self.CPLX.currentIndex()]
        TIME = params_table['TIME'][self.TIME.currentIndex()]
        STOR = params_table['STOR'][self.STOR.currentIndex()]
        VIRT = params_table['VIRT'][self.VIRT.currentIndex()]
        TURN = params_table['TURN'][self.TURN.currentIndex()]
        ACAP = params_table['ACAP'][self.ACAP.currentIndex()]
        AEXP = params_table['AEXP'][self.AEXP.currentIndex()]
        PCAP = params_table['PCAP'][self.PCAP.currentIndex()]
        VEXP = params_table['VEXP'][self.VEXP.currentIndex()]
        LEXP = params_table['LEXP'][self.LEXP.currentIndex()]
        MOPD = params_table['MOPD'][self.MODP.currentIndex()]
        TOOL = params_table['TOOL'][self.TOOL.currentIndex()]
        SCED = params_table['SCED'][self.SCED.currentIndex()]

        return RELY * DATA * CPLX * TIME * STOR * VIRT * TURN * ACAP * AEXP * PCAP * VEXP * LEXP * MOPD * TOOL * SCED

    def PM(self):
        mode = self.project_mode.currentIndex()
        SIZE = float(self.SIZE.text())

        return project_modes['c1'][mode] * self.eaf() * (SIZE ** project_modes['p1'][mode])

    def TM(self):
        mode = self.project_mode.currentIndex()

        return project_modes['c2'][mode] * (self.PM() ** project_modes['p2'][mode])


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == '__main__':
    sys.exit(main())
