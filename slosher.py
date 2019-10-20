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
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        self.btnCalculate = QtWidgets.QPushButton("Calculate!")
        self.txtHours = QLineEdit(self)
        self.txtBetween = QLineEdit(self)
        self.txtWeight = QLineEdit(self)
        #self.lblResults = QLabel(self)

        self.cbSex = QComboBox(self)
        self.cbSex.addItems(["Male", "Female"])

        self.slInebriation = QSlider(Qt.Horizontal)
        self.slInebriation.setMinimum(1)
        self.slInebriation.setMaximum(16)
        self.slInebriation.setValue(8)
        #self.slInebriation.setSingleStep(0.01)
        #self.slInebriation.setTickPosition(QSlider.TicksBelow)
        #self.slInebriation.setTickInterval(13)

        self.layoutUI()
        self.connectUI()

    def layoutUI(self):
        self.layout = QtWidgets.QVBoxLayout()
        self.title = QtWidgets.QHBoxLayout()
        self.form = QFormLayout()

        image = QPixmap('logo.png')
        self.logo = QLabel(self)
        self.logo.setPixmap(image)
        self.logo.setFixedHeight(image.height())
        self.logo.setAlignment(Qt.AlignRight)

        self.lblTitle = QLabel("The correct amount for you to drink.\n\nYou can adjust the slider to control\nhow drunk you will become:\n - The right will have you falling over\n - The left will have you mildly buzzing")

        self.titleBox = QGroupBox("Information:")
        self.title.addWidget(self.lblTitle)
        self.title.addWidget(self.logo)
        self.titleBox.setLayout(self.title)
        #self.titleBox.setFixedHeight(200)
        self.titleBox.setFlat(True)

        self.formGroupBox = QGroupBox("User data:")
        self.form.addRow(QLabel("Total drinking time (minutes):"), self.txtHours)
        self.form.addRow(QLabel("Time between drinks (minutes):"), self.txtBetween)
        self.form.addRow(QLabel("Weight (kg):"), self.txtWeight)
        self.form.addRow(QLabel("Sex:"), self.cbSex)
        self.form.addRow(QLabel("Inebriation level:"), self.slInebriation)
        self.formGroupBox.setLayout(self.form)

        self.resultsTable = QTableWidget()
        self.resultsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.resultsTable.setRowCount(0)
        self.resultsTable.setColumnCount(2)
        self.resultsTable.setHorizontalHeaderLabels(["Drink", "Quantity"])

        self.layout.addWidget(self.titleBox)
        self.layout.addWidget(self.formGroupBox)

        self.layout.addWidget(self.btnCalculate)
        #self.layout.addWidget(self.lblResults)
        self.layout.addWidget(self.resultsTable)

        self.setLayout(self.layout)

        self.adjustSize()

    def connectUI(self):
        self.btnCalculate.clicked.connect(self.calculate)

    def calculate(self):
        if self.txtHours.text() == "" or self.txtBetween.text() == "" or self.txtHours.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Fill in the boxes dummy!")
            msg.setWindowTitle("You there!")

            msg.exec()
            return False

        minbacs = (float(self.slInebriation.value())/100) - 0.005
        maxbacs = (float(self.slInebriation.value())/100) + 0.005
        timebetween = (float(self.txtBetween.text()) / 60)
        recomend = Recomend()
        foo = ""

        self.resultsTable.setRowCount(0)

        for i in recomend.recomended:
            rowPosition = self.resultsTable.rowCount()
            self.resultsTable.insertRow(rowPosition)

            self.resultsTable.setItem(rowPosition, 0, QTableWidgetItem(i.product))
            self.resultsTable.setItem(rowPosition, 1, QTableWidgetItem(i.quantity + i.quantityunits))

            #foo = foo + i.product + " " + i.quantity + i.quantityunits + "\n"

        self.resultsTable.resizeColumnsToContents()
        self.adjustSize()
        #self.lblResults.setText(foo)


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
        self.BAC(widget.txtWeight.text(),widget.cbSex.currentText())

    def VoidStyle(self):
        self.style = self.catagory

    def BAC(self, weight, sex):
        r = -1
        if  sex == "Female":
            r = 0.55
        elif sex == "Male":
            r = 0.68

        self.bac = ( self.AcoholGrams() / (float(weight) * r) ) * 100

    def AcoholGrams(self):
        return float(self.units) * 8
#Retrieve("Open-Units.csv")

class Recomend(object):
    def __init__(self):
        self.drinks = Retrieve("drinks.csv")
        self.currentdrink = self.drinks[random.randint(0,len(self.drinks) - 1)]
        self.currentBACs = burnrate * timebetween * self.currentdrink.bac
        self.drunk = False
        self.recomended = []
        self.recomended.append(self.currentdrink)
        self.time = 0
        self.GetDrinks()

    def NextDrink(self):
        possibledrinks = []
        for i in self.drinks:
            if burnrate * timebetween * (self.currentBACs + i.bac) < maxbacs and burnrate * timebetween * (self.currentBACs + i.bac) > minbacs and i.catagory == self.currentdrink.catagory:
                possibledrinks.append(i)

        self.currentdrink = possibledrinks[random.randint(0, len(possibledrinks) - 1)]
        self.currentBACs = burnrate * timebetween * (self.currentBACs + self.currentdrink.bac)
        self.time += timebetween

    def FirstDrinks(self):
        possibledrinks = []
        for i in self.drinks:
            if burnrate * timebetween * (self.currentBACs + i.bac) < maxbacs and i.catagory == self.currentdrink.catagory:
                possibledrinks.append(i)

        self.currentdrink = possibledrinks[random.randint(0, len(possibledrinks) - 1)]
        self.currentBACs = burnrate * timebetween * (self.currentBACs + self.currentdrink.bac)
        self.time += timebetween

    def GetDrinks(self):
        while not self.drunk and self.time < int(widget.txtHours.text()) / 60:
            self.FirstDrinks()
            self.recomended.append(self.currentdrink)
            if(self.currentBACs > minbacs):
                self.drunk = True
        while self.time < (int(widget.txtHours.text()) / 60):
            self.NextDrink()
            self.recomended.append(self.currentdrink)
        
def Retrieve (csv):
    file = open(csv, "r")
    drinks = []
    count = 0
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
        #print(array[6], count)
        count += 1
        drinks.append(Drink(array[0],array[1],array[2],array[3],array[4],array[5],array[6]))
    #print (drinks)
    file.close()
    return drinks


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    palette = widget.palette()
    
    #palette.setColor(widget.backgroundRole(), QColor(93,91,89))
    widget.setPalette(palette)

    widget.resize(10, 600)
    widget.show()

    sys.exit(app.exec_())
