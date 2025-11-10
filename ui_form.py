# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionForm_Pengaduan = QAction(MainWindow)
        self.actionForm_Pengaduan.setObjectName(u"actionForm_Pengaduan")
        self.actionForm_Tindakan = QAction(MainWindow)
        self.actionForm_Tindakan.setObjectName(u"actionForm_Tindakan")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 18))
        self.menuHalaman_Aplikasi = QMenu(self.menubar)
        self.menuHalaman_Aplikasi.setObjectName(u"menuHalaman_Aplikasi")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHalaman_Aplikasi.menuAction())
        self.menuHalaman_Aplikasi.addAction(self.actionForm_Pengaduan)
        self.menuHalaman_Aplikasi.addAction(self.actionForm_Tindakan)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionForm_Pengaduan.setText(QCoreApplication.translate("MainWindow", u"Form Pengaduan", None))
        self.actionForm_Tindakan.setText(QCoreApplication.translate("MainWindow", u"Form Tindakan", None))
        self.menuHalaman_Aplikasi.setTitle(QCoreApplication.translate("MainWindow", u"Halaman Aplikasi", None))
    # retranslateUi

