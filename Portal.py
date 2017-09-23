# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'Portal.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Detection_Recognition import Detector,FaceDetection,createdataset
from recognitionScript import recogniser,recogniserImage
import os
import cv2
import sys

faceCascade = cv2.CascadeClassifier("frontal_face.xml")
folder = "RTMS/face_photos/test_images"

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


def getimagepath():
    filePath = QtGui.QFileDialog.getOpenFileName(None,
                                                 'Select Image',
                                                 "home/chandan/Pictures",
                                                 ('*.png *.jpg *.jpeg'))
    # print('filePath', filePath, '\n')
    #
    # fileHandle = open(filePath, 'r')
    # lines = fileHandle.readlines()
    # for line in lines:
    #     print(line)
    return filePath

class Ui_MainWindow(object):
    def imageRecognition1(frame):
        cv2.imshow('IMAGE GOT',frame)
        cv2.waitKey(1)

    def detectRImage(self):
        print("detect image clicked R")
        counter=1
        filePath = getimagepath()
        print('FilePath' , filePath, '\n')
        recogniserImage(filePath,counter)


    def detectDImage(self):
        counter=1;
        print("Detect image clicked D")
        filePath = getimagepath()
        print('FilePath' , filePath, '\n')
        frame = cv2.imread(str(filePath))
        cv2.imshow('SelectedImage', frame)
        FaceDetection(frame,counter)


    def camRFeed(self):
        print("Detect Image from cam clicked R")
        counter =20;
        recogniser(folder,counter)


    def camDFeed(self):
        print("Detect Image from cam clicked D")
        Detector()


    def captureCFeed(self):
        print("clicked")
        branch = str(self.SelectBranchC.currentText())
        year = str(self.SelectYearC.currentText())
        semester = str(self.SelectSemesterC.currentText())
        section = str(self.SelectSectionC.currentText())
        name = str(self.NameC.text()).lower()

        folder = "tf_face/" + name + "/" + branch + "/" + year + "/" + semester + "/" + section # input name
        if not os.path.exists(folder):
            #os.mkdir(folder)
            os.makedirs(folder)
            #n = True
        else:
            print "This name already exists"
            #n = False

    def trainTFeed(self):
        print("clicked")
        branch1 = str(self.SelectBranchT.currentText())
        year1 = str(self.SelectYearT.currentText())
        semester1 = str(self.SelectSemesterT.currentText())
        section1 = str(self.SelectSectionT.currentText())
        name1 = str(self.NameT.text()).lower()

        folder = "tf_face/" + name1 + "/" + branch1 + "/" + year1 + "/" + semester1 + "/" + section1 # input name
        if os.path.exists(folder):
            print("Successfully Taken folders")
        else:
            print "Folder name does not exist"




    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(515, 624)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        MainWindow.setStyleSheet(_fromUtf8("border-color: rgb(0, 255, 0);\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 225), stop:1 rgba(255, 255, 255, 255));"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(371, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 66, 255, 227), stop:1 rgba(255, 255, 255, 255));"))

        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.DetectImage = QtGui.QWidget()
        self.DetectImage.setObjectName(_fromUtf8("DetectImage"))
        self.label = QtGui.QLabel(self.DetectImage)
        self.label.setGeometry(QtCore.QRect(20, 40, 31, 21))
        self.label.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 0, 219), stop:1 rgba(255, 255, 255, 255));"))

        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.DetectImage)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 161, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.DetectImage)
        self.label_3.setGeometry(QtCore.QRect(20, 280, 31, 16))
        self.label_3.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 0, 219), stop:1 rgba(255, 255, 255, 255));"))

        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.DetectImage)
        self.label_4.setGeometry(QtCore.QRect(60, 280, 141, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        # self.SelectButtonD = QtGui.QPushButton(self.DetectImage)
        # self.SelectButtonD.setGeometry(QtCore.QRect(60, 140, 85, 27))
        # self.SelectButtonD.setObjectName(_fromUtf8("SelectButtonD"))
        # '################### SELECT IMAGE EVENT #############################'
        # self.SelectButtonD.clicked.connect(self.selectDImage)


        self.DetectButtonD = QtGui.QPushButton(self.DetectImage)
        self.DetectButtonD.setGeometry(QtCore.QRect(120, 140, 85, 27))
        self.DetectButtonD.setObjectName(_fromUtf8("DetectButtonD"))
        '################### DETECT IMAGE EVENT D #############################'
        self.DetectButtonD.clicked.connect(self.detectDImage)


        self.CamButtonD = QtGui.QPushButton(self.DetectImage)
        self.CamButtonD.setGeometry(QtCore.QRect(80, 370, 201, 27))
        self.CamButtonD.setObjectName(_fromUtf8("CamButtonD"))
        '################### OPEN CAM FOR DETECTION EVENT #####################'
        self.CamButtonD.clicked.connect(self.camDFeed)


        self.tabWidget.addTab(self.DetectImage, _fromUtf8(""))
        self.RecogniseImage = QtGui.QWidget()
        self.RecogniseImage.setObjectName(_fromUtf8("RecogniseImage"))
        self.label_5 = QtGui.QLabel(self.RecogniseImage)
        self.label_5.setGeometry(QtCore.QRect(30, 60, 31, 21))
        self.label_5.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 0, 219), stop:1 rgba(255, 255, 255, 255));"))

        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.RecogniseImage)
        self.label_6.setGeometry(QtCore.QRect(30, 330, 31, 21))
        self.label_6.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 0, 219), stop:1 rgba(255, 255, 255, 255));"))

        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.RecogniseImage)
        self.label_7.setGeometry(QtCore.QRect(70, 60, 161, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.RecogniseImage)
        self.label_8.setGeometry(QtCore.QRect(70, 330, 231, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.DetectButtonR = QtGui.QPushButton(self.RecogniseImage)
        self.DetectButtonR.setGeometry(QtCore.QRect(120, 150, 85, 27))
        self.DetectButtonR.setObjectName(_fromUtf8("DetectButtonR"))
        '#################### DETECT IMAGE EVENT R #############################'
        self.DetectButtonR.clicked.connect(self.detectRImage)

        self.CamButtonR = QtGui.QPushButton(self.RecogniseImage)
        self.CamButtonR.setGeometry(QtCore.QRect(70, 410, 211, 27))
        self.CamButtonR.setObjectName(_fromUtf8("CamButtonR"))
        '#################### OPEN CAM FOR RECOGNITION EVENT ###################'
        self.CamButtonR.clicked.connect(self.camRFeed)

        self.tabWidget.addTab(self.RecogniseImage, _fromUtf8(""))
        self.CreateImage = QtGui.QWidget()
        self.CreateImage.setObjectName(_fromUtf8("CreateImage"))
        self.BranchC = QtGui.QLabel(self.CreateImage)
        self.BranchC.setGeometry(QtCore.QRect(30, 81, 51, 21))
        self.BranchC.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 0, 219), stop:1 rgba(255, 255, 255, 255));"))

        self.BranchC.setObjectName(_fromUtf8("BranchC"))
        self.SemesterC = QtGui.QLabel(self.CreateImage)
        self.SemesterC.setGeometry(QtCore.QRect(30, 210, 71, 21))
        self.SemesterC.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 0, 219), stop:1 rgba(255, 255, 255, 255));"))

        self.SemesterC.setObjectName(_fromUtf8("SemesterC"))
        self.SectionC = QtGui.QLabel(self.CreateImage)
        self.SectionC.setGeometry(QtCore.QRect(30, 280, 61, 21))
        self.SectionC.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 0, 219), stop:1 rgba(255, 255, 255, 255));"))

        self.SectionC.setObjectName(_fromUtf8("SectionC"))
        self.NameC_2 = QtGui.QLabel(self.CreateImage)
        self.NameC_2.setGeometry(QtCore.QRect(30, 350, 50, 12))
        self.NameC_2.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 0, 219), stop:1 rgba(255, 255, 255, 255));"))

        self.NameC_2.setObjectName(_fromUtf8("NameC_2"))
        self.YearC = QtGui.QLabel(self.CreateImage)
        self.YearC.setGeometry(QtCore.QRect(30, 150, 50, 16))
        self.YearC.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 0, 219), stop:1 rgba(255, 255, 255, 255));"))

        self.YearC.setObjectName(_fromUtf8("YearC"))
        self.CaptureButtonC = QtGui.QPushButton(self.CreateImage)
        self.CaptureButtonC.setGeometry(QtCore.QRect(140, 390, 85, 27))
        self.CaptureButtonC.setObjectName(_fromUtf8("CaptureButtonC"))
        '############################# CAPTURE C EVENT ################################'
        self.CaptureButtonC.clicked.connect(self.captureCFeed)

        # self.TrainButtonC = QtGui.QPushButton(self.CreateImage)
        # self.TrainButtonC.setGeometry(QtCore.QRect(140, 460, 85, 27))
        # self.TrainButtonC.setObjectName(_fromUtf8("TrainButtonC"))
        # '############################# TRAIN C EVENT ##################################'
        # self.TrainButtonC.clicked.connect(self.trainCFeed)

        self.SelectBranchC = QtGui.QComboBox(self.CreateImage)
        self.SelectBranchC.setGeometry(QtCore.QRect(190, 80, 151, 24))
        self.SelectBranchC.setMouseTracking(False)
        self.SelectBranchC.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.SelectBranchC.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.SelectBranchC.setAcceptDrops(True)
        self.SelectBranchC.setObjectName(_fromUtf8("SelectBranchC"))
        self.SelectBranchC.addItem(_fromUtf8(""))
        self.SelectBranchC.setItemText(0, _fromUtf8("Select Branch"))
        self.SelectBranchC.addItem(_fromUtf8(""))
        self.SelectBranchC.addItem(_fromUtf8(""))
        self.SelectBranchC.addItem(_fromUtf8(""))
        self.SelectBranchC.addItem(_fromUtf8(""))
        self.SelectBranchC.addItem(_fromUtf8(""))
        self.SelectYearC = QtGui.QComboBox(self.CreateImage)
        self.SelectYearC.setGeometry(QtCore.QRect(190, 140, 151, 24))
        self.SelectYearC.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.SelectYearC.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.SelectYearC.setAcceptDrops(True)
        self.SelectYearC.setObjectName(_fromUtf8("SelectYearC"))
        self.SelectYearC.addItem(_fromUtf8(""))
        self.SelectYearC.addItem(_fromUtf8(""))
        self.SelectYearC.addItem(_fromUtf8(""))
        self.SelectYearC.addItem(_fromUtf8(""))
        self.SelectYearC.addItem(_fromUtf8(""))
        self.SelectYearC.addItem(_fromUtf8(""))
        self.SelectYearC.addItem(_fromUtf8(""))
        self.SelectSemesterC = QtGui.QComboBox(self.CreateImage)
        self.SelectSemesterC.setGeometry(QtCore.QRect(190, 210, 151, 24))
        self.SelectSemesterC.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.SelectSemesterC.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.SelectSemesterC.setAcceptDrops(True)
        self.SelectSemesterC.setObjectName(_fromUtf8("SelectSemesterC"))
        self.SelectSemesterC.addItem(_fromUtf8(""))
        self.SelectSemesterC.addItem(_fromUtf8(""))
        self.SelectSemesterC.addItem(_fromUtf8(""))
        self.SelectSemesterC.addItem(_fromUtf8(""))
        self.SelectSemesterC.addItem(_fromUtf8(""))
        self.SelectSemesterC.addItem(_fromUtf8(""))
        self.SelectSemesterC.addItem(_fromUtf8(""))
        self.SelectSemesterC.addItem(_fromUtf8(""))
        self.SelectSemesterC.addItem(_fromUtf8(""))
        self.SelectSectionC = QtGui.QComboBox(self.CreateImage)
        self.SelectSectionC.setGeometry(QtCore.QRect(190, 280, 151, 24))
        self.SelectSectionC.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.SelectSectionC.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.SelectSectionC.setAcceptDrops(True)
        self.SelectSectionC.setObjectName(_fromUtf8("SelectSectionC"))
        self.SelectSectionC.addItem(_fromUtf8(""))
        self.SelectSectionC.addItem(_fromUtf8(""))
        self.SelectSectionC.addItem(_fromUtf8(""))
        self.SelectSectionC.addItem(_fromUtf8(""))
        self.SelectSectionC.addItem(_fromUtf8(""))
        self.NameC = QtGui.QLineEdit(self.CreateImage)
        self.NameC.setGeometry(QtCore.QRect(192, 340, 151, 22))
        self.NameC.setText(_fromUtf8(""))
        self.NameC.setObjectName(_fromUtf8("NameC"))
        self.tabWidget.addTab(self.CreateImage, _fromUtf8(""))
        self.TrainImage = QtGui.QWidget()
        self.TrainImage.setObjectName(_fromUtf8("TrainImage"))
        self.BranchT = QtGui.QLabel(self.TrainImage)
        self.BranchT.setGeometry(QtCore.QRect(30, 80, 61, 21))
        self.BranchT.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 0, 219), stop:1 rgba(255, 255, 255, 255));"))

        self.BranchT.setObjectName(_fromUtf8("BranchT"))
        self.YearT = QtGui.QLabel(self.TrainImage)
        self.YearT.setGeometry(QtCore.QRect(30, 140, 50, 21))
        self.YearT.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 0, 219), stop:1 rgba(255, 255, 255, 255));"))

        self.YearT.setObjectName(_fromUtf8("YearT"))
        self.SemesterT = QtGui.QLabel(self.TrainImage)
        self.SemesterT.setGeometry(QtCore.QRect(30, 200, 71, 31))
        self.SemesterT.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 0, 219), stop:1 rgba(255, 255, 255, 255));"))

        self.SemesterT.setObjectName(_fromUtf8("SemesterT"))
        self.SectionT = QtGui.QLabel(self.TrainImage)
        self.SectionT.setGeometry(QtCore.QRect(30, 270, 71, 20))
        self.SectionT.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 0, 219), stop:1 rgba(255, 255, 255, 255));"))

        self.SectionT.setObjectName(_fromUtf8("SectionT"))
        self.NameT_2 = QtGui.QLabel(self.TrainImage)
        self.NameT_2.setGeometry(QtCore.QRect(30, 330, 50, 16))
        self.NameT_2.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 0, 219), stop:1 rgba(255, 255, 255, 255));"))

        self.NameT_2.setObjectName(_fromUtf8("NameT_2"))
        # self.CaptureButtonT = QtGui.QPushButton(self.TrainImage)
        # self.CaptureButtonT.setGeometry(QtCore.QRect(120, 400, 85, 27))
        # self.CaptureButtonT.setObjectName(_fromUtf8("CaptureButtonT"))
        # '############################## CAPTURE EVENT #################################'
        # self.CaptureButtonT.clicked.connect(self.captureTFeed)

        self.TrainButtonT = QtGui.QPushButton(self.TrainImage)
        self.TrainButtonT.setGeometry(QtCore.QRect(120, 460, 85, 27))
        self.TrainButtonT.setObjectName(_fromUtf8("TrainButtonT"))
        '############################# TRAIN EVENT ####################################3'
        self.TrainButtonT.clicked.connect(self.trainTFeed)

        self.SelectBranchT = QtGui.QComboBox(self.TrainImage)
        self.SelectBranchT.setGeometry(QtCore.QRect(170, 80, 161, 24))
        self.SelectBranchT.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.SelectBranchT.setAcceptDrops(True)
        self.SelectBranchT.setObjectName(_fromUtf8("SelectBranchT"))
        self.SelectBranchT.addItem(_fromUtf8(""))
        self.SelectBranchT.addItem(_fromUtf8(""))
        self.SelectBranchT.addItem(_fromUtf8(""))
        self.SelectBranchT.addItem(_fromUtf8(""))
        self.SelectBranchT.addItem(_fromUtf8(""))
        self.SelectBranchT.addItem(_fromUtf8(""))
        self.SelectYearT = QtGui.QComboBox(self.TrainImage)
        self.SelectYearT.setGeometry(QtCore.QRect(170, 140, 161, 24))
        self.SelectYearT.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.SelectYearT.setAcceptDrops(True)
        self.SelectYearT.setObjectName(_fromUtf8("SelectYearT"))
        self.SelectYearT.addItem(_fromUtf8(""))
        self.SelectYearT.addItem(_fromUtf8(""))
        self.SelectYearT.addItem(_fromUtf8(""))
        self.SelectYearT.addItem(_fromUtf8(""))
        self.SelectYearT.addItem(_fromUtf8(""))
        self.SelectYearT.addItem(_fromUtf8(""))
        self.SelectYearT.addItem(_fromUtf8(""))
        self.SelectSemesterT = QtGui.QComboBox(self.TrainImage)
        self.SelectSemesterT.setGeometry(QtCore.QRect(170, 200, 161, 24))
        self.SelectSemesterT.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.SelectSemesterT.setAcceptDrops(True)
        self.SelectSemesterT.setObjectName(_fromUtf8("SelectSemesterT"))
        self.SelectSemesterT.addItem(_fromUtf8(""))
        self.SelectSemesterT.addItem(_fromUtf8(""))
        self.SelectSemesterT.addItem(_fromUtf8(""))
        self.SelectSemesterT.addItem(_fromUtf8(""))
        self.SelectSemesterT.addItem(_fromUtf8(""))
        self.SelectSemesterT.addItem(_fromUtf8(""))
        self.SelectSemesterT.addItem(_fromUtf8(""))
        self.SelectSemesterT.addItem(_fromUtf8(""))
        self.SelectSemesterT.addItem(_fromUtf8(""))
        self.SelectSectionT = QtGui.QComboBox(self.TrainImage)
        self.SelectSectionT.setGeometry(QtCore.QRect(170, 260, 161, 24))
        self.SelectSectionT.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.SelectSectionT.setAcceptDrops(True)
        self.SelectSectionT.setObjectName(_fromUtf8("SelectSectionT"))
        self.SelectSectionT.addItem(_fromUtf8(""))
        self.SelectSectionT.addItem(_fromUtf8(""))
        self.SelectSectionT.addItem(_fromUtf8(""))
        self.SelectSectionT.addItem(_fromUtf8(""))
        self.SelectSectionT.addItem(_fromUtf8(""))
        self.NameT = QtGui.QLineEdit(self.TrainImage)
        self.NameT.setGeometry(QtCore.QRect(170, 330, 161, 22))
        self.NameT.setObjectName(_fromUtf8("NameT"))
        self.tabWidget.addTab(self.TrainImage, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 515, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.SelectBranchC.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "(a)", None))
        self.label_2.setText(_translate("MainWindow", "Select Image Offline", None))
        self.label_3.setText(_translate("MainWindow", "(b)", None))
        self.label_4.setText(_translate("MainWindow", "Detect FRom Live Feed", None))
        #self.SelectButtonD.setText(_translate("MainWindow", "Select", None))
        self.DetectButtonD.setText(_translate("MainWindow", "Detect", None))
        self.CamButtonD.setText(_translate("MainWindow", "Open Cam For Detection", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DetectImage), _translate("MainWindow", "DETECTION", None))
        self.label_5.setText(_translate("MainWindow", "(a)", None))
        self.label_6.setText(_translate("MainWindow", "(b)", None))
        self.label_7.setText(_translate("MainWindow", "Select Image Offline", None))
        self.label_8.setText(_translate("MainWindow", "Recognised From Live Stream", None))
        #self.SelectButtonR.setText(_translate("MainWindow", "Select", None))
        self.DetectButtonR.setText(_translate("MainWindow", "Detect", None))
        self.CamButtonR.setText(_translate("MainWindow", "Open Cam For Detection", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RecogniseImage), _translate("MainWindow", "RECOGNISE", None))
        self.BranchC.setText(_translate("MainWindow", "Branch", None))
        self.SemesterC.setText(_translate("MainWindow", "Semester", None))
        self.SectionC.setText(_translate("MainWindow", "Section", None))
        self.NameC_2.setText(_translate("MainWindow", "Name", None))
        self.YearC.setText(_translate("MainWindow", "Year", None))
        self.CaptureButtonC.setText(_translate("MainWindow", "Capture", None))
        #self.TrainButtonC.setText(_translate("MainWindow", "Train", None))
        self.SelectBranchC.setItemText(0, _translate("MainWindow", "Select Branch", None))
        self.SelectBranchC.setItemText(1, _translate("MainWindow", "CSE", None))
        self.SelectBranchC.setItemText(2, _translate("MainWindow", "IT", None))
        self.SelectBranchC.setItemText(3, _translate("MainWindow", "ME", None))
        self.SelectBranchC.setItemText(4, _translate("MainWindow", "EC", None))
        self.SelectBranchC.setItemText(5, _translate("MainWindow", "CE", None))
        self.SelectYearC.setItemText(0, _translate("MainWindow", "Select Year", None))
        self.SelectYearC.setItemText(1, _translate("MainWindow", "2012", None))
        self.SelectYearC.setItemText(2, _translate("MainWindow", "2013", None))
        self.SelectYearC.setItemText(3, _translate("MainWindow", "2014", None))
        self.SelectYearC.setItemText(4, _translate("MainWindow", "2015", None))
        self.SelectYearC.setItemText(5, _translate("MainWindow", "2016", None))
        self.SelectYearC.setItemText(6, _translate("MainWindow", "2017", None))
        self.SelectSemesterC.setItemText(0, _translate("MainWindow", "Select Semester", None))
        self.SelectSemesterC.setItemText(1, _translate("MainWindow", "1", None))
        self.SelectSemesterC.setItemText(2, _translate("MainWindow", "2", None))
        self.SelectSemesterC.setItemText(3, _translate("MainWindow", "3", None))
        self.SelectSemesterC.setItemText(4, _translate("MainWindow", "4", None))
        self.SelectSemesterC.setItemText(5, _translate("MainWindow", "5", None))
        self.SelectSemesterC.setItemText(6, _translate("MainWindow", "6", None))
        self.SelectSemesterC.setItemText(7, _translate("MainWindow", "7", None))
        self.SelectSemesterC.setItemText(8, _translate("MainWindow", "8", None))
        self.SelectSectionC.setItemText(0, _translate("MainWindow", "Select Section", None))
        self.SelectSectionC.setItemText(1, _translate("MainWindow", "A", None))
        self.SelectSectionC.setItemText(2, _translate("MainWindow", "B", None))
        self.SelectSectionC.setItemText(3, _translate("MainWindow", "C", None))
        self.SelectSectionC.setItemText(4, _translate("MainWindow", "D", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CreateImage), _translate("MainWindow", "CREATE", None))
        self.BranchT.setText(_translate("MainWindow", "Branch", None))
        self.YearT.setText(_translate("MainWindow", "Year", None))
        self.SemesterT.setText(_translate("MainWindow", "Semester", None))
        self.SectionT.setText(_translate("MainWindow", "Section", None))
        self.NameT_2.setText(_translate("MainWindow", "Name", None))
        #self.CaptureButtonT.setText(_translate("MainWindow", "Capture", None))
        self.TrainButtonT.setText(_translate("MainWindow", "Train", None))
        self.SelectBranchT.setItemText(0, _translate("MainWindow", "Select Branch", None))
        self.SelectBranchT.setItemText(1, _translate("MainWindow", "CSE", None))
        self.SelectBranchT.setItemText(2, _translate("MainWindow", "IT", None))
        self.SelectBranchT.setItemText(3, _translate("MainWindow", "ME", None))
        self.SelectBranchT.setItemText(4, _translate("MainWindow", "EC", None))
        self.SelectBranchT.setItemText(5, _translate("MainWindow", "CE", None))
        self.SelectYearT.setItemText(0, _translate("MainWindow", "Select Year", None))
        self.SelectYearT.setItemText(1, _translate("MainWindow", "2012", None))
        self.SelectYearT.setItemText(2, _translate("MainWindow", "2013", None))
        self.SelectYearT.setItemText(3, _translate("MainWindow", "2014", None))
        self.SelectYearT.setItemText(4, _translate("MainWindow", "2015", None))
        self.SelectYearT.setItemText(5, _translate("MainWindow", "2016", None))
        self.SelectYearT.setItemText(6, _translate("MainWindow", "2017", None))
        self.SelectSemesterT.setItemText(0, _translate("MainWindow", "Select Semester", None))
        self.SelectSemesterT.setItemText(1, _translate("MainWindow", "1", None))
        self.SelectSemesterT.setItemText(2, _translate("MainWindow", "2", None))
        self.SelectSemesterT.setItemText(3, _translate("MainWindow", "3", None))
        self.SelectSemesterT.setItemText(4, _translate("MainWindow", "4", None))
        self.SelectSemesterT.setItemText(5, _translate("MainWindow", "5", None))
        self.SelectSemesterT.setItemText(6, _translate("MainWindow", "6", None))
        self.SelectSemesterT.setItemText(7, _translate("MainWindow", "7", None))
        self.SelectSemesterT.setItemText(8, _translate("MainWindow", "8", None))
        self.SelectSectionT.setItemText(0, _translate("MainWindow", "Select Section", None))
        self.SelectSectionT.setItemText(1, _translate("MainWindow", "A", None))
        self.SelectSectionT.setItemText(2, _translate("MainWindow", "B", None))
        self.SelectSectionT.setItemText(3, _translate("MainWindow", "C", None))
        self.SelectSectionT.setItemText(4, _translate("MainWindow", "D", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TrainImage), _translate("MainWindow", "TRAIN", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
   # ip = QtGui.PrettyWidget()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

