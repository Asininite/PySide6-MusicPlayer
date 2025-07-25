# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MusicUI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,
    QMetaObject, QRect,
    QSize, Qt)
from PySide6.QtGui import (QAction,QFont,QIcon)
from PySide6.QtWidgets import (QHBoxLayout, QLabel,
    QMenu, QMenuBar, QSizePolicy, QSlider,
    QSpacerItem, QStatusBar, QToolButton, QVBoxLayout,
    QWidget)
import resources


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 150)
        self.actionOpen_Music = QAction(MainWindow)
        self.actionOpen_Music.setObjectName(u"actionOpen_Music")
        self.actionOpen_Playlist = QAction(MainWindow)
        self.actionOpen_Playlist.setObjectName(u"actionOpen_Playlist")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSliderPlay = QSlider(self.centralwidget)
        self.horizontalSliderPlay.setObjectName(u"horizontalSliderPlay")
        self.horizontalSliderPlay.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.horizontalSliderPlay)

        self.labelTimer = QLabel(self.centralwidget)
        self.labelTimer.setObjectName(u"labelTimer")
        font = QFont()
        font.setPointSize(14)
        self.labelTimer.setFont(font)

        self.horizontalLayout.addWidget(self.labelTimer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.toolButtonPlay = QToolButton(self.centralwidget)
        self.toolButtonPlay.setObjectName(u"toolButtonPlay")
        icon = QIcon()
        icon.addFile(u":/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonPlay.setIcon(icon)
        self.toolButtonPlay.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.toolButtonPlay)

        self.toolButtonStop = QToolButton(self.centralwidget)
        self.toolButtonStop.setObjectName(u"toolButtonStop")
        icon2 = QIcon()
        icon2.addFile(u":/icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonStop.setIcon(icon2)
        self.toolButtonStop.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.toolButtonStop)

        self.toolButtonPrevious = QToolButton(self.centralwidget)
        self.toolButtonPrevious.setObjectName(u"toolButtonPrevious")
        icon_prev = QIcon()
        icon_prev.addFile(u":/icons/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonPrevious.setIcon(icon_prev)
        self.toolButtonPrevious.setIconSize(QSize(32, 32))
        self.horizontalLayout_2.addWidget(self.toolButtonPrevious)

        self.toolButtonNext = QToolButton(self.centralwidget)
        self.toolButtonNext.setObjectName(u"toolButtonNext")
        icon_next = QIcon()
        icon_next.addFile(u":/icons/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonNext.setIcon(icon_next)
        self.toolButtonNext.setIconSize(QSize(32, 32))
        self.horizontalLayout_2.addWidget(self.toolButtonNext)

        self.horizontalSpacer = QSpacerItem(338, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        # START: ADD THIS CODE
        self.toolButtonLike = QToolButton(self.centralwidget)
        self.toolButtonLike.setObjectName(u"toolButtonLike")
        icon4 = QIcon()
        # This assumes you will add 'heart-outline.png' to your resources
        icon4.addFile(u":/icons/heart-outline.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonLike.setIcon(icon4)
        self.toolButtonLike.setIconSize(QSize(32, 32))
        self.toolButtonLike.setCheckable(True) # Makes the button act like a toggle
        self.horizontalLayout_2.addWidget(self.toolButtonLike)
        # END: ADD THIS CODE

        self.toolButtonVolume = QToolButton(self.centralwidget)
        self.toolButtonVolume.setObjectName(u"toolButtonVolume")
        icon3 = QIcon()
        icon3.addFile(u":/icons/volume.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButtonVolume.setIcon(icon3)
        self.toolButtonVolume.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.toolButtonVolume)

        self.horizontalSliderVolume = QSlider(self.centralwidget)
        self.horizontalSliderVolume.setObjectName(u"horizontalSliderVolume")
        self.horizontalSliderVolume.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.horizontalSliderVolume)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen_Music)
        self.menuFile.addAction(self.actionOpen_Playlist)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_Music.setText(QCoreApplication.translate("MainWindow", u"Open Music", None))
        self.actionOpen_Playlist.setText(QCoreApplication.translate("MainWindow", u"Open Playlist", None))
        self.labelTimer.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.toolButtonPlay.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButtonStop.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButtonPrevious.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButtonNext.setText(QCoreApplication.translate("MainWindow", u"...", None))
         # START: ADD THIS LINE
        self.toolButtonLike.setText(QCoreApplication.translate("MainWindow", u"...", None))
        # END: ADD THIS LINE
        self.toolButtonVolume.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

