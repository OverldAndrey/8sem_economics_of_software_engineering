import sys
from PyQt5 import uic, QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QComboBox, QLabel, QSpinBox

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = uic.loadUi("lab7.ui", self)

        self.tab1 = self.ui.tabWidget.widget(0)

        self.EIQty: QLineEdit = self.tab1.findChild(QLineEdit, 'EIEdit')
        self.EOQty: QLineEdit = self.tab1.findChild(QLineEdit, 'EOEdit')
        self.EQQty: QLineEdit = self.tab1.findChild(QLineEdit, 'EQEdit')
        self.ILFQty: QLineEdit = self.tab1.findChild(QLineEdit, 'ILFEdit')
        self.EIFQty: QLineEdit = self.tab1.findChild(QLineEdit, 'EIFEdit')

        self.EIDif: QComboBox = self.tab1.findChild(QComboBox, 'comboBox_1')
        self.EODif: QComboBox = self.tab1.findChild(QComboBox, 'comboBox_2')
        self.EQDif: QComboBox = self.tab1.findChild(QComboBox, 'comboBox_3')
        self.ILFDif: QComboBox = self.tab1.findChild(QComboBox, 'comboBox_4')
        self.EIFDif: QComboBox = self.tab1.findChild(QComboBox, 'comboBox_5')

        self.EIRes: QLabel = self.tab1.findChild(QLabel, 'EILabel')
        self.EORes: QLabel = self.tab1.findChild(QLabel, 'EOLabel')
        self.EQRes: QLabel = self.tab1.findChild(QLabel, 'EQLabel')
        self.ILFRes: QLabel = self.tab1.findChild(QLabel, 'ILFLabel')
        self.EIFRes: QLabel = self.tab1.findChild(QLabel, 'EIFLabel')
        self.TFPRes: QLabel = self.tab1.findChild(QLabel, 'ResLabel')

        self.sysParams = []
        for i in range(1, 15):
            self.sysParams.append(self.tab1.findChild(QSpinBox, 'spinBox_' + str(i)))

        self.ASMPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'ASMEdit')
        self.CPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'CEdit')
        self.CobolPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'CobolEdit')
        self.FortranPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'FortranEdit')
        self.PascalPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'PascalEdit')
        self.CPPPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'CPPEdit')
        self.JavaPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'JavaEdit')
        self.AdaPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'AdaEdit')
        self.VBPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'VBEdit')
        self.VCPPPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'VCPPEdit')
        self.DelphiPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'DelphiEdit')
        self.PerlPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'PerlEdit')
        self.PrologPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'PrologEdit')

        self.NormFPRes: QLabel = self.tab1.findChild(QLabel, 'NormFPLabel')
        self.FPRes: QLabel = self.tab1.findChild(QLabel, 'FPLabel')
        self.LOCRes: QLabel = self.tab1.findChild(QLabel, 'LOCLabel')

        print(self.ui.tabWidget.widget(0).findChild(QLineEdit, 'CEdit'))

    def get_sys_params(self):
        return list(map(lambda sb: sb.value(), self.sysParams))

    def get_lang_percentages(self):
        return {
            'ASM': float(self.ASMPercent.text()),
            'C': float(self.CPercent.text()),
            'Cobol': float(self.CobolPercent.text()),
            'Fortran': float(self.FortranPercent.text()),
            'Pascal': float(self.PascalPercent.text()),
            'CPP': float(self.CPPPercent.text()),
            'Java': float(self.JavaPercent.text()),
            'Ada': float(self.AdaPercent.text()),
            'VB': float(self.VBPercent.text()),
            'VCPP': float(self.VCPPPercent.text()),
            'Delphi': float(self.DelphiPercent.text()),
            'Perl': float(self.PerlPercent.text()),
            'Prolog': float(self.PrologPercent.text()),
        }

    def get_fp_qty(self):
        return {
            'EI': float(self.EIQty.text()),
            'EO': float(self.EOQty.text()),
            'EQ': float(self.EQQty.text()),
            'ILF': float(self.ILFQty.text()),
            'EIF': float(self.EIFQty.text()),
        }

    def get_fp_levels(self):
        return {
            'EI': self.EIDif.currentIndex(),
            'EO': self.EODif.currentIndex(),
            'EQ': self.EQDif.currentIndex(),
            'ILF': self.ILFDif.currentIndex(),
            'EIF': self.EIFDif.currentIndex(),
        }

    def set_fp_results(self, EI, EO, EQ, ILF, EIF, RES):
        self.EIRes.setText(str(EI))
        self.EORes.setText(str(EO))
        self.EQRes.setText(str(EQ))
        self.ILFRes.setText(str(ILF))
        self.EIFRes.setText(str(EIF))
        self.TFPRes.setText(str(RES))

    def set_calculate_fp_results(self, NormFP, FP, LOC):
        self.NormFPRes.setText(str(NormFP))
        self.FPRes.setText(str(FP))
        self.LOCRes.setText(str(LOC))

    @pyqtSlot(name='on_calculateButton_clicked')
    def calculate_fp(self):
        print('Calculate')


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == '__main__':
    sys.exit(main())
