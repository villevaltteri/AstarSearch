import sys
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __int__(self):
        super().__init__()
        self.setLayout(qtw.QGridLayout())

        self.show()




if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())




