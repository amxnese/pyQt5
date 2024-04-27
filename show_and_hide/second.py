from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SecondWindow(object):
    def hide(self, window):
        window.hide()

    def show(self, window):
        window.show()

    def setupUi(self, SecondWindow, MainWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(420, 175)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.show_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.show(MainWindow))
        self.show_pushButton.setGeometry(QtCore.QRect(44, 40, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.show_pushButton.setFont(font)
        self.show_pushButton.setObjectName("show_pushButton")
        self.hide_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.hide(MainWindow))
        self.hide_pushButton.setGeometry(QtCore.QRect(210, 40, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hide_pushButton.setFont(font)
        self.hide_pushButton.setObjectName("hide_pushButton")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 22))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "SecondWindow"))
        self.show_pushButton.setText(_translate("SecondWindow", "show main"))
        self.hide_pushButton.setText(_translate("SecondWindow", "hide main"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())
