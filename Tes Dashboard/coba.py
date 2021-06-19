import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import *
from PyQt5 import *
import sys
import matplotlib
import plotly.graph_objects as go
import datetime
import pandas as pd
# from tes2 import Ui_MainWindow
from matplotlib.widgets import TextBox
import mplcursors
matplotlib.use("Qt5Agg")


class MyMplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):

        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.subplots_adjust(bottom=0.2)
        self.axes = self.fig.add_subplot(111)
        # self.input = QLineEdit()
        # self.input.textChanged.connect(self.update_figure)
        axbox = self.fig.add_axes([0.1, 0.02, 0.2, 0.075])
        # text_box.on_submit(update_figure)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def update_figure(self):
        self.axes.clear()

        df = pd.read_excel(r'd:\KALBE\FPPFKP.xlsx', index_col=None,
                           sheet_name='FPP', usecols="B,D,O", skiprows=4)

        planning = df.loc[df['tier1'] == 'planning'].count()[0]
        ADMINISTRASI = df.loc[df['tier1'] == 'ADMINISTRASI'].count()[0]
        NaN = df['tier1'].isnull().values.any().sum()
        labels = ['planning', 'ADMINISTRASI', 'NaN']
        values = [planning, ADMINISTRASI, NaN]
        bars = plt.bar(labels, values)
        for i in range(len(labels)):
            self.axes.text(i, values[i], values[i], ha="center", va="bottom")

        self.axes.bar(labels, values, color=['purple', 'blue', 'red'])
        # value = self.input.text()
        # print(value)
        self.axes.set_xticks(labels)
        self.axes.set_ylabel('Values')
        self.axes.set_xlabel('Categories')
        self.axes.set_title('DATA FPP', fontdict={
                            'fontweight': 'bold', 'fontsize': 18})
        mplcursors.cursor(self.axes, hover=True)
        self.fig.savefig("tes.pdf")
        self.draw()


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.layout = QVBoxLayout(self)
        self.mpl = MyMplCanvas(self, width=5, height=4, dpi=100)
        self.mpl.update_figure()
        # self.input = QLineEdit()
        self.layout.addWidget(self.mpl)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibWidget()
    ui.show()
    sys.exit(app.exec_())
