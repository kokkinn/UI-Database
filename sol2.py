import sys

from PyQt5.QtCore import QEventLoop, QTimer, QTime
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
import sqlite3

usrn = None


class info(QtWidgets.QDialog):
    def __init__(self):
        super(info, self).__init__()
        loadUi("C:\\Users\\kokki\\Desktop\\Solo\\info.ui", self)
        self.pushButton.clicked.connect(self.goback)

    def goback(self):
        self.close()


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


userm = None


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
                global userm
                userm = username
                self.gotomain()


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
        while True:
            usrnpr = None
            passpr = None
            agpr = None
            username = self.regusername.toPlainText()
            if username == '':
                usrnpr = True
            query = f"select 1 from users WHERE username = '{username}'"
            cur.execute(query)
            res = cur.fetchall()
            if res:
                usrnpr = True
            print("UWU")
            password = self.regpassword.toPlainText()
            if len(password) < 5:
                passpr = True
            name = self.regname.toPlainText().capitalize()
            surname = self.regsurname.toPlainText().capitalize()
            city = self.regcity.toPlainText()
            age = self.regage.toPlainText()
            if age.isdigit() is False or int(age) < 0:
                agpr = True
            genre = self.reggenre.currentIndex()
            print("Good1")
            if usrnpr is True or passpr is True or agpr is True:
                if usrnpr is True:
                    self.usrnp.setText("Incorrect username")
                if passpr is True:
                    self.pssp.setText("Password is too easy ")
                if agpr is True:
                    self.agp.setText("Incorrect age")
                break
            query = f"insert into info (Name, Surname, Age, City, GenreLove) values ('{name}','{surname}','{age}','{city}','{genre}')"
            query2 = f"insert into users (username, password) values ('{username}', '{password}')"
            print("Good2")
            cur.execute(query)
            cur.execute(query2)
            connection.commit()
            self.label_7.setText("Registered Successfully")
            loop = QEventLoop()
            QTimer.singleShot(2000, loop.quit)
            loop.exec_()
            self.gotomain()
            break


class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("C:\\Users\\kokki\\Desktop\\Solo\\new.ui", self)
        timer = QTimer(self)
        timer.timeout.connect(self.disp)
        timer.start(1000)
        self.loggedname.setText(f"{userm}")
        self.button.clicked.connect(self.loaddata)
        self.table.setRowCount(1)
        self.pushButton.clicked.connect(self.goinfo)
        self.findgenre.clicked.connect(self.filltable)

    def filltable(self):
        a = self.comboBox.currentIndex()
        connection = sqlite3.connect('C:\\Users\\kokki\\Desktop\\Solo\\dbdata.db')
        cur = connection.cursor()
        query = f"SELECT u.username, i.City FROM users u join info i on u.id = i.ID WHERE i.GenreLove = {a};"
        cur.execute(query)
        connection.commit()
        res = cur.fetchall()
        self.table.setRowCount(len(res))
        tablerow = 0
        for row in res:
            self.table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem((row[0])))
            self.table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))

            tablerow += 1

    def goinfo(self):
        self.myOtherWindow = info()
        self.myOtherWindow.show()

    def disp(self):
        current_time = QTime.currentTime()
        disptx = current_time.toString('hh:mm:ss')
        self.label_6.setText(disptx)

    def loaddata(self):
        connection = sqlite3.connect('C:\\Users\\kokki\\Desktop\\Solo\\dbdata.db')
        name = self.textfield_2.toPlainText()

        cur = connection.cursor()
        query = f'SELECT i.ID, i.Name, i.Surname, i.City, i.Age, g.Genre, u.username FROM info i JOIN Genre g on ' \
                f'i.GenreLove = g.ID JOIN users u on i.ID = u.id WHERE u.username = "{name}" '
        cur.execute(query)
        connection.commit()
        res = cur.fetchall()
        if not res:
            self.label.setText("Error, no such user found")
        else:
            self.dispname.setText(f"{res[0][1]}")
            self.dispsurname.setText(f"{res[0][2]}")
            self.dispage.setText(f"{res[0][3]}")
            self.dispcity.setText(f"{res[0][4]}")
            self.dispgenre.setText(f"{res[0][5]}")
            self.label_9.setText(f"{res[0][6]}")


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()

widget = QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.setFixedHeight(500)
widget.setFixedWidth(700)
widget.show()
app.exec_()
