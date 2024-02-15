import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
class MainWindow(qtw.QWidget): 
  def __init__(self):
    super().__init__()
    # Setting The Title of The Window
    self.setWindowTitle("My Project")

    # Setting a Vertical Layout
    self.setLayout(qtw.QVBoxLayout())
    # Setting Label
    label = qtw.QLabel("Hello Developer!! What's Your Favorite Language?")
    # Setting Label Font
    label.setFont(qtg.QFont("Helvetica", 20))
    self.layout().addWidget(label)

    '''
    # Setting an Entry Box
    entry = qtw.QLineEdit()
    entry.setObjectName("name_field")
    # entry.setText("Enter Your Name Here")
    self.layout().addWidget(entry)
    '''

    
    # Setting a Combo Box
    combo = qtw.QComboBox(editable=True, insertPolicy=qtw.QComboBox.InsertAtTop)

    # Adding Items To The Combo Box
    combo.addItem("Python")
    combo.addItem("C++")
    combo.addItem("C")
    combo.addItem("Java")
    combo.addItem("JavaScript")
    combo.addItem("Rust")
    lst = ["Python", "C++", "C", "JavaScript", "Rust"]

    # Setting The Combo Box Font 
    combo.setFont(qtg.QFont("helvetica", 20))

    # Adding The Combo Widget To The Layout
    self.layout().addWidget(combo)

    # Setting a Button For The Combo Widget
    combo_button = qtw.QPushButton("Confirm", clicked= lambda : combo_press())
    def combo_press():
      # Doing Something in The Label Based On The currentText Chosen
      if combo.currentText() == "Java":
        label.setText("Come On, Really!!")
      elif combo.currentText() in lst:
        label.setText(f"You Know Your Stuff Don't You :)")
      else:
        label.setText(f"You Have Chosen {combo.currentText()}")
    # Setting The Button Font
    combo_button.setFont(qtg.QFont("helvetica", 15))
    # Adding The Button Wiget To The Layout
    self.layout().addWidget(combo_button)  

    # Setting a Spin Box
    spin = qtw.QSpinBox(
      value=10, 
      maximum=25, 
      minimum=0, 
      singleStep=1,
      prefix="I Have ",
      suffix=" Years of Experience")
    spin.setFont(qtg.QFont("helvetica", 15))
    # Adding The Spin Box To The Layout
    self.layout().addWidget(spin)

    # Setting a Button For The Spin Box
    spin_button = qtw.QPushButton("Confirm", clicked=lambda: spin_press())
    def spin_press():
      if spin.value() <= 3:
        label.setText(f"You Are an Entry Level Devoloper")
      elif spin.value() <= 5:
        label.setText("You Are a Junior Developer")
      elif spin.value() <= 8:
        label.setText("You Are an Intermediate Developer")
      else:
        label.setText("You Are a Senior Developer")

    
    # Setting The Spin Button Font
    spin_button.setFont(qtg.QFont("helvetica", 15))

    # Adding The Spin Button Widget To The Layout
    self.layout().addWidget(spin_button)

    # Showing My App
    self.show()

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()