from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolBar
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.figure import Figure
import numpy as np


class PlotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # Инициализируем экземпляр
        self.initUi()  # Строим интерфейс

    def initUi(self):
        self.mainLayout = QVBoxLayout(self)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.navToolbar = NavigationToolBar(self.canvas, self)

        self.mainLayout.addWidget(self.canvas)
        self.mainLayout.addWidget(self.navToolbar)

    def clearGraph(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_xlabel('Время')
        ax.set_title('Модель эпидемии')
        ax.grid()
        self.canvas.draw()

