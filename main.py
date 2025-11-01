from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
import sys
import os

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui",self)
        self.creatAccount.clicked.connect(self.show_register)
        self.btnLogin.clicked.connect(self.check_login)
        self.msg_box = QMessageBox()

    def back_to_login(self):
        Login.show()
        self.close()

    def show_register(self):
        register.show()
        self.close()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Main.ui",self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    register = Register()
    main = Main()
    login.show()
    app.exec()