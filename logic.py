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
        self.radioButton.setChecked(True)
        self.show()


    def clickButton(self):
        type_of_prokld = 0
        arr = []
        arr.append(self.lineEdit)
        arr.append(self.lineEdit_2)
        arr.append(self.lineEdit_3)
        arr.append(self.lineEdit_4)
        arr.append(self.lineEdit_5)
        arr.append(self.lineEdit_6)
        arr.append(self.lineEdit_7)
        if self.radioButton.isChecked():
            type_of_prokld = 0
            print(0)
        elif self.radioButton_2.isChecked():
            type_of_prokld = 1
            print(1)
        elif self.radioButton_3.isChecked():
            type_of_prokld = 2
            print(2)
        elif self.radioButton_4.isChecked():
            type_of_prokld = 3
            print(3)
        arr.append(type_of_prokld)
        arr.append(self.lineEdit_9)
        arr.append(self.lineEdit_10)
        arr.append(self.lineEdit_11)
        arr.append(self.lineEdit_12)
        arr.append(self.lineEdit_13)
        arr.append(self.lineEdit_14)
        ans = pipes(arr)
        self.lineEdit_15.setText(str(ans))
        print(ans)
        self.Clear()


    def Clear(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.radioButton.setChecked(True)
        self.lineEdit_9.setText("")
        self.lineEdit_10.setText("")
        self.lineEdit_11.setText("")
        self.lineEdit_12.setText("")
        self.lineEdit_13.setText("")
        self.lineEdit_14.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    sys.exit(app.exec_())