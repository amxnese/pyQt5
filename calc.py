from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(243, 368)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(20, 10, 201, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.outputLabel.setFont(font)
        self.outputLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.outputLabel.setMouseTracking(False)
        self.outputLabel.setTabletTracking(False)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setMidLineWidth(0)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setIndent(-1)
        self.outputLabel.setObjectName("outputLabel")
        self.seven_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.press_it("7"))
        self.seven_button.setGeometry(QtCore.QRect(20, 110, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.seven_button.setFont(font)
        self.seven_button.setStyleSheet("background-color: #efefef")
        self.seven_button.setObjectName("seven_button")
        self.four_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.press_it("4"))
        self.four_button.setGeometry(QtCore.QRect(20, 160, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.four_button.setFont(font)
        self.four_button.setStyleSheet("background-color: #efefef")
        self.four_button.setObjectName("four_button")
        self.one_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.press_it("1"))
        self.one_button.setGeometry(QtCore.QRect(20, 210, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.one_button.setFont(font)
        self.one_button.setStyleSheet("background-color: #efefef")
        self.one_button.setObjectName("one_button")
        self.plus_minus_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.sign_it())
        self.plus_minus_button.setGeometry(QtCore.QRect(20, 260, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.plus_minus_button.setFont(font)
        self.plus_minus_button.setStyleSheet("background-color: #efefef")
        self.plus_minus_button.setObjectName("plus_minus_button")
        self.percent_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.press_it("%"))
        self.percent_button.setGeometry(QtCore.QRect(20, 60, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.percent_button.setFont(font)
        self.percent_button.setStyleSheet("background-color: #efefef")
        self.percent_button.setObjectName("percent_button")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.clear_it())
        self.clear_button.setGeometry(QtCore.QRect(70, 60, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.clear_button.setFont(font)
        self.clear_button.setStyleSheet("background-color: #efefef")
        self.clear_button.setObjectName("clear_button")
        self.eight_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.press_it("8"))
        self.eight_button.setGeometry(QtCore.QRect(70, 110, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.eight_button.setFont(font)
        self.eight_button.setStyleSheet("background-color: #efefef")
        self.eight_button.setObjectName("eight_button")
        self.five_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.press_it("5"))
        self.five_button.setGeometry(QtCore.QRect(70, 160, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.five_button.setFont(font)
        self.five_button.setStyleSheet("background-color: #efefef")
        self.five_button.setObjectName("five_button")
        self.two_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.press_it("2"))
        self.two_button.setGeometry(QtCore.QRect(70, 210, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.two_button.setFont(font)
        self.two_button.setStyleSheet("background-color: #efefef")
        self.two_button.setObjectName("two_button")
        self.zero_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.press_it("0"))
        self.zero_button.setGeometry(QtCore.QRect(70, 260, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.zero_button.setFont(font)
        self.zero_button.setStyleSheet("background-color: #efefef")
        self.zero_button.setObjectName("zero_button")
        self.arrow_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.remove_it())
        self.arrow_button.setGeometry(QtCore.QRect(120, 60, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.arrow_button.setFont(font)
        self.arrow_button.setStyleSheet("background-color: #efefef")
        self.arrow_button.setObjectName("arrow_button")
        self.div_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.press_it("/"))
        self.div_button.setGeometry(QtCore.QRect(170, 60, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.div_button.setFont(font)
        self.div_button.setStyleSheet("background-color: #efefef")
        self.div_button.setObjectName("div_button")
        self.six_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.press_it("6"))
        self.six_button.setGeometry(QtCore.QRect(120, 160, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.six_button.setFont(font)
        self.six_button.setStyleSheet("background-color: #efefef")
        self.six_button.setObjectName("six_button")
        self.three_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.press_it("3"))
        self.three_button.setGeometry(QtCore.QRect(120, 210, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.three_button.setFont(font)
        self.three_button.setStyleSheet("background-color: #efefef")
        self.three_button.setObjectName("three_button")
        self.point_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.dot_it())
        self.point_button.setGeometry(QtCore.QRect(120, 260, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.point_button.setFont(font)
        self.point_button.setStyleSheet("background-color: #efefef")
        self.point_button.setObjectName("point_button")
        self.nine_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.press_it("9"))
        self.nine_button.setGeometry(QtCore.QRect(120, 110, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.nine_button.setFont(font)
        self.nine_button.setStyleSheet("background-color: #efefef")
        self.nine_button.setObjectName("nine_button")
        self.mul_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.press_it("x"))
        self.mul_button.setGeometry(QtCore.QRect(170, 110, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.mul_button.setFont(font)
        self.mul_button.setStyleSheet("background-color: #efefef")
        self.mul_button.setObjectName("mul_button")
        self.sub_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.press_it("-"))
        self.sub_button.setGeometry(QtCore.QRect(170, 160, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.sub_button.setFont(font)
        self.sub_button.setStyleSheet("background-color: #efefef")
        self.sub_button.setObjectName("sub_button")
        self.add_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.press_it("+"))
        self.add_button.setGeometry(QtCore.QRect(170, 210, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.add_button.setFont(font)
        self.add_button.setStyleSheet("background-color: #efefef")
        self.add_button.setObjectName("add_button")
        self.assign_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.assign_it())
        self.assign_button.setGeometry(QtCore.QRect(170, 260, 51, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.assign_button.setFont(font)
        self.assign_button.setStyleSheet("background-color: #efefef")
        self.assign_button.setObjectName("assign_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 243, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Handling The "-/+" Button
    def sign_it(self):
        if self.outputLabel.text()[0] == '-':
            self.outputLabel.setText(f"{self.outputLabel.text()[1:]}")
        else:
            self.outputLabel.setText(f"-{self.outputLabel.text()}")
        
    # Handling Some Buttons With One Function
    def press_it(self, pressed):
        # Removing The Leading Zero And The Error Output From The Output Label
        self.outputLabel.setText("") if self.outputLabel.text() == "0" or self.outputLabel.text() == "Error" else ""
        # Adding The Pressed Button To The Previous Output Label
        self.outputLabel.setText(f"{self.outputLabel.text()}{pressed}")
    
    # Handling The "C" Button
    def clear_it(self):
        # Clearing Both The Output Label And The Equation List
        self.outputLabel.setText("0")

    # Handling The ">>" Button
    def remove_it(self):
        # Removing The Last Item From The Output Label
        self.outputLabel.setText( self.outputLabel.text()[:-1])

    # Handling The "." Button
    def dot_it(self):
            # Declaring The Variable last To Store The Last Longest Valid Number From The Output Label
            last = ""
            # Starting From The End
            for i in range(len(self.outputLabel.text())-1, 0, -1):
                last += self.outputLabel[i]
                ops = ["-", "+", "*", "/"]
                # Checking if We Hit an Operation So We Can Stop
                if last[-1] in ops:
                    break
            # Checking if The Number We Got Hasn't a Point So We Can Gime Him One
            if "." not in last:
                self.outputLabel.setText(f"{self.outputLabel.text()}.")

    # Handling The "=" Button
    def assign_it(self):
        try:
            # Replacing The 'x' With '*' So We Can Evaluate It
            eq = self.outputLabel.text().replace('x', '*')
            self.outputLabel.setText(str(eval(eq)))
        except:
            self.outputLabel.setText("Error")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.seven_button.setText(_translate("MainWindow", "7"))
        self.four_button.setText(_translate("MainWindow", "4"))
        self.one_button.setText(_translate("MainWindow", "1"))
        self.plus_minus_button.setText(_translate("MainWindow", "+/-"))
        self.percent_button.setText(_translate("MainWindow", "%"))
        self.clear_button.setText(_translate("MainWindow", "C"))
        self.eight_button.setText(_translate("MainWindow", "8"))
        self.five_button.setText(_translate("MainWindow", "5"))
        self.two_button.setText(_translate("MainWindow", "2"))
        self.zero_button.setText(_translate("MainWindow", "0"))
        self.arrow_button.setText(_translate("MainWindow", "<<"))
        self.div_button.setText(_translate("MainWindow", "/"))
        self.six_button.setText(_translate("MainWindow", "6"))
        self.three_button.setText(_translate("MainWindow", "3"))
        self.point_button.setText(_translate("MainWindow", "."))
        self.nine_button.setText(_translate("MainWindow", "9"))
        self.mul_button.setText(_translate("MainWindow", "x"))
        self.sub_button.setText(_translate("MainWindow", "-"))
        self.add_button.setText(_translate("MainWindow", "+"))
        self.assign_button.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
