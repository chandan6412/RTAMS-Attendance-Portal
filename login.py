# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
from Portal import Ui_MainWindow
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_userLS(object):
    def showmessagebox(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def openmainwindowshow(self):
        self.openMainWindow = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.openMainWindow)
        self.openMainWindow.show()

    def loginauthentication(self):
        username = self.loginusername_lineEdit.text()
        password = self.loginpassword_lineEdit.text()

        connection = sqlite3.connect("signIn.db")
        result = connection.execute("SELECT Username, Password FROM USER WHERE Username = ? AND Password = ?",((str(username)),(str(password))))
        if(len(result.fetchall()) > 0):
            #print("User     Found")
            self.openmainwindowshow()
        else:
            #print("User Not Found")
            self.showmessagebox('Warning','Invalid Usernam Or Password')
        connection.close()


    def signup(self):
        print("clicked")
        username1 = self.signupusername_lineEdit.text()
        emailid1 = self.signupemailid_lineEdit.text()
        password1 = self.signuppassword_lineEdit.text()
        connection1 = sqlite3.connect("signIn.db")
        connection1.execute("INSERT INTO USER(USERNAME, EMAIL_ID, PASSWORD) VALUES(?, ?, ?)",(str(username1), str(emailid1), str(password1)))
        connection1.commit()
        connection1.close()

    def setupUi(self, userLS):
        userLS.setObjectName(_fromUtf8("userLS"))
        userLS.resize(491, 606)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(14)
        userLS.setFont(font)
        userLS.setAcceptDrops(True)
        userLS.setSizeGripEnabled(True)
        self.signupTab = QtGui.QTabWidget(userLS)
        self.signupTab.setGeometry(QtCore.QRect(80, 20, 351, 521))
        self.signupTab.setObjectName(_fromUtf8("signupTab"))
        self.loginTab = QtGui.QWidget()
        self.loginTab.setMaximumSize(QtCore.QSize(347, 16777215))
        self.loginTab.setObjectName(_fromUtf8("loginTab"))
        self.gridLayout = QtGui.QGridLayout(self.loginTab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.loginTab)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.loginusername_lineEdit = QtGui.QLineEdit(self.loginTab)
        self.loginusername_lineEdit.setObjectName(_fromUtf8("loginusername_lineEdit"))
        self.gridLayout.addWidget(self.loginusername_lineEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.loginTab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.loginpassword_lineEdit = QtGui.QLineEdit(self.loginTab)
        self.loginpassword_lineEdit.setObjectName(_fromUtf8("loginpassword_lineEdit"))
        self.gridLayout.addWidget(self.loginpassword_lineEdit, 1, 1, 1, 1)
        self.loginButton = QtGui.QPushButton(self.loginTab)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        '################# Login event ########################################'
        self.loginButton.clicked.connect(self.loginauthentication)

        self.gridLayout.addWidget(self.loginButton, 2, 0, 1, 2)
        self.signupTab.addTab(self.loginTab, _fromUtf8(""))
        self.signupTab1 = QtGui.QWidget()
        self.signupTab1.setObjectName(_fromUtf8("signupTab1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.signupTab1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.signupTab1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.signupusername_lineEdit = QtGui.QLineEdit(self.signupTab1)
        self.signupusername_lineEdit.setObjectName(_fromUtf8("signupusername_lineEdit"))
        self.gridLayout_2.addWidget(self.signupusername_lineEdit, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.signupTab1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.signupemailid_lineEdit = QtGui.QLineEdit(self.signupTab1)
        self.signupemailid_lineEdit.setObjectName(_fromUtf8("signupemailid_lineEdit"))
        self.gridLayout_2.addWidget(self.signupemailid_lineEdit, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.signupTab1)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.signuppassword_lineEdit = QtGui.QLineEdit(self.signupTab1)
        self.signuppassword_lineEdit.setObjectName(_fromUtf8("signuppassword_lineEdit"))
        self.gridLayout_2.addWidget(self.signuppassword_lineEdit, 2, 1, 1, 1)
        self.signupButton_2 = QtGui.QPushButton(self.signupTab1)
        self.signupButton_2.setObjectName(_fromUtf8("signupButton_2"))
        '###################### Sign Up Event ####################################'
        self.signupButton_2.clicked.connect(self.signup)

        self.gridLayout_2.addWidget(self.signupButton_2, 3, 0, 1, 2)
        self.signupTab.addTab(self.signupTab1, _fromUtf8(""))
        self.signupTab.raise_()
        self.label.raise_()

        self.retranslateUi(userLS)
        self.signupTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(userLS)

    def retranslateUi(self, userLS):
        userLS.setWindowTitle(_translate("userLS", "Dialog", None))
        self.label.setText(_translate("userLS", "Username", None))
        self.label_2.setText(_translate("userLS", "Password", None))
        self.loginButton.setText(_translate("userLS", "Login", None))
        self.signupTab.setTabText(self.signupTab.indexOf(self.loginTab), _translate("userLS", "Login", None))
        self.label_3.setText(_translate("userLS", "Username", None))
        self.label_4.setText(_translate("userLS", "EmailId", None))
        self.label_5.setText(_translate("userLS", "Password", None))
        self.signupButton_2.setText(_translate("userLS", "SignUp", None))
        self.signupTab.setTabText(self.signupTab.indexOf(self.signupTab1), _translate("userLS", "SignUp", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    userLS = QtGui.QDialog()
    ui = Ui_userLS()
    ui.setupUi(userLS)
    userLS.show()
    sys.exit(app.exec_())

