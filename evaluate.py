# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
w=0
r=0
q=0
sd=0
ad=0
w2=0
r2=0
q2=0
sd2=0
ad2=0
w1=0
r1=0
q1=0
sd1=0
ad1=0




import sqlite3

class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(565, 615)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.comboBox_1 = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.comboBox_1.setFont(font)
        self.comboBox_1.setEditable(False)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.openbutton = QtWidgets.QPushButton(Form)
        self.openbutton.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        self.openbutton.setFont(font)
        self.openbutton.setObjectName("openbutton")
        self.horizontalLayout_2.addWidget(self.openbutton)
        self.openbutton.clicked.connect(self.show)
        spacerItem5 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.label_3 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem8 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.poi = QtWidgets.QLineEdit(Form)
        self.poi.setMaximumSize(QtCore.QSize(50, 16777215))
        self.poi.setObjectName("poi")
        self.horizontalLayout_3.addWidget(self.poi)
        spacerItem10 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem11 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setMaximumSize(QtCore.QSize(180, 280))
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_4.addWidget(self.listWidget)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.list1 = QtWidgets.QListWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list1.sizePolicy().hasHeightForWidth())
        self.list1.setSizePolicy(sizePolicy)
        self.list1.setMaximumSize(QtCore.QSize(180, 280))
        self.list1.setObjectName("list1")
        self.horizontalLayout_4.addWidget(self.list1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem15)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem16)
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.calc)
        spacerItem17 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem17)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem18)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem19 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem19)
        self.evcbox()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Evaluate the Performance of your Fantasy Team"))
        self.comboBox_1.setCurrentText(_translate("Form", "Select Team"))
        self.comboBox_1.setItemText(0, _translate("Form", "Select Team"))
        self.comboBox_2.setItemText(0, _translate("Form", "Select Match"))
        self.comboBox_2.setItemText(1, _translate("Form", "Match 1"))
        self.comboBox_2.setItemText(2, _translate("Form", "Match 2"))
        self.comboBox_2.setItemText(3, _translate("Form", "Match 3"))
        self.openbutton.setText(_translate("Form", "Open"))
        self.label_3.setText(_translate("Form", "Players:"))
        self.label_2.setText(_translate("Form", "Points:"))
        self.pushButton.setText(_translate("Form", "Calculate Score:"))

    def evcbox(self):
        cb=[]
        myrb1=sqlite3.connect('database.db')
        currb1=myrb1.cursor()
        sql="SELECT * From teams"
        currb1.execute(sql)
        records=currb1.fetchall()
        for row in records:
            cb.append(row[0])
        cb=list(dict.fromkeys(cb))
        
        for i in cb:
            self.comboBox_1.addItem(i)

    def show(self):
        tb=[]
        yt=[]
        total=0
        mm=str(self.comboBox_1.currentText())
        nn=str(self.comboBox_2.currentText())
        if mm=='Select Team':
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please Select Team")
            msg.setIcon(QMessageBox.Critical)
            x=msg.exec()
        elif nn=='Select Match':
            msg1 = QMessageBox()
            msg1.setWindowTitle("Error")
            msg1.setText("Please Select Match")
            msg1.setIcon(QMessageBox.Critical)
            x=msg1.exec()
        else:
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
            self.poi.setText(str(total))
            self.listWidget.clear()
            self.list1.clear()
            for c in tb:
                self.listWidget.addItem(str(c))
            for a in yt:
                self.list1.addItem(str(a))

    def calc(self):
        
        score=[]
        m="o"
        if self.listWidget.count()==0:
            msg2 = QMessageBox()
            msg2.setWindowTitle("Error")
            msg2.setText("Please select open to continue")
            msg2.setIcon(QMessageBox.Critical)
            x=msg2.exec()
        else:
            list3=[]
            for i in range(self.listWidget.count()):
                list3.append(self.listWidget.item(i).text())
            print(list3)
            myrb1=sqlite3.connect('database.db')
            currb1=myrb1.cursor()
            
            for i in range(11):
                total=0
                m=str(list3[i])
                currb1.execute("SELECT * From match WHERE player='"+m+"';")
                record=currb1.fetchone()
                total=total+(record[1]/2)
                
                if int(record[1])==0:
                     print("")
                        
                else:
                    strate=float(((float(record[1]))/(float(record[2])))*100)
                    if strate>=80 and strate<100:
                        total=total+2
                    elif strate>=100:
                        total=total+4
                
                total=total+(int(record[3])*1)
                total=total+(int(record[4])*2)
                total=total+(record[8]*10)
                
                if int(record[8])>=3:
                    total=total+5
                if int(record[8])==5:
                    total=total+10
                
                
                if int(record[5])==0:
                        print("")
                else:
                    er=(record[7])/((record[5])/6)
                    if er<=2:
                        total=total+10
                    if er>2 and er<=3.5:
                        total=total+7
                    if er>3.5 and er<=4.5:
                        total=total+4
            
                total=total+(int(record[9])*10)
                total=total+(int(record[10])*10)
                total=total+(int(record[11])*10)
                
                score.append(total)
        
            t=0
            for i in score:
                t=float(t+float(i))
            print(t)
            self.lineEdit_2.setText(str(t))
            msg1 = QMessageBox()
            msg1.setWindowTitle("Score")
            msg1.setText("The score of your team is-  "+str(t)+"\t")
            msg1.setIcon(QMessageBox.Information)
            x=msg1.exec()
            if (str(self.comboBox_2.currentText())=='Match 1'):
                global w, r, q, sd, ad
                if w==0:
                    w=w+1
                    r=t
                    sd=str(self.comboBox_1.currentText())
                else:
                    w=0
                    q=t
                    ad=str(self.comboBox_1.currentText())
                    if(r>q):
                        msg3 = QMessageBox()
                        msg3.setWindowTitle("Result")
                        msg3.setText("The team who won the match is:\t"+str(sd)+"\t")
                        msg3.setIcon(QMessageBox.Information)
                        x1=msg3.exec()
                    elif(q==r):
                        msg4 = QMessageBox()
                        msg4.setWindowTitle("Result")
                        msg4.setText("Match 1 has been tied between"+str(sd)+"and"+str(ad))
                        msg4.setIcon(QMessageBox.Information)
                        x2=msg4.exec()
                    elif(q>r):
                        msg5 = QMessageBox()
                        msg5.setWindowTitle("Result")
                        msg5.setText("The team who won the match is:\t"+str(ad)+"\t")
                        msg5.setIcon(QMessageBox.Information)
                        x3=msg5.exec()
                    

            elif (str(self.comboBox_2.currentText())=='Match 2'):
                global w1, r1, q1, sd1, ad1
                if w1==0:
                    w1=w1+1
                    r1=t
                    sd1=str(self.comboBox_1.currentText())
                else:
                    w1=0
                    q1=t
                    ad1=str(self.comboBox_1.currentText())
                    if(r1>q1):
                        msg6 = QMessageBox()
                        msg6.setWindowTitle("Result")
                        msg6.setText("The team who won the match is:\t"+str(sd1)+"\t")
                        msg6.setIcon(QMessageBox.Information)
                        x4=msg6.exec()
                    elif(q1==r1):
                        msg7 = QMessageBox()
                        msg7.setWindowTitle("Result")
                        msg7.setText("Match 1 has been tied between"+str(sd1)+"and"+str(ad1))
                        msg7.setIcon(QMessageBox.Information)
                        x5=msg7.exec()
                    elif(q1>r1):
                        msg8 = QMessageBox()
                        msg8.setWindowTitle("Result")
                        msg8.setText("The team who won the match is:\t"+str(ad1)+"\t")
                        msg8.setIcon(QMessageBox.Information)
                        x5=msg8.exec()
                        
            elif (str(self.comboBox_2.currentText())=='Match 3'):
                global w2, r2, q2, sd2, ad2
                if w2==0:
                    w2=w2+1
                    r2=t
                    sd=str(self.comboBox_1.currentText())
                else:
                    w2=0
                    q2=t
                    ad2=str(self.comboBox_1.currentText())
                    if(r2>q2):
                        msg9 = QMessageBox()
                        msg9.setWindowTitle("Result")
                        msg9.setText("The team who won the match is:\t"+str(sd2)+"\t")
                        msg9.setIcon(QMessageBox.Information)
                        x6=msg9.exec()
                    elif(q2==r2):
                        msg10 = QMessageBox()
                        msg10.setWindowTitle("Result")
                        msg10.setText("Match 1 has been tied between"+str(sd2)+"and"+str(ad2))
                        msg10.setIcon(QMessageBox.Information)
                        x7=msg10.exec()
                    elif(q2>r2):
                        msg11 = QMessageBox()
                        msg11.setWindowTitle("Result")
                        msg11.setText("The team who won the match is:\t"+str(ad2)+"\t")
                        msg11.setIcon(QMessageBox.Information)
                        x8=msg11.exec()
                   
            
                
                
                    
            
        
        
       
               
            
                
        
                    
                        
                        
                            
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    
                


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form1 = QtWidgets.QWidget()
    ui = Ui_Form1()
    ui.setupUi(Form1)
    Form1.show()
    sys.exit(app.exec_())
