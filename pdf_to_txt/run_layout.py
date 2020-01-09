import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from main import main

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "pdf to text program ⚡️"
        self.left = 300
        self.top = 300
        self.width = 450
        self.height = 450
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(20, 20)
        self.textbox1.setPlaceholderText("insert forder path of input pdf files") 
        self.textbox1.resize(280,40)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(20, 80)
        self.textbox2.setPlaceholderText("insert forder path of output txt files") 
        self.textbox2.resize(280,40)

        self.button = QPushButton('convert 😀', self)
        self.button.move(20, 140)

        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue1 = self.textbox1.text()
        textboxValue2 = self.textbox2.text()
        main(textboxValue1, textboxValue2)
        QMessageBox.question(self, 'Message', 'convert Success! 😆', buttons = QMessageBox.Ok)
        self.textbox1.setText("")
        self.textbox2.setText("")
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    ex = App()
    sys.exit(app.exec_())
