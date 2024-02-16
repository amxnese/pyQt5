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
    my_combo = qtw.QComboBox(editable=True, insertPolicy=qtw.QComboBox.InsertAtTop)

    # Adding Items To The Combo Box
    my_combo.addItem("Python")
    my_combo.addItem("C++")
    my_combo.addItem("C")
    my_combo.addItem("Java")
    my_combo.addItem("JavaScript")
    my_combo.addItem("Rust")
    lst = ["Python", "C++", "C", "JavaScript", "Rust"]

    # Setting The Combo Box Font 
    my_combo.setFont(qtg.QFont("helvetica", 20))

    # Adding The Combo Widget To The Layout
    self.layout().addWidget(my_combo)

    # Setting a Button For The Combo Widget
    combo_button = qtw.QPushButton("Confirm", clicked= lambda : combo_press())
    def combo_press():
      # Doing Something in The Label Based On The currentText Chosen
      if my_combo.currentText() == "Java":
        label.setText("Come On, Really!!")
      elif my_combo.currentText() in lst:
        label.setText(f"You Know Your Stuff Don't You :)")
      else:
        label.setText(f"You Have Chosen {my_combo.currentText()}")
    # Setting The Button Font
    combo_button.setFont(qtg.QFont("helvetica", 15))
    # Adding The Button Wiget To The Layout
    self.layout().addWidget(combo_button)  

    # Setting a Spin Box
    my_spin = qtw.QSpinBox(
      value=10, 
      maximum=25, 
      minimum=0, 
      singleStep=1,
      prefix="I Have ",
      suffix=" Years of Experience")
    my_spin.setFont(qtg.QFont("helvetica", 15))
    # Adding The Spin Box To The Layout
    self.layout().addWidget(my_spin)

    # Setting a Button For The Spin Box
    spin_button = qtw.QPushButton("Confirm", clicked=lambda: spin_press())
    def spin_press():
      if my_spin.value() <= 3:
        label.setText(f"You Are an Entry Level Devoloper")
      elif my_spin.value() <= 5:
        label.setText("You Are a Junior Developer")
      elif my_spin.value() <= 8:
        label.setText("You Are an Intermediate Developer")
      else:
        label.setText("You Are a Senior Developer")

    
    # Setting The Spin Button Font
    spin_button.setFont(qtg.QFont("helvetica", 15))

    # Adding The Spin Button Widget To The Layout
    self.layout().addWidget(spin_button)

    # Create a Text Box
    my_text = qtw.QTextEdit(
      lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
      lineWrapColumnOrWidth=69,
      placeholderText="Type Here",
      readOnly=False,
      acceptRichText=False,
      plainText="hi"
    )

    # Setting The Text Box Font
    my_text.setFont(qtg.QFont("helvetica", 15))

    # Adding The TextBox Widget To The Layout
    self.layout().addWidget(my_text)

    # Setting a Button For The TextBox
    my_text_button = qtw.QPushButton("Confirm", clicked=lambda: text_press())

    # Defining The text_press Function
    def text_press():
      label.setText(my_text.toPlainText())
      splitted = my_text.toPlainText().split()
      word = "Word" if len(splitted) == 1 else "Words"
      my_text.setPlainText(f"You Typed {len(splitted)} {word}")
      
    # Setting The TextBox Button Font
    my_text_button.setFont(qtg.QFont("helvetica", 15))

    # Adding The TextBox Button Widget To The Layout
    self.layout().addWidget(my_text_button)

    # Showing My App
    self.show()

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()