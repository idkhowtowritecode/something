import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QFormLayout, QLineEdit, QPushButton, 
                             QComboBox, QCheckBox, QTabWidget, QLabel, QFileDialog)
from PyQt5.QtGui import QIntValidator

class IPInputWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        self.part1 = QLineEdit()
        self.part1.setValidator(QIntValidator(0, 255))
        self.part1.setMaxLength(3)
        self.part1.setFixedWidth(40)
        
        self.part2 = QLineEdit()
        self.part2.setValidator(QIntValidator(0, 255))
        self.part2.setMaxLength(3)
        self.part2.setFixedWidth(40)
        
        self.part3 = QLineEdit()
        self.part3.setValidator(QIntValidator(0, 255))
        self.part3.setMaxLength(3)
        self.part3.setFixedWidth(40)
        
        self.part4 = QLineEdit()
        self.part4.setValidator(QIntValidator(0, 255))
        self.part4.setMaxLength(3)
        self.part4.setFixedWidth(40)
        
        layout.addWidget(self.part1)
        layout.addWidget(QLabel("."))
        layout.addWidget(self.part2)
        layout.addWidget(QLabel("."))
        layout.addWidget(self.part3)
        layout.addWidget(QLabel("."))
        layout.addWidget(self.part4)
        
        self.setLayout(layout)

    def get_ip(self):
        return f"{self.part1.text()}.{self.part2.text()}.{self.part3.text()}.{self.part4.text()}"

class TSTEditor(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        form_layout = QFormLayout()

        self.add_test = QLineEdit()
        self.script_dir = QPushButton("SELECT")
        self.script_dir.clicked.connect(self.select_script_dir)
        self.pairs = QLineEdit()
        self.protocol = QComboBox()
        self.protocol.addItems(["TCP", "UDP"])

        self.e1 = IPInputWidget()
        self.e2 = IPInputWidget()
        self.m1 = IPInputWidget()
        self.m2 = IPInputWidget()

        self.duration = QLineEdit()
        self.add_button = QPushButton("ADD")

        form_layout.addRow("Add test", self.add_test)
        form_layout.addRow("Script Dir", self.script_dir)
        form_layout.addRow("Pairs", self.pairs)
        form_layout.addRow("Protocol", self.protocol)
        form_layout.addRow("E1 (ipv4)", self.e1)
        form_layout.addRow("E2 (ipv4)", self.e2)
        form_layout.addRow("M1 (*opt)", self.m1)
        form_layout.addRow("M2 (*opt)", self.m2)
        form_layout.addRow("Duration", self.duration)
        
        layout.addLayout(form_layout)
        layout.addWidget(self.add_button)
        
        self.setLayout(layout)

    def select_script_dir(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Select Script Directory", "", "Source Files (*.src)", options=options)
        if file:
            self.script_dir.setText(file)

class TSTRunner(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        form_layout = QFormLayout()

        self.run_test = QPushButton("SELECT")
        self.run_test.clicked.connect(self.select_run_test)
        self.save_as = QLineEdit()
        self.export_pdf = QCheckBox("Export pdf")
        self.repeat = QLineEdit()
        self.submit_button = QPushButton("Submit")

        form_layout.addRow("Run test", self.run_test)
        form_layout.addRow("Save as", self.save_as)
        form_layout.addWidget(self.export_pdf)
        form_layout.addRow("Repeat", self.repeat)
        
        layout.addLayout(form_layout)
        layout.addWidget(self.submit_button)
        
        self.setLayout(layout)

    def select_run_test(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Select Test File", "", "Test Files (*.tst)", options=options)
        if file:
            self.run_test.setText(file)

class TSTScheduler(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        form_layout = QFormLayout()

        self.run_test1 = QPushButton("SELECT")
        self.run_test1.clicked.connect(lambda: self.select_test_file(self.run_test1))
        self.save_as1 = QLineEdit()
        self.run_test2 = QPushButton("SELECT")
        self.run_test2.clicked.connect(lambda: self.select_test_file(self.run_test2))
        self.save_as2 = QLineEdit()
        self.run_test3 = QPushButton("SELECT")
        self.run_test3.clicked.connect(lambda: self.select_test_file(self.run_test3))
        self.save_as3 = QLineEdit()
        self.submit_button = QPushButton("Submit")

        form_layout.addRow("Run test1", self.run_test1)
        form_layout.addRow("Save as", self.save_as1)
        form_layout.addRow("Run test2", self.run_test2)
        form_layout.addRow("Save as", self.save_as2)
        form_layout.addRow("Run test3", self.run_test3)
        form_layout.addRow("Save as", self.save_as3)
        
        layout.addLayout(form_layout)
        layout.addWidget(self.submit_button)
        
        self.setLayout(layout)

    def select_test_file(self, button):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Select Test File", "", "Test Files (*.tst)", options=options)
        if file:
            button.setText(file)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TST Application")

        tabs = QTabWidget()
        tabs.addTab(TSTEditor(), "TST Editor")
        tabs.addTab(TSTRunner(), "TST Runner")
        tabs.addTab(TSTScheduler(), "TST Scheduler")

        self.setCentralWidget(tabs)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
