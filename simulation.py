from gambler import Gamble

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(776, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 70, 71, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 131, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 190, 111, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 100, 181, 41))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 170, 201, 41))
        self.label_6.setObjectName("label_6")
        self.martcheck = QtWidgets.QCheckBox(self.centralwidget)
        self.martcheck.setGeometry(QtCore.QRect(310, 250, 181, 31))
        self.martcheck.setStyleSheet("font-size:12pt; \n"
"font-weight:600; \n"
"color:#9f9e9e;\n"
"align: center;")
        self.martcheck.setObjectName("martcheck")
        self.i_funds = QtWidgets.QLineEdit(self.centralwidget)
        self.i_funds.setGeometry(QtCore.QRect(190, 80, 113, 20))
        self.i_funds.setObjectName("i_funds")
        self.i_wager = QtWidgets.QLineEdit(self.centralwidget)
        self.i_wager.setGeometry(QtCore.QRect(190, 140, 113, 20))
        self.i_wager.setObjectName("i_wager")
        self.i_wagecount = QtWidgets.QLineEdit(self.centralwidget)
        self.i_wagecount.setGeometry(QtCore.QRect(190, 200, 113, 20))
        self.i_wagecount.setObjectName("i_wagecount")
        self.i_win = QtWidgets.QLineEdit(self.centralwidget)
        self.i_win.setGeometry(QtCore.QRect(630, 120, 113, 20))
        self.i_win.setObjectName("i_win")
        self.i_numsim = QtWidgets.QLineEdit(self.centralwidget)
        self.i_numsim.setGeometry(QtCore.QRect(630, 190, 113, 20))
        self.i_numsim.setObjectName("i_numsim")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 5, 561, 61))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 320, 161, 51))
        self.pushButton.setStyleSheet(".QPushButton {\n"
"  background: #3498db;\n"
"  background-image: -webkit-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -moz-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -ms-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -o-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: linear-gradient(to bottom, #3498db, #2980b9);\n"
"  -webkit-border-radius: 28;\n"
"  -moz-border-radius: 28;\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 20px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"  background: #3cb0fd;\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #3498db);\n"
"  text-decoration: none;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.driver())
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#9f9e9e;\">Funds </span><span style=\" font-size:12pt; font-weight:600; color:#9f9e9e; vertical-align:super;\">*</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#9f9e9e;\">Initial Wager </span><span style=\" font-size:12pt; font-weight:600; color:#9f9e9e; vertical-align:super;\">*</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#9f9e9e;\">Wage count </span><span style=\" font-size:12pt; font-weight:600; color:#9f9e9e; vertical-align:super;\">*</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#9f9e9e;\">Winning percentage</span></p><p align=\"center\"><span style=\" font-size:7pt; font-weight:600; color:#9f9e9e;\">default: 50%</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#9f9e9e;\">Number of simulation</span></p><p align=\"center\"><span style=\" font-size:7pt; font-weight:600; color:#9f9e9e;\">default: 1</span></p></body></html>"))
        self.martcheck.setText(_translate("MainWindow", "Martingale strategy"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Monte Carlo Simulation</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#949494;\">Graphical representation of results</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Simulate"))

    def driver(self):
        funds = int(self.i_funds.text())
        init_wager = int(self.i_wager.text())
        wager_count = int(self.i_wagecount.text())
        win_chance = 50
        num_sim = 1
        mstrategy = False
        if self.i_win.text():
            win_chance = int(self.i_win.text())
        if self.i_numsim.text():
            num_sim = int(self.i_numsim.text())
        if self.martcheck.isChecked():
            mstrategy = True
        print(funds,init_wager,wager_count,win_chance,num_sim,mstrategy)
        gamble = Gamble(funds,init_wager,wager_count,win_chance)
        gamble.run(num_sim,mstrategy)
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

