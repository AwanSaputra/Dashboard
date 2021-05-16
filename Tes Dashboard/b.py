from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi

from matplotlib.backends.backend_qt5agg import (
    NavigationToolbar2QT as NavigationToolbar)

import numpy as np
import random


class MatplotlibWidget(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)

        loadUi("tes2.ui", self)

        self.setWindowTitle("PyQt5 & Matplotlib Example GUI")

        self.pushButton.clicked.connect(
            self.update_graph)

        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))

    def update_graph(self):
        self.MplWidget.canvas.axes.clear()
        df = pd.read_excel(r'd:\KALBE\FPPFKP.xlsx', index_col=None,
                           sheet_name='FPP', usecols="B,D,O", skiprows=4)

        planning = df.loc[df['tier1'] == 'planning'].count()[0]
        ADMINISTRASI = df.loc[df['tier1'] == 'ADMINISTRASI'].count()[0]
        labels = ['planning', 'ADMINISTRASI']
        values = [planning, ADMINISTRASI]
        bars = plt.bar(labels, values)
        plt.bar(labels, values, color=['purple', 'blue'])
        plt.xticks(labels, labels, rotation='vertical')
        plt.title('DATA FPP', fontdict={'fontweight': 'bold', 'fontsize': 18})

        self.MplWidget.canvas.axes.bar(labels, values)
        self.MplWidget.canvas.axes.set_ylabels('jumlah')
        self.MplWidget.canvas.axes.set_title('DATA FPP', fontdict={
            'fontweight': 'bold', 'fontsize': 18})
        self.draw()
        # self.MplWidget.canvas.axes.clear()
        # self.MplWidget.canvas.axes.plot(t, cosinus_signal)
        # self.MplWidget.canvas.axes.plot(t, sinus_signal)
        # self.MplWidget.canvas.axes.legend(
        #     ('cosinus', 'sinus'), loc='upper right')
        # self.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
        # self.MplWidget.canvas.draw()


app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()
