# -*- coding: utf-8 -*-

import sys
import threading
import random

import numpy as np

from PyQt5.QtWidgets import QApplication, QDialog, QSizePolicy  #, QMenu, QVBoxLayout, QMessageBox, QWidget, QPushButton
from PyQt5 import uic

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


BEST_NAME_IN_THE_WORLD = "Ульяночка"


class Window(QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("ui.ui", self)

        self.setStyleSheet("""
            #you + me {
                height: calc(165+185);
                top: sky;
                bottom: sea;
                let_your: eye;
                never: cry;
                our_dreams: bright;
                your_heart: warm;
                between_us: storm;
                its_love: all right;
            }
       	""")

        self.plot = PlotCanvas(self, width=5, height=4)
        self.plot.move(0,0)

        self.hearts = ["❤", "💓", "💕", "💖", "💗", "💘", "💙", "💚", "💛", "🧡", "💜", "🖤", "💝", "💞", "💟", "❣"]

        self.button.clicked.connect(self.plot.plot)

        self.change_hearts()

    def change_hearts(self):
        self.thread = threading.Timer(1.0, self.change_hearts)
        self.thread.start()

        heart = random.choice(self.hearts)
        self.button.setToolTip(heart + " " + BEST_NAME_IN_THE_WORLD + " " + heart)

    def closeEvent(self, event):
    	self.thread.cancel()
    	super().closeEvent(event)

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def plot(self):
        ax = self.figure.add_subplot(111)
        y, x = np.ogrid[-2:2:100j, -2:2:100j]
        ax.contour(x.ravel(), y.ravel(), (x**2+y**2-1)**3 - x**2*y**3, [0])

        self.draw()


app = QApplication(sys.argv)
ex = Window()
ex.show()
sys.exit(app.exec_())