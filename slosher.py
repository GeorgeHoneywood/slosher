import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
#from PySide2.QtCore import *
#from PySide2.QtGui import *

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

burnrate = 0.984
minbacs = 0.07
maxbacs = 0.08
timebetween = 0.25

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Slosher")

        self.btnCalculate = QtWidgets.QPushButton("Calculate!")
        self.txtHours = QLineEdit(self)
        self.txtWeight = QLineEdit(self)
        self.cbSex = QComboBox(self)

        self.cbSex.addItems(["Male", "Female"])

        self.layoutUI()
        self.connectUI()

    def layoutUI(self):
        self.layout = QtWidgets.QVBoxLayout()
        self.form = QFormLayout()

        image = QPixmap('slosher/logo.png')
        self.logo = QLabel(self)
        self.logo.setPixmap(image)
        self.logo.setFixedHeight(image.height())
        self.logo.setAlignment(Qt.AlignRight)

        self.formGroupBox = QGroupBox("User data")
        self.form.addRow(QLabel("Time between drinks (minutes):"), self.txtHours)
        self.form.addRow(QLabel("Weight (kg):"), self.txtWeight)
        self.form.addRow(QLabel("Sex:"), self.cbSex)
        self.formGroupBox.setLayout(self.form)
        
        self.layout.addWidget(self.logo)
        self.layout.addWidget(self.formGroupBox)

        self.layout.addWidget(self.btnCalculate)

        self.setLayout(self.layout)

    def connectUI(self):
        self.btnCalculate.clicked.connect(self.calculate)

    def calculate(self):
        pass

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

        self.bac = ( self.AcoholGrams / (int(weight) * r) ) * 100

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
    return drinks
        
#Retrieve("Open-Units.csv")   
class Recomend(object):
    def __init__(self):
        self.drinks = Retrieve("drinks.csv")
        self.currentdrink = self.drinks[random.randint(0,len(self.drinks) - 1)]
        self.currentBACs = burate * timebetween * self.currentdrink.BAC(MyWidget.txtWeight.text(), MyWidget.cbGender.text())
        self.drunk = False
        self.recomended = []
        self.time = 0

    def NextDrink(self):
        possibledrinks = []
        for i in self.drinks:
            if self.currentBACs + burate * timebetween * i.BAC(MyWidget.txtWeight.text(),MyWidget.cbGender.text())< maxbacs and self.currentBACs+burate * timebetween * i.BAC(MyWidget.txtWeight.text(),MyWidget.cbGender.text()) > minbacs and i.catagory = self.currentdrink.catagory:
                possibledrinks.append(i)

        self.currentdrink = possibledrinks[random.randint(0, len(possibledrinks) - 1)]
        self.currentBACs = self.currentBACs + (burate * timebetween * self.currentdrink.BAC(MyWidget.txtWeight.text(), MyWidget.cbGender.text()))
        self.time += timebetween

  def GetDrinks(self):
      while not self.drunk:
          #and self.time < TOTALTIME#
          if(self.currentBACs > minbacs):
              self.drunk = True
      #while self.time < TOTAL TIME:
          self.NextDrink()        
