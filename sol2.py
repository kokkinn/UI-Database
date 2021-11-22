import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.Qt import Qt

from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget
import sqlite3


class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("C:\\Users\\kokki\\Desktop\\Solo\\new.ui", self)
        self.button.setText('Ku')
        self.button.clicked.connect(self.loaddata)

        self.table.setRowCount(1)

    # def enterkey(self, event):
    #     if event.key() == Qt.Key_Enter:
    #
    # def butpres(self):
    #     self.loaddata()

    def loaddata(self):

        connection = sqlite3.connect('C:\\Users\\kokki\\Desktop\\Solo\\dbdata.db')
        # mytext = self.textfield.toPlainText()
        # if self.checkBox.isChecked() == True:
        #     self.table.setColumnCount(1)
        name = self.textfield_2.toPlainText()

        cur = connection.cursor()
        query = f"SELECT * FROM info WHERE Name = '{name}'"
        cur.execute(query)
        connection.commit()
        res = cur.fetchall()
        if res == []:
            self.label.setText("Error, no such user found")
        else:
            self.label.setText(f"User: {name}")
        tablerow = 0
        # self.table.setRowCount(len(res))
        self.dispname.setText(f"{res[0][1]}")
        self.dispsurname.setText(f"{res[0][2]}")
        self.dispage.setText(f"{res[0][3]}")
        self.dispcity.setText(f"{res[0][4]}")
        # for row in res:
        #     self.table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem((row[1])))
        #     self.table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
        #     self.table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem((row[3])))
        #     self.table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[4])))
        #     tablerow += 1
        # print("SRhgs")


class logorreg(QtWidgets.QDialog):
    def __init__(self):
        super(logorreg, self).__init__()
        loadUi("C:\\Users\\kokki\\Desktop\\Solo\\logorreg.ui", self)
        self.logbut.clicked.connect(self.gologform)
        self.regbut.clicked.connect(self.goregform)

    def gologform(self):
        mainwindow = logform()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goregform(self):
        mainwindow = regform()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class logform(QtWidgets.QDialog):
    def __init__(self):
        super(logform, self).__init__()
        loadUi("C:\\Users\\kokki\\Desktop\\Solo\\logform.ui", self)
        self.pushButton23.clicked.connect(self.gobackRrL)
        self.gologin.clicked.connect(self.logged)

    def gobackRrL(self):
        mainwindow = logorreg()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotomain(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def logged(self):
        password = self.passwordtext.toPlainText()
        username = self.usernametext.toPlainText()
        connection = sqlite3.connect('C:\\Users\\kokki\\Desktop\\Solo\\dbdata.db')
        cur = connection.cursor()
        query = f'select 1 from users WHERE username = "{username}" and password = "{password}"'
        cur.execute(query)
        connection.commit()
        res = cur.fetchall()

        if not res:
            self.label_4.setText("Incorrect username or password")
            print("Not UWU")
        else:
            if res[0][0] == 1:
                print("UWU")
                self.label_4.setText("")
                self.gotomain()

            # print("we")


class regform(QtWidgets.QDialog):
    def __init__(self):
        super(regform, self).__init__()
        loadUi("C:\\Users\\kokki\\Desktop\\Solo\\regform.ui", self)
        self.pushButton21.clicked.connect(self.gobackRrL)
        self.pushButton23.clicked.connect(self.regged)

    def gobackRrL(self):
        mainwindow = logorreg()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotomain(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def regged(self):
        connection = sqlite3.connect('C:\\Users\\kokki\\Desktop\\Solo\\dbdata.db')
        cur = connection.cursor()

        username = self.regusername.toPlainText()
        query = f"select 1 from users WHERE username = '{username}'"
        cur.execute(query)
        res = cur.fetchall()
        if not res:
            print("UWU")
            self.label_7.setText("")
            password = self.regpassword.toPlainText()
            name = self.regname.toPlainText()
            surname = self.regsurname.toPlainText()
            city = self.regcity.toPlainText()
            age = self.regage.toPlainText()
            query = f"insert into info (Name, Surname, Age, City) values ('{name}','{surname}','{age}','{city}')"
            query2 = f"insert into users (username, password) values ('{username}', '{password}')"
            cur.execute(query)
            cur.execute(query2)
            connection.commit()
            self.label_7.setText("Data Gone")

        else:

            self.label_7.setText("This username is already taken")
            print("Not UWU")



        # connection = sqlite3.connect('C:\\Users\\kokki\\Desktop\\Solo\\dbdata.db')
        # cur = connection.cursor()
        # query = f'select 1 from users WHERE username = "{username}" and password = "{password}"'
        # cur.execute(query)
        # connection.commit()
        # res = cur.fetchall()


app = QtWidgets.QApplication(sys.argv)
window = logorreg()

widget = QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.setFixedHeight(600)
widget.setFixedWidth(600)
widget.show()
app.exec_()
