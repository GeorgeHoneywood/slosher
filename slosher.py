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
        #self.txtGender = 
        #self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layoutUI()
        self.connectUI()

    def layoutUI(self):
        self.layout = QtWidgets.QVBoxLayout()

        self.layout.addWidget(self.txtHeight)
        self.layout.addWidget(self.btnCalculate)
        self.setLayout(self.layout)

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

class Drink(object):
    def __init__(self, product, brand, catagory, style, quantity, units):
        self.product = product
        self.brand = brand
        self.catagory = catagory
        self.style = style
        self.quantity = quantity
        self.units = units
        
        if(self.style = ""):
            self.VoidStyle()


    def VoidStyle(self):
        self.style = self.catagory

    def BAC(self, weight, sex):
        if(sex.lower == "female"):
            r = 0.55
        elif(sex.lower == "male"):
            r = 0.68

        self.bac = ( self.AcoholGrams / (weight * r) ) * 100

    def AcoholGrams(self):
        return self.units * 8
        




  
