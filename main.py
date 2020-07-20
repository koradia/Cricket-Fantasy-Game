# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QLineEdit
from open import Ui_Form
from evaluate import Ui_Form1
import sqlite3

w=0
x=0
y=0
z=0
pav=1000
p=0
tm=None
i=0
j=0
k=0
l=0
rb4=[]
rb1=[]
rb2=[]
rb3=[]
class Ui_MainWindow(object):

    def openwindow(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openwindow1(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_Form1()
        self.ui.setupUi(self.window)
        self.window.show()
        
    
        
        
        
    



    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(855, 551)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.batcount = QtWidgets.QLabel(self.centralwidget)
        self.batcount.setGeometry(QtCore.QRect(380, 180, 91, 71))
        self.batcount.setObjectName("batcount")
        self.horizontalLayout.addWidget(self.batcount)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.bowcount = QtWidgets.QLabel(self.centralwidget)
        self.bowcount.setGeometry(QtCore.QRect(380, 180, 91, 71))
        self.bowcount.setObjectName("bowcount")
        self.horizontalLayout.addWidget(self.bowcount)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(110, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.arcount = QtWidgets.QLabel(self.centralwidget)
        self.arcount.setGeometry(QtCore.QRect(380, 180, 91, 71))
        self.arcount.setObjectName("arcount")
        self.horizontalLayout.addWidget(self.arcount)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.wkcount = QtWidgets.QLabel(self.centralwidget)
        self.wkcount.setGeometry(QtCore.QRect(380, 180, 91, 71))
        self.wkcount.setObjectName("wkcount")
        self.horizontalLayout.addWidget(self.wkcount)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.pointsavailable = QtWidgets.QLabel(self.centralwidget)
        self.pointsavailable.setGeometry(QtCore.QRect(380, 180, 91, 71))        
        self.pointsavailable.setObjectName("pointsavailable")
        self.horizontalLayout_5.addWidget(self.pointsavailable)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.points = QtWidgets.QLabel(self.centralwidget)
        self.points.setGeometry(QtCore.QRect(380, 180, 91, 71))
        self.points.setObjectName("points")
        
        self.horizontalLayout_5.addWidget(self.points)
        spacerItem4 = QtWidgets.QSpacerItem(135, 50, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)

        self.rbbat = QtWidgets.QRadioButton(self.centralwidget)
        self.rbbat.setObjectName("rbbat")
        self.rbbat.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.rbbat)
        self.rbbat.toggled.connect(self.rb1)
        self.rbbow = QtWidgets.QRadioButton(self.centralwidget)
        self.rbbow.setObjectName("rbbow")
        self.rbbow.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.rbbow)
        self.rbbow.toggled.connect(self.rb2)
        self.rbar = QtWidgets.QRadioButton(self.centralwidget)
        self.rbar.setObjectName("rbar")
        self.rbar.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.rbar)
        self.rbar.toggled.connect(self.rb3)
        self.rbwk = QtWidgets.QRadioButton(self.centralwidget)
        self.rbwk.setObjectName("rbwk")
        self.rbwk.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.rbwk)
        self.rbwk.toggled.connect(self.rb4)
        spacerItem7 = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(90, 60))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.teamname = QtWidgets.QLabel(self.centralwidget)
        self.teamname.setGeometry(QtCore.QRect(380, 180, 91, 71))
        self.teamname.setObjectName("teamname")
        self.horizontalLayout_2.addWidget(self.teamname)
        spacerItem8 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem9 = QtWidgets.QSpacerItem(60, 10, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.listw1 = QtWidgets.QListWidget(self.centralwidget)
        self.listw1.setMaximumSize(QtCore.QSize(250, 300))
        self.listw1.setObjectName("listw1")
        self.horizontalLayout_3.addWidget(self.listw1)
        self.listw1.itemDoubleClicked.connect(self.removelistw1)
        spacerItem10 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.listw2 = QtWidgets.QListWidget(self.centralwidget)
        self.listw2.setMaximumSize(QtCore.QSize(250, 300))
        self.listw2.setObjectName("listw2")
        self.horizontalLayout_3.addWidget(self.listw2)
        self.listw2.itemDoubleClicked.connect(self.removelistw2)
        
        spacerItem11 = QtWidgets.QSpacerItem(60, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 855, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.menuManage_Teams.setFont(font)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.newteam = QtWidgets.QAction(MainWindow)
        self.newteam.setObjectName("newteam")
        
        self.openteam = QtWidgets.QAction(MainWindow)
        self.openteam.setObjectName("openteam")
        self.saveteam = QtWidgets.QAction(MainWindow)
        self.saveteam.setObjectName("saveteam")
        self.evaluateteam = QtWidgets.QAction(MainWindow)
        self.evaluateteam.setObjectName("evaluateteam")
        self.rules = QtWidgets.QAction(MainWindow)
        self.rules.setObjectName("rules")
        self.menuManage_Teams.addAction(self.newteam)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.openteam)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.saveteam)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.evaluateteam)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.rules)
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.newteam.triggered.connect(self.nm) 
        self.openteam.triggered.connect(self.openwindow)
        self.saveteam.triggered.connect(self.st)
        self.evaluateteam.triggered.connect(self.openwindow1)
        self.rules.triggered.connect(self.fun)

    

    

    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Your Selection"))
        self.label_5.setText(_translate("MainWindow", "Batting[BAT]:"))
        self.label_4.setText(_translate("MainWindow", "Bowler[BOW]:"))
        self.label_3.setText(_translate("MainWindow", "Allrounder[AR]:"))
        self.label_2.setText(_translate("MainWindow", "Wicket-Keeper[Wk]:"))
        self.label_6.setText(_translate("MainWindow", "Points Available:"))
        self.label_7.setText(_translate("MainWindow", "Points:"))
        self.rbbat.setText(_translate("MainWindow", "BAT"))
        self.rbbow.setText(_translate("MainWindow", "Bow"))
        self.rbar.setText(_translate("MainWindow", "AR"))
        self.rbwk.setText(_translate("MainWindow", "WK"))
        self.label_8.setText(_translate("MainWindow", "Team:"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.newteam.setText(_translate("MainWindow", "New Team"))
        self.openteam.setText(_translate("MainWindow", "Open Team"))
        self.saveteam.setText(_translate("MainWindow", "Save Team"))
        self.evaluateteam.setText(_translate("MainWindow", "Evaluate Team"))
        self.rules.setText(_translate("MainWindow", "Rules"))




    def nm(self):
            global w, x, y, z, i, j, k, l
            w=0
            x=0
            y=0
            z=0
            i=0
            j=0
            k=0
            l=0
            self.batcount.setText(str(w))
            self.bowcount.setText(str(x))
            self.arcount.setText(str(y))
            self.wkcount.setText(str(z))
            self.points.setText("0")
            self.pointsavailable.setText("1000")
            self.listw1.clear()
            self.listw2.clear()
            xl.getText()
            self.teamname.setText(str(tm))
            self.listw1.clear()
            self.listw2.clear()
            self.rbbat.setEnabled(True)
            self.rbbow.setEnabled(True)
            self.rbar.setEnabled(True)
            self.rbwk.setEnabled(True)


    def fun(self):
        msg = QMessageBox()
        msg.setWindowTitle("Rules")
        msg.setText("1.\tYou can not select 2 wicket keepers\n2.\tAny team should only be consist of 11 players.\n3.\tIf you want to take a match between two then you\n\t have to select match no. accordingly.")
        msg.setIcon(QMessageBox.Information)
        x=msg.exec()
        

    
        

    def st(self):
        
       xx=int(self.wkcount.text())
       yy=int(self.listw2.count())
        
       if xx>1:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("More Than 1 Wicket-keeper is not Allowed")
            msg.setIcon(QMessageBox.Critical)
            x1=msg.exec()
       elif xx<1:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("there is no wicket-keeper in your team")
            msg.setIcon(QMessageBox.Critical)
            x1=msg.exec()
       elif p>1000:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Your Team points should not be greater than 1000")
            msg.setIcon(QMessageBox.Critical)
            x1=msg.exec()

       elif yy>11 or yy<11:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Your Team should only have 11 players")
            msg.setIcon(QMessageBox.Critical)
            x1=msg.exec()
            

       else:
           items=[]
           for i1 in range(yy):
               items.append(self.listw2.item(i1).text())
           print(items)
           g=(self.teamname.text())
           print(g)
           h=int(self.points.text())
           print(h)
           myrb1=sqlite3.connect('database.db')
            
           for e in items:
               myrb1=sqlite3.connect('database.db')
               sql="SELECT value FROM stats WHERE player='"+e+"';"
               currb1=myrb1.cursor()
               currb1.execute(sql)
               player_pt=currb1.fetchall()
               print(player_pt)
               currb1.execute("INSERT INTO teams VALUES (?,?,?);", (g,e,player_pt[0][0]))
               myrb1.commit()
           global w, x, y, z, i, j, k, l
           w=0
           x=0
           y=0
           z=0
           i=0
           j=0
           k=0
           l=0
           self.batcount.setText(str(w))
           self.bowcount.setText(str(x))
           self.arcount.setText(str(y))
           self.wkcount.setText(str(z))
           self.points.setText("0")
           self.pointsavailable.setText("1000")
           self.listw1.clear()
           self.listw2.clear()
           self.listw1.clear()
           self.listw2.clear()
                
     
    def rb1(self):
        self.listw1.clear()
        global rb1
        global l
        while l==0:
            self.listw1.clear()
            myrb1=sqlite3.connect('database.db')
            
            sql="SELECT * from stats WHERE ctg=='BAT';"
            currb1=myrb1.cursor()
            currb1.execute(sql)
            while True:
                rec=currb1.fetchone()
                if rec is None:
                    break
                else :
                    rb1.append(rec[0])
                    
            l=l+1
        
        for o in rb1:
            self.listw1.addItem(o)

    def rb2(self):
        self.listw1.clear()
        global rb2
        global k
        while k==0:
            self.listw1.clear()
            myrb1=sqlite3.connect('database.db')
            
            sql="SELECT * from stats WHERE ctg=='BWL';"
            currb1=myrb1.cursor()
            currb1.execute(sql)
            while True:
                rec=currb1.fetchone()
                if rec is None:
                    break
                else :
                    rb2.append(rec[0])
                    
            k=k+1
        
        for o in rb2:
            self.listw1.addItem(o)

    def rb3(self):
        self.listw1.clear()
        global rb3
        global j
        while j==0:
            self.listw1.clear()
            myrb1=sqlite3.connect('database.db')
            
            sql="SELECT * from stats WHERE ctg=='AR';"
            currb1=myrb1.cursor()
            currb1.execute(sql)
            while True:
                rec=currb1.fetchone()
                if rec is None:
                   break
                else :
                    rb3.append(rec[0])
                    
                    
            j=j+1
        
        for o in rb3:
            self.listw1.addItem(o)

    def rb4(self):
        self.listw1.clear()
        global rb4
        global i
        while i==0:
            
            self.listw1.clear()
            myrb1=sqlite3.connect('database.db')
            
            sql="SELECT * from stats WHERE ctg=='WK';"
                
            currb1=myrb1.cursor()
            currb1.execute(sql)
            while True:
                rec=currb1.fetchone()
                if rec is None:
                    break
                else :
                    rb4.append(rec[0])
                    
            i=i+1
        
        for o in rb4:
            self.listw1.addItem(o)
        
        
        
        

    def removelistw1(self,item):
        global p, pav, rb4, rb1, rb2, rb3
        nm=(item.text())
        myrb1=sqlite3.connect('database.db')
        
        sql="SELECT * from stats WHERE player='"+nm+"';"
        currb1=myrb1.cursor()
        currb1.execute(sql)
        record=currb1.fetchone()
        
        if (record[6])=='BAT':
            global w
            w=w+1
            self.batcount.setText(str(w))
            rb1.remove(record[0])
            print (rb1)
        elif str(record[6])=='BWL':
            global x
            x=x+1
            self.bowcount.setText(str(x))
            rb2.remove(record[0])
            print (rb2)
        elif str(record[6])=='AR':
            global y
            y=y+1
            self.arcount.setText(str(y))
            rb3.remove(record[0])
            print (rb3)
        elif str(record[6])=='WK':
            global z
            z=z+1
            self.wkcount.setText(str(z))
            rb4.remove(record[0])
            print (rb4)
        
        pav=pav-int(record[5])
        p=p+int(record[5])
        self.points.setText(str(p))
        self.pointsavailable.setText(str(pav))
        
        self.listw1.takeItem(self.listw1.row(item))
        
        
        self.listw2.addItem(item.text())

    def removelistw2(self,item):
        global p, pav, rb1, rb2, rb3, rb4
        nm=(item.text())
        myrb1=sqlite3.connect('database.db')
        
        sql="SELECT * from stats WHERE player='"+nm+"';"
        currb1=myrb1.cursor()
        currb1.execute(sql)
        record=currb1.fetchone()
        
        if (record[6])=='BAT':
            global w
            w=w-1
            self.batcount.setText(str(w))
            rb1.append(record[0])
        elif str(record[6])=='BWL':
            global x
            x=x-1
            self.bowcount.setText(str(x))
            rb2.append(record[0])
            
        elif str(record[6])=='AR':
            global y
            y=y-1
            self.arcount.setText(str(y))
            rb3.append(record[0])
        elif str(record[6])=='WK':
            global z
            z=z-1
            self.wkcount.setText(str(z))
            rb4.append(record[0])
        
        pav=pav+int(record[5])
        p=p-int(record[5])
        self.points.setText(str(p))
        self.pointsavailable.setText(str(pav))
        self.listw2.takeItem(self.listw2.row(item))
        


class ren:
    def __init__(self,x):
        self.xl=None
        


    def getText(self):
            

        text, okPressed = QInputDialog.getText(self.xl, "Get text","Your name:", QLineEdit.Normal, "")
        
        if okPressed and text != '':
            print(text)
            global tm
            tm=str(text)
    

    
        
xl=ren(None)
            
            
        
        
        
        
            
            
            
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
