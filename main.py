import sys, os, requests
from PyQt5 import QtWidgets, QtCore
from matplotlib.backends.backend_pdf import PdfPages
import design, PlotWidget
import numpy as np
from math import *

class initializeEpidemicModel(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Делаем возможность доступа к переменным, методам в файле design.py
        super().__init__()
        self.setupUi(self)

        self.widget.clearGraph()  # Очищаем график перед запуском

        self.directory = os.getcwd()  # Местоположение программы при запуске


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = initializeEpidemicModel()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()