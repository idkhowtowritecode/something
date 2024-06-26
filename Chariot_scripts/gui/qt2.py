import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QFormLayout, QLineEdit, QPushButton, 
                             QComboBox, QCheckBox, QTabWidget, QLabel)
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
        layout = QFormLayout()

        self.add_test = QLineEdit()
        self.script_dir = QPushButton("SELECT")
        self.pairs = QLineEdit()
        self.protocol = QComboBox()
        self.protocol.addItems(["TCP/UDP"])

        self.e1 = IPInputWidget()
        self.e2 = IPInputWidget()
        self.m1 = IPInputWidget()
        self.m2 = IPInputWidget()

        self.duration = QLineEdit()
        self.add_button = QPushButton("ADD")

        layout.addRow("Add test", self.add_test)
        layout.addRow("Script Dir", self.script_dir)
        layout.addRow("Pairs", self.pairs)
        layout.addRow("Protocol", self.protocol)
        layout.addRow("E1 (ipv4)", self.e1)
        layout.addRow("E2 (ipv4)", self.e2)
        layout.addRow("M1 (*opt)", self.m1)
        layout.addRow("M2 (*opt)", self.m2)
        layout.addRow("Duration", self.duration)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

class TSTRunner(QWidget):
    def __init__(self):
        super().__init__()
        layout = QFormLayout()
        
        self.run_test = QPushButton("SELECT")
        self.save_as = QLineEdit()
        self.export_pdf = QCheckBox("Export pdf")
        self.repeat = QLineEdit()
        self.submit_button = QPushButton("Submit")

        layout.addRow("Run test", self.run_test)
        layout.addRow("Save as", self.save_as)
        layout.addRow(self.export_pdf)
        layout.addRow("Repeat", self.repeat)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

class TSTScheduler(QWidget):
    def __init__(self):
        super().__init__()
        layout = QFormLayout()

        self.run_test1 = QPushButton("SELECT")
        self.save_as1 = QLineEdit()
        self.run_test2 = QPushButton("SELECT")
        self.save_as2 = QLineEdit()
        self.run_test3 = QPushButton("SELECT")
        self.save_as3 = QLineEdit()
        self.submit_button = QPushButton("Submit")

        layout.addRow("Run test1", self.run_test1)
        layout.addRow("Save as", self.save_as1)
        layout.addRow("Run test2", self.run_test2)
        layout.addRow("Save as", self.save_as2)
        layout.addRow("Run test3", self.run_test3)
        layout.addRow("Save as", self.save_as3)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

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
