import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
#from PySide2.QtCore import *
#from PySide2.QtGui import *
from PySide2.QtGui import QColor
from PySide2.QtCore import Qt

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.btnCalculate = QtWidgets.QPushButton("Calculate!")
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.btnCalculate)
        self.setLayout(self.layout)

        self.btnCalculate.clicked.connect(self.magic)


    def magic(self):
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

