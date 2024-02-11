from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import random
class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.click)
    def click(self):
        sign = ''
        if  self.ui.checkBox.isChecked():
            sign = '0123456789'
        if self.ui.checkBox_2.isChecked():
            sign = 'abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM'
        if self.ui.checkBox.isChecked and self.ui.checkBox_2.isChecked():
            sign = 'abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM0123456789'


        result = ''
        for _ in range(8):
            result += random.choice(sign)
        self.ui.label_2.setText(result)
        


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()