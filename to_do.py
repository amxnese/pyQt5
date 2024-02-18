from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

# Connect to an existing database or create a new one
conn = sqlite3.connect('to_do.db')
# Create a cursor object
cr = conn.cursor()
# Creating a Table
cr.execute('''CREATE TABLE IF NOT EXISTS items(
    item TEXT
)''')
# Commiting Changes And Closing DB
conn.commit()
conn.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 374)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add_pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.add_it())
        self.add_pushButton.setGeometry(QtCore.QRect(10, 36, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.add_pushButton.setFont(font)
        self.add_pushButton.setStyleSheet("background-color: #efefef")
        self.add_pushButton.setObjectName("add_pushButton")
        self.remove_pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.remove_it())
        self.remove_pushButton_2.setGeometry(QtCore.QRect(170, 36, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.remove_pushButton_2.setFont(font)
        self.remove_pushButton_2.setStyleSheet("background-color: #efefef")
        self.remove_pushButton_2.setObjectName("remove_pushButton_2")
        self.clear_pushButton_3 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.clear_it())
        self.clear_pushButton_3.setGeometry(QtCore.QRect(330, 36, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.clear_pushButton_3.setFont(font)
        self.clear_pushButton_3.setStyleSheet("background-color: #efefef")
        self.clear_pushButton_3.setObjectName("clear_pushButton_3")
        self.my_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.my_listWidget.setGeometry(QtCore.QRect(10, 81, 591, 241))
        self.my_listWidget.setObjectName("my_listWidget")
        self.type_here_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.type_here_lineEdit.setGeometry(QtCore.QRect(10, 0, 591, 34))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.type_here_lineEdit.setFont(font)
        self.type_here_lineEdit.setObjectName("type_here_lineEdit")
        self.add_to_db_pushButton_4 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.save_it())
        self.add_to_db_pushButton_4.setGeometry(QtCore.QRect(470, 36, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.add_to_db_pushButton_4.setFont(font)
        self.add_to_db_pushButton_4.setStyleSheet("background-color: #efefef")
        self.add_to_db_pushButton_4.setObjectName("add_to_db_pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Grabing all The Items That are in The DB
        self.grab_all()

    # Handling The Grab All Func
    def grab_all(self):
        # Connect to an existing database or create a new one
        conn = sqlite3.connect('to_do.db')
        # Create a cursor object
        cr = conn.cursor()
        # Fetching all Items
        cr.execute('SELECT * FROM items')
        items = cr.fetchall()
        # Commting And Closing DB
        conn.commit()
        conn.close()
        # Looping Through Items 
        for item in items:
            self.my_listWidget.addItem(item[0])

    # Handling The Add Item Button
    def add_it(self):
        # Grabbing What is Typed in The lineEdit
        item = self.type_here_lineEdit.text()
        # Checking if it's a Valid Item
        if not item: return
        # Adding The Item To listWidet
        self.my_listWidget.addItem(item)
        # Clearing The lineEdit
        self.type_here_lineEdit.clear()

    # Handling The Remove Item Button
    def remove_it(self):
        # Getting The Index of The Selected Item
        selected = self.my_listWidget.currentRow()
        # Passing The Index To The TakeItem() Func To Remove It From The listWidget
        self.my_listWidget.takeItem(selected)

    # Handling The Clear Button
    def clear_it(self):
        self.my_listWidget.clear()

    # Handling The Save To DataBase Button
    def save_it(self):
        # Connect to an existing database or create a new one
        conn = sqlite3.connect('to_do.db')
        # Create a cursor object
        cr = conn.cursor()
        # Clearing The DataBasa
        cr.execute('DELETE FROM items;',)
        # Declaring The List Which Going To Contain Our Items
        my_items = []
        # Looping Through Each Item in The listWidget and Appending it To Our List
        for i in range(self.my_listWidget.count()):
            my_items.append(self.my_listWidget.item(i).text())
        for item in my_items:
            # Adding Items To DB
            cr.execute('INSERT INTO items VALUES (:item)',
            {
                'item' : item,
            })
        
        # Commting And Closing DB
        conn.commit()
        conn.close()

        # pop up Box
        msg = QMessageBox()
        msg.setWindowTitle("Saved")
        msg.setText("Your Items Has Been Saved To The DataBase")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_pushButton.setText(_translate("MainWindow", "Add Item"))
        self.remove_pushButton_2.setText(_translate("MainWindow", "Remove Item"))
        self.clear_pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.type_here_lineEdit.setPlaceholderText(_translate("MainWindow", "Type Here"))
        self.add_to_db_pushButton_4.setText(_translate("MainWindow", "Add To DB"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
