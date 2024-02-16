import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
  def __init__(self):
    super().__init__()
    # Add a Title
    self.setWindowTitle("My Project 1")

    # Set Form Layout
    form_layout = qtw.QFormLayout()
    self.setLayout(form_layout)

    # Creating Widgets
    label = qtw.QLabel("Fill in The Forms Below")
    label.setFont(qtg.QFont("helvetica", 24))
    f_name = qtw.QLineEdit()
    f_name.setFont(qtg.QFont("helvetica", 15))
    l_name = qtw.QLineEdit()
    l_name.setFont(qtg.QFont("helvetica", 15))

    # Adding Widgets To The Layout
    form_layout.addRow(label)
    form_layout.addRow("First Name", f_name)
    form_layout.addRow("Last Name", l_name)
    form_layout.addRow(qtw.QPushButton("Confirm", clicked=lambda:press_it()))
    
    # Defining The press_it Function
    def press_it():
      # Removing The label Widget
      form_layout.removeWidget(label)
      label.deleteLater()
      # Creating a New Widget To Welcome The User
      label1 = qtw.QLabel(f"Welcome To The App {f_name.text()} {l_name.text()}")
      label1.setFont(qtg.QFont("helvetica", 20))
      form_layout.addRow(label1)

    # Showing App
    self.show()

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()