import sys,os
import searchEngine

required_packages=["PyQt5"]

for my_package in required_packages:
    try:
        command_string="pip install "+ my_package+ " --yes"
        os.system(command_string)
    except:
        count=1

from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QPushButton, QLabel,
                             QGridLayout,QVBoxLayout, QGroupBox, QPlainTextEdit)

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

import warnings
warnings.filterwarnings("ignore")

#::--------------------------------
# Deafault font size for all the windows
#::--------------------------------
font_size_window = 'font-size:15px'


class App(QMainWindow):
    #::-------------------------------------------------------
    # This class creates all the elements of the application
    #::-------------------------------------------------------
    send_fig = pyqtSignal(str)

    def __init__(self):
        super(App, self).__init__()
        self.Title = "Stack Overflow Search Engine"
        self.initUi()

    def initUi(self):
        self.setWindowTitle(self.Title)
        self.setStyleSheet(font_size_window)

        self.main_widget = QWidget(self)
        self.layout = QGridLayout(self.main_widget)

        self.labelImage = QLabel(self)
        self.pixmap = QPixmap('assets/img/titleImage.png')
        self.labelImage.setPixmap(self.pixmap)
        self.labelImage.adjustSize()

        self.setFixedSize(self.pixmap.width(), 900)

        self.groupBoxImage = QGroupBox()
        self.groupBoxImageLayout = QVBoxLayout()
        self.groupBoxImage.setLayout(self.groupBoxImageLayout)
        self.groupBoxImageLayout.addWidget(self.labelImage,alignment=Qt.AlignCenter)

        self.inputSearch = QPlainTextEdit(self)

        self.btnSearch = QPushButton("Search")
        self.btnSearch.clicked.connect(self.update)

        self.groupBoxSearch = QGroupBox('ENTER SEARCH QUERY')
        self.groupBoxSearchLayout = QGridLayout()  # Grid
        self.groupBoxSearch.setLayout(self.groupBoxSearchLayout)
        self.groupBoxSearchLayout.addWidget(self.inputSearch, 0, 0, 11, 1)
        self.groupBoxSearchLayout.addWidget(self.btnSearch, 11, 0, 2, 1)


        self.result1Text1 = QLabel()
        self.result1Text2 = QLabel()
        self.result1Text2.setMaximumWidth(70)
        self.result1Text3 = QLabel()
        self.result1Text4 = QLabel()
        self.result1Text4.setMaximumWidth(70)
        self.groupBoxResult1 = QGroupBox('# 1')
        self.groupBoxResult1Layout = QGridLayout()  # Grid
        self.groupBoxResult1.setLayout(self.groupBoxResult1Layout)
        self.groupBoxResult1Layout.addWidget(QLabel("Question:"), 0, 0, 1, 1)
        self.groupBoxResult1Layout.addWidget(self.result1Text1, 0, 1, 1, 8)
        self.groupBoxResult1Layout.addWidget(QLabel("    Votes:"), 0, 9, 1, 1)
        self.groupBoxResult1Layout.addWidget(self.result1Text2, 0, 10, 1, 1)
        self.groupBoxResult1Layout.addWidget(QLabel("URL:"), 1, 0, 1, 1)
        self.groupBoxResult1Layout.addWidget(self.result1Text3, 1, 1, 1, 8)
        self.groupBoxResult1Layout.addWidget(QLabel("    S. I. :"), 1, 9, 1, 1)
        self.groupBoxResult1Layout.addWidget(self.result1Text4, 1, 10, 1, 1)

        self.result2Text1 = QLabel()
        self.result2Text2 = QLabel()
        self.result2Text2.setMaximumWidth(70)
        self.result2Text3 = QLabel()
        self.result2Text4 = QLabel()
        self.result2Text4.setMaximumWidth(70)
        self.groupBoxResult2 = QGroupBox('# 2')
        self.groupBoxResult2Layout = QGridLayout()  # Grid
        self.groupBoxResult2.setLayout(self.groupBoxResult2Layout)
        self.groupBoxResult2Layout.addWidget(QLabel("Question:"), 0, 0, 1, 1)
        self.groupBoxResult2Layout.addWidget(self.result2Text1, 0, 1, 1, 8)
        self.groupBoxResult2Layout.addWidget(QLabel("    Votes:"), 0, 9, 1, 1)
        self.groupBoxResult2Layout.addWidget(self.result2Text2, 0, 10, 1, 1)
        self.groupBoxResult2Layout.addWidget(QLabel("URL:"), 1, 0, 1, 1)
        self.groupBoxResult2Layout.addWidget(self.result2Text3, 1, 1, 1, 8)
        self.groupBoxResult2Layout.addWidget(QLabel("    S. I. :"), 1, 9, 1, 1)
        self.groupBoxResult2Layout.addWidget(self.result2Text4, 1, 10, 1, 1)

        self.result3Text1 = QLabel()
        self.result3Text2 = QLabel()
        self.result3Text2.setMaximumWidth(70)
        self.result3Text3 = QLabel()
        self.result3Text4 = QLabel()
        self.result3Text4.setMaximumWidth(70)
        self.groupBoxResult3 = QGroupBox('# 3')
        self.groupBoxResult3Layout = QGridLayout()  # Grid
        self.groupBoxResult3.setLayout(self.groupBoxResult3Layout)
        self.groupBoxResult3Layout.addWidget(QLabel("Question:"), 0, 0, 1, 1)
        self.groupBoxResult3Layout.addWidget(self.result3Text1, 0, 1, 1, 8)
        self.groupBoxResult3Layout.addWidget(QLabel("    Votes:"), 0, 9, 1, 1)
        self.groupBoxResult3Layout.addWidget(self.result3Text2, 0, 10, 1, 1)
        self.groupBoxResult3Layout.addWidget(QLabel("URL:"), 1, 0, 1, 1)
        self.groupBoxResult3Layout.addWidget(self.result3Text3, 1, 1, 1, 8)
        self.groupBoxResult3Layout.addWidget(QLabel("    S. I. :"), 1, 9, 1, 1)
        self.groupBoxResult3Layout.addWidget(self.result3Text4, 1, 10, 1, 1)

        self.result4Text1 = QLabel()
        self.result4Text2 = QLabel()
        self.result4Text2.setMaximumWidth(70)
        self.result4Text3 = QLabel()
        self.result4Text4 = QLabel()
        self.result4Text4.setMaximumWidth(70)
        self.groupBoxResult4 = QGroupBox('# 4')
        self.groupBoxResult4Layout = QGridLayout()  # Grid
        self.groupBoxResult4.setLayout(self.groupBoxResult4Layout)
        self.groupBoxResult4Layout.addWidget(QLabel("Question:"), 0, 0, 1, 1)
        self.groupBoxResult4Layout.addWidget(self.result4Text1, 0, 1, 1, 8)
        self.groupBoxResult4Layout.addWidget(QLabel("    Votes:"), 0, 9, 1, 1)
        self.groupBoxResult4Layout.addWidget(self.result4Text2, 0, 10, 1, 1)
        self.groupBoxResult4Layout.addWidget(QLabel("URL:"), 1, 0, 1, 1)
        self.groupBoxResult4Layout.addWidget(self.result4Text3, 1, 1, 1, 8)
        self.groupBoxResult4Layout.addWidget(QLabel("    S. I. :"), 1, 9, 1, 1)
        self.groupBoxResult4Layout.addWidget(self.result4Text4, 1, 10, 1, 1)

        self.result5Text1 = QLabel()
        self.result5Text2 = QLabel()
        self.result5Text2.setMaximumWidth(70)
        self.result5Text3 = QLabel()
        self.result5Text4 = QLabel()
        self.result5Text4.setMaximumWidth(70)
        self.groupBoxResult5 = QGroupBox('# 5')
        self.groupBoxResult5Layout = QGridLayout()  # Grid
        self.groupBoxResult5.setLayout(self.groupBoxResult5Layout)
        self.groupBoxResult5Layout.addWidget(QLabel("Question:"), 0, 0, 1, 1)
        self.groupBoxResult5Layout.addWidget(self.result5Text1, 0, 1, 1, 8)
        self.groupBoxResult5Layout.addWidget(QLabel("    Votes:"), 0, 9, 1, 1)
        self.groupBoxResult5Layout.addWidget(self.result5Text2, 0, 10, 1, 1)
        self.groupBoxResult5Layout.addWidget(QLabel("URL:"), 1, 0, 1, 1)
        self.groupBoxResult5Layout.addWidget(self.result5Text3, 1, 1, 1, 8)
        self.groupBoxResult5Layout.addWidget(QLabel("    S. I. :"), 1, 9, 1, 1)
        self.groupBoxResult5Layout.addWidget(self.result5Text4, 1, 10, 1, 1)

        self.groupBoxResults=QGroupBox('RESULTS')
        self.groupBoxResultsLayout = QVBoxLayout()
        self.groupBoxResults.setLayout(self.groupBoxResultsLayout)
        self.groupBoxResultsLayout.addWidget(self.groupBoxResult1)
        self.groupBoxResultsLayout.addWidget(self.groupBoxResult2)
        self.groupBoxResultsLayout.addWidget(self.groupBoxResult3)
        self.groupBoxResultsLayout.addWidget(self.groupBoxResult4)
        self.groupBoxResultsLayout.addWidget(self.groupBoxResult5)
        self.groupBoxResults.setEnabled(False)

        self.layout.addWidget(self.groupBoxImage, 0, 0, 11, 14)
        self.layout.addWidget(QLabel(""), 11, 0, 1, 14)
        self.layout.addWidget(self.groupBoxSearch, 12, 0, 15, 3)
        self.layout.addWidget(self.groupBoxResults, 12, 3, 15, 11)

        self.setCentralWidget(self.main_widget)
        self.show()


    def update(self):
        searchQuery = str(self.inputSearch.toPlainText())

        results=searchEngine.showResults(searchQuery)
        self.groupBoxResults.setEnabled(True)

        self.result1Text1.setText(results["Questions"][0])
        self.result1Text2.setText(str(results["Votes"][0]))
        self.result1Text3.setText(results["Web URL"][0])
        self.result1Text3.setOpenExternalLinks(True)
        self.result1Text4.setText(str(round(results["S.I."][0],2)))

        self.result2Text1.setText(results["Questions"][1])
        self.result2Text2.setText(str(results["Votes"][1]))
        self.result2Text3.setText(results["Web URL"][1])
        self.result2Text3.setOpenExternalLinks(True)
        self.result2Text4.setText(str(round(results["S.I."][1],2)))

        self.result3Text1.setText(results["Questions"][2])
        self.result3Text2.setText(str(results["Votes"][2]))
        self.result3Text3.setText(results["Web URL"][2])
        self.result3Text3.setOpenExternalLinks(True)
        self.result3Text4.setText(str(round(results["S.I."][2],2)))

        self.result4Text1.setText(results["Questions"][3])
        self.result4Text2.setText(str(results["Votes"][3]))
        self.result4Text3.setText(results["Web URL"][3])
        self.result4Text3.setOpenExternalLinks(True)
        self.result4Text4.setText(str(round(results["S.I."][3],2)))

        self.result5Text1.setText(results["Questions"][4])
        self.result5Text2.setText(str(results["Votes"][4]))
        self.result5Text3.setText(results["Web URL"][4])
        self.result5Text3.setOpenExternalLinks(True)
        self.result5Text4.setText(str(round(results["S.I."][4],2)))


def main():
    #::-------------------------------------------------
    # Initiates the application
    #::-------------------------------------------------
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = App()
    ex.show()
    ex.showMaximized()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()