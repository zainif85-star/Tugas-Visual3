# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formTindakan.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(80, 150, 56, 18))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(240, 150, 56, 18))
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(110, 40, 160, 81))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.idPengaduanLabel = QLabel(self.formLayoutWidget)
        self.idPengaduanLabel.setObjectName(u"idPengaduanLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.idPengaduanLabel)

        self.EditId = QLineEdit(self.formLayoutWidget)
        self.EditId.setObjectName(u"EditId")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.EditId)

        self.tanggalLabel = QLabel(self.formLayoutWidget)
        self.tanggalLabel.setObjectName(u"tanggalLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.tanggalLabel)

        self.EditTanggal = QDateEdit(self.formLayoutWidget)
        self.EditTanggal.setObjectName(u"EditTanggal")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.EditTanggal)

        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(160, 150, 56, 18))
        self.tabelAnggota = QTableWidget(Form)
        if (self.tabelAnggota.columnCount() < 2):
            self.tabelAnggota.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelAnggota.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelAnggota.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tabelAnggota.setObjectName(u"tabelAnggota")
        self.tabelAnggota.setGeometry(QRect(100, 190, 221, 81))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.idPengaduanLabel.setText(QCoreApplication.translate("Form", u"Id Tindakan", None))
        self.tanggalLabel.setText(QCoreApplication.translate("Form", u"Tanggal", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        ___qtablewidgetitem = self.tabelAnggota.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Id Tindakan", None));
        ___qtablewidgetitem1 = self.tabelAnggota.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Tanggal", None));
    # retranslateUi

