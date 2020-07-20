# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'open.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(435, 121)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 381, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.operation)
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.cbox()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Team:"))
        self.pushButton.setText(_translate("Form", "Open"))


    def cbox(self):
        cb=[]
        myrb1=sqlite3.connect('database.db')
        currb1=myrb1.cursor()
        sql="SELECT * From teams"
        currb1.execute(sql)
        records=currb1.fetchall()
        for row in records:
            cb.append(row[0])
        cb=list(dict.fromkeys(cb))
        print(cb)
        for i in cb:
            self.comboBox.addItem(i)


    def operation(self):
        tb=[]
        yt=[]
        total=0
        mm=str(self.comboBox.currentText())
        myrb1=sqlite3.connect('database.db')
        currb1=myrb1.cursor()
        sql="SELECT * From teams WHERE name='"+mm+"';"
        currb1.execute(sql)
        record=currb1.fetchall()
        for row in record:
            tb.append(row[1])
        print(tb)
        for row in record:
            yt.append(row[2])
        print(yt)
        for i in range(0,len(yt)):
            total=total+int(yt[i])
        print(total)
        msg = QMessageBox()
        msg.setWindowTitle("Team Info")
        msg.setText("Team consist of players-\n\n"+str(tb[0])+"\n"+str(tb[1])+"\n"+str(tb[2])+"\n"+str(tb[3])+"\n"+str(tb[4])+"\n"+str(tb[5])+"\n"+str(tb[6])+"\n"+str(tb[7])+"\n"+str(tb[8])+"\n"+str(tb[9])+"\n"+str(tb[10])+"\n\n\ntotal score of this team is-\t"+str(total)+"\t")
        msg.setIcon(QMessageBox.Information)
        x=msg.exec()
        
        
        
        
        
        

        
        
            
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
