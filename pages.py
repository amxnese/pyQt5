import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QWidget, QVBoxLayout

class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.button = QPushButton("Go to Page 2")
        layout.addWidget(self.button)
        self.setLayout(layout)

class SecondPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.button = QPushButton("Go to Main Page")
        layout.addWidget(self.button)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()

        self.main_page = MainPage()
        self.second_page = SecondPage()

        self.stacked_widget.addWidget(self.main_page)
        self.stacked_widget.addWidget(self.second_page)

        # Connect buttons to change pages
        self.main_page.button.clicked.connect(self.goto_second_page)
        self.second_page.button.clicked.connect(self.goto_main_page)

        self.setCentralWidget(self.stacked_widget)

    def goto_second_page(self):
        self.stacked_widget.setCurrentWidget(self.second_page)

    def goto_main_page(self):
        self.stacked_widget.setCurrentWidget(self.main_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
