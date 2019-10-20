import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
#from PySide2.QtCore import *
#from PySide2.QtGui import *

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *


burnrate = 0.984
goalbacs = 0.07
timebetween = 0.25

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
        self.form = QFormLayout()

        self.formGroupBox = QGroupBox("User data")
        self.form.addRow(QLabel("Height:"), self.txtHeight)
        self.form.addRow(QLabel("Weight:"), self.txtWeight)
        self.form.addRow(QLabel("Gender:"), self.cbGender)
        self.formGroupBox.setLayout(self.form)
        
        self.layout.addWidget(self.formGroupBox)

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
    
    #palette.setColor(widget.backgroundRole(), QColor(93,91,89))
    widget.setPalette(palette)

    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())

class Drink(object):
    def __init__(self, product, brand, catagory, style, quantity, quantityunits, units):
        self.product = product
        self.brand = brand
        self.catagory = catagory
        self.style = style
        self.quantity = quantity
        self.quantityunits = quantityunits
        self.units = units
        
        if(self.style == ""):
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
        
def Retrieve (csv):
    file = open(csv, "r")
    drinks = []
    for line in file:
        array = []
        item = ""
        for i in range (0,len(line)):
            if line[i] == ",":
                array.append(item)
                item = ""
            else:
                item += line[i]    
        item = item.replace("\n","")
        array.append(item)
        drinks.append(Drink(array[0],array[1],array[2],array[3],array[4],array[5],array[6]))
    #print (drinks)
    file.close()
        
#Retrieve("Open-Units.csv")   



  
