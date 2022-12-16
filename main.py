import hashlib
import string
import random
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.l = 0
        self.u = 0
        self.d = 0
        self.p = 0
        self.k = 0
        self.z = 0
        self.length = random.randint(8, 16)
        self.chars = '@$_!%*#?&'
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(19, 154, 145);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkpasswd_btn = QtWidgets.QPushButton(self.centralwidget)
        self.checkpasswd_btn.setGeometry(QtCore.QRect(510, 140, 151, 31))
        self.checkpasswd_btn.setStyleSheet("background-color: rgb(24, 189, 176);\n"
"font: 63 13pt \"Montserrat\";\n"
"color: rgb(255, 255, 255);")
        self.checkpasswd_btn.setObjectName("checkpasswd_btn")
        self.generatepasswd_btn = QtWidgets.QPushButton(self.centralwidget)
        self.generatepasswd_btn.setGeometry(QtCore.QRect(300, 450, 181, 31))
        self.generatepasswd_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 13pt \"Montserrat\";\n"
"background-color: rgb(24, 189, 176);")
        self.generatepasswd_btn.setObjectName("generatepasswd_btn")
        self.mainlabel = QtWidgets.QLabel(self.centralwidget)
        self.mainlabel.setGeometry(QtCore.QRect(90, 70, 681, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.mainlabel.setFont(font)
        self.mainlabel.setStyleSheet("color: rgb(255, 255,255);\n"
"font: 75 36pt \"Montserrat\";")
        self.mainlabel.setObjectName("mainlabel")
        self.generatedpasswd = QtWidgets.QLabel(self.centralwidget)
        self.generatedpasswd.setGeometry(QtCore.QRect(300, 500, 301, 21))
        self.generatedpasswd.setText("")
        self.generatedpasswd.setObjectName("generatedpasswd")
        self.enterpasswd = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.enterpasswd.setGeometry(QtCore.QRect(190, 140, 321, 31))
        self.enterpasswd.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.enterpasswd.setObjectName("enterpasswd")
        self.enterfile_btn = QtWidgets.QPushButton(self.centralwidget)
        self.enterfile_btn.setGeometry(QtCore.QRect(280, 330, 151, 32))
        self.enterfile_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 13pt \"Montserrat\";\n"
"background-color: rgb(24, 189, 176);")
        self.enterfile_btn.setObjectName("enterfile_btn")
        self.passwd_answer = QtWidgets.QLabel(self.centralwidget)
        self.passwd_answer.setGeometry(QtCore.QRect(190, 190, 411, 21))
        self.passwd_answer.setText("")
        self.passwd_answer.setObjectName("passwd_answer")
        self.enterfile = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.enterfile.setGeometry(QtCore.QRect(190, 290, 321, 31))
        self.enterfile.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "color: rgb(0, 0, 0);")
        self.enterfile.setObjectName("enterfile")
        self.checkfile_btn = QtWidgets.QPushButton(self.centralwidget)
        self.checkfile_btn.setGeometry(QtCore.QRect(510, 290, 201, 31))
        self.checkfile_btn.setStyleSheet("background-color: rgb(24, 189, 176);\n"
"font: 63 13pt \"Montserrat\";\n"
"color: rgb(255, 255, 255);")
        self.checkfile_btn.setObjectName("checkfile_btn")
        self.file_answer = QtWidgets.QLabel(self.centralwidget)
        self.file_answer.setGeometry(QtCore.QRect(190, 390, 411, 21))
        self.file_answer.setText("")
        self.file_answer.setObjectName("file_answer")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.addfunctions()
    def addfunctions(self):
        self.generatepasswd_btn.clicked.connect(lambda: self.generatepw())
        self.enterfile_btn.clicked.connect(lambda: self.openfile())
        self.checkfile_btn.clicked.connect(lambda: self.check())
        self.checkpasswd_btn.clicked.connect(lambda: self.checkpasswd())

    def checkpasswd(self):
        s = self.enterpasswd.toPlainText()
        if not s:
            print('nothing')
            return
        s = self.func(s)
        if self.z != 1:
            self.passwd_answer.setText(s)
        else:
            self.passwd_answer.setText('В пароле присутствует(-ют) недопустимые символы')
            self.z = 0

    def check(self):
        try:
            file = self.enterfile.toPlainText()
            if file[len(file)-4:] == '.txt':
                self.enterfile.setPlainText(file)
                answer = open('checkedfile.txt', 'w')
                with open(file) as file:
                    for line in file:
                        s = line.rstrip()
                        a = self.func(s)
                        if self.z != 1:
                            answer.write(a + '\n')
                        else:
                            answer.write(a + ' В пароле присутствует(-ют) недопустимые символы' + '\n')
                            self.z = 0
                self.file_answer.setText('Результат сохранен в файл checkedfile.txt')
            else:
                self.file_answer.setText('Выбран неверный файл!')
        except FileNotFoundError:
            print('nothing')
    def openfile(self):
        fname = QFileDialog.getOpenFileName(None)[0]
        try:
            f = open(fname)
            f = str(f)
            f = f[25:-28]
            file = f
            if file[len(file)-4:] == '.txt':
                self.enterfile.setPlainText(file)
            else:
                self.file_answer.setText('Выбран неверный файл!')
        except FileNotFoundError:
            print('nothing')

    def func(self, s):
        for i in s:
            if i in [' ', '~', ',','.','^','"', '\'', '/','\\', '|','>','<',')','(']:
                self.z = 1
                return s
            if i.islower():
                self.l += 1
            if i.isupper():
                self.u += 1
            if i.isdigit():
                self.d += 1
            if i == '@' or i == '$' or i == '_' or i == '!' or i == '%' or i == '*' or i == '#' or i == '?' or i == '&':
                self.p += 1

        if self.l >= 1 and self.u >= 1 and self.d >= 1 and self.p >= 1 and len(s) >= 8 and s:
            with open('bad_pass.txt') as file:
                for line in file:
                    hash_object = hashlib.sha1(s.encode())
                    hex_dig = hash_object.hexdigest()
                    pos = line.find(':')
                    st1 = line[pos + 1:]
                    pos2 = st1.find(':')
                    st2_1 = st1[:pos2]
                    st2_2 = st1[pos2 + 1:].rstrip('\n')
                    if str(s) == str(st2_2) and str(st2_1) == str(hex_dig):
                        self.k = 1
            if self.k == 1:
                s = s + "  Скомпрометирован! Слабый пароль!"
                self.k = 0
                self.l = 0
                self.u = 0
                self.p = 0
                self.d = 0
                print(s)
                return s
            else:
                s = s + " Не скомпрометирован! Сильный пароль!"
                print(s)
                self.l = 0
                self.u = 0
                self.p = 0
                self.d = 0
                self.k = 0
                return s
        else:
                with open('bad_pass.txt') as file:
                    for line in file:
                        hash_object = hashlib.sha1(s.encode())
                        hex_dig = hash_object.hexdigest()
                        pos = line.find(':')
                        st1 = line[pos + 1:]
                        pos2 = st1.find(':')
                        st2_1 = st1[:pos2]
                        st2_2 = st1[pos2 + 1:].rstrip('\n')
                        if str(s) == str(st2_2) and str(st2_1) == str(hex_dig):
                            self.k = 1
                if self.k == 1:
                    s = s + " Скомпрометирован! Слабый пароль!"
                    print(s)
                    self.l = 0
                    self.u = 0
                    self.p = 0
                    self.d = 0
                    self.k = 0
                    return s
                else:
                    s = s + " Не скомпрометирован! Слабый пароль!"
                    print(s)
                    self.k = 0
                    self.l = 0
                    self.u = 0
                    self.p = 0
                    self.d = 0
                    return s

    def generatepw(self):
        letters = string.ascii_letters + string.digits + random.choice(self.chars)
        rand_string = ''.join(random.choice(letters) for i in range(self.length))
        for i in rand_string:
            if i.islower():
                self.l += 1
            if i.isupper():
                self.u += 1
            if i.isdigit():
                self.d += 1
            if i == '@' or i == '$' or i == '_' or i == '!' or i == '%' or i == '*' or i == '#' or i == '?' or i == '&':
                self.p += 1
        if self.l >= 1 and self.u >= 1 and self.d >= 1 and self.p >= 1:
            self.generatedpasswd.setText("Ваш безопасный пароль:" + rand_string)
            return rand_string
        else:
            self.l = 0
            self.u = 0
            self.d = 0
            self.p = 0
            self.k = 0
            self.z = 0
            self.generatepw()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Проверь свой пароль"))
        self.checkpasswd_btn.setText(_translate("MainWindow", "Проверить пароль"))
        self.generatepasswd_btn.setText(_translate("MainWindow", "Сгенерировать пароль"))
        self.mainlabel.setText(_translate("MainWindow", " Выберите, что вы хотите сделать:"))
        self.enterfile_btn.setText(_translate("MainWindow", " Выберите txt файл"))
        self.checkfile_btn.setText(_translate("MainWindow", "Проверить пароли из файла"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
