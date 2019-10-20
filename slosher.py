import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
#from PySide2.QtCore import *
#from PySide2.QtGui import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Slosher")

        self.btnCalculate = QtWidgets.QPushButton("Calculate!")
        self.txtHeight = QLineEdit(self)
        self.txtWeight = QLineEdit(self)
        self.cbGender = QCheckBox("Male?", self)
        #self.txtGender = 
        #self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layoutUI()
        self.connectUI()

    def layoutUI(self):
        self.layout = QtWidgets.QVBoxLayout()

        
        self.layout.addWidget(self.formGroupBox)

        self.layout.addWidget(self.txtHeight)
        self.layout.addWidget(self.btnCalculate)

        self.setLayout(self.layout)

        # mainLayout = QVBoxLayout()
        # mainLayout.addWidget(self.formGroupBox)
        # mainLayout.addWidget(buttonBox)
        # self.setLayout(mainLayout)

    def connectUI(self):
        self.btnCalculate.clicked.connect(self.calculate)

    def calculate(self):
        self.text.setText("E")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    palette = widget.palette()
    
    palette.setColor(widget.backgroundRole(), QColor(93,91,89))
    widget.setPalette(palette)

    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
