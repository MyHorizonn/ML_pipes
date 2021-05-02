import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp
from PyQt5.QtCore import Qt, QEvent, QObject
from interface import Ui_MainWindow
from pipes import pipes

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.clickButton) #here is where the issue is occurs
        self.show()


    def clickButton(self):
        arr = []
        arr.append(self.lineEdit)
        arr.append(self.lineEdit_2)
        arr.append(self.lineEdit_3)
        arr.append(self.lineEdit_4)
        arr.append(self.lineEdit_5)
        arr.append(self.lineEdit_6)
        arr.append(self.lineEdit_7)
        arr.append(self.lineEdit_8)
        arr.append(self.lineEdit_9)
        arr.append(self.lineEdit_10)
        arr.append(self.lineEdit_11)
        arr.append(self.lineEdit_12)
        arr.append(self.lineEdit_13)
        arr.append(self.lineEdit_14)
        self.lineEdit_15.setText(str(pipes(arr)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    sys.exit(app.exec_())