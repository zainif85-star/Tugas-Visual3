# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formPengaduan.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(240, 150, 56, 18))
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(100, 20, 160, 113))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.idPengaduanLabel = QLabel(self.formLayoutWidget)
        self.idPengaduanLabel.setObjectName(u"idPengaduanLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.idPengaduanLabel)

        self.EditId = QLineEdit(self.formLayoutWidget)
        self.EditId.setObjectName(u"EditId")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.EditId)

        self.divisiLabel = QLabel(self.formLayoutWidget)
        self.divisiLabel.setObjectName(u"divisiLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.divisiLabel)

        self.ComboDivisi = QComboBox(self.formLayoutWidget)
        self.ComboDivisi.addItem("")
        self.ComboDivisi.addItem("")
        self.ComboDivisi.addItem("")
        self.ComboDivisi.addItem("")
        self.ComboDivisi.addItem("")
        self.ComboDivisi.setObjectName(u"ComboDivisi")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.ComboDivisi)

        self.tanggalLabel = QLabel(self.formLayoutWidget)
        self.tanggalLabel.setObjectName(u"tanggalLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.tanggalLabel)

        self.EditTanggal = QDateEdit(self.formLayoutWidget)
        self.EditTanggal.setObjectName(u"EditTanggal")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.EditTanggal)

        self.keteranganLabel = QLabel(self.formLayoutWidget)
        self.keteranganLabel.setObjectName(u"keteranganLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.keteranganLabel)

        self.EditKeterangan = QLineEdit(self.formLayoutWidget)
        self.EditKeterangan.setObjectName(u"EditKeterangan")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.EditKeterangan)

        self.statusLabel = QLabel(self.formLayoutWidget)
        self.statusLabel.setObjectName(u"statusLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.statusLabel)

        self.ComboStatus = QComboBox(self.formLayoutWidget)
        self.ComboStatus.addItem("")
        self.ComboStatus.addItem("")
        self.ComboStatus.setObjectName(u"ComboStatus")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.ComboStatus)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(80, 150, 56, 18))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(160, 150, 56, 18))
        self.tabelAnggota = QTableWidget(Form)
        if (self.tabelAnggota.columnCount() < 5):
            self.tabelAnggota.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelAnggota.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelAnggota.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelAnggota.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelAnggota.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelAnggota.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelAnggota.setObjectName(u"tabelAnggota")
        self.tabelAnggota.setGeometry(QRect(20, 190, 361, 81))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.idPengaduanLabel.setText(QCoreApplication.translate("Form", u"Id Pengaduan", None))
        self.divisiLabel.setText(QCoreApplication.translate("Form", u"Divisi", None))
        self.ComboDivisi.setItemText(0, QCoreApplication.translate("Form", u"Pelayanan", None))
        self.ComboDivisi.setItemText(1, QCoreApplication.translate("Form", u"Infrastruktur", None))
        self.ComboDivisi.setItemText(2, QCoreApplication.translate("Form", u"Kebersihan", None))
        self.ComboDivisi.setItemText(3, QCoreApplication.translate("Form", u"Keamanan", None))
        self.ComboDivisi.setItemText(4, QCoreApplication.translate("Form", u"Sosial", None))

        self.tanggalLabel.setText(QCoreApplication.translate("Form", u"Tanggal", None))
        self.keteranganLabel.setText(QCoreApplication.translate("Form", u"Keterangan", None))
        self.statusLabel.setText(QCoreApplication.translate("Form", u"Status", None))
        self.ComboStatus.setItemText(0, QCoreApplication.translate("Form", u"Diterima", None))
        self.ComboStatus.setItemText(1, QCoreApplication.translate("Form", u"Ditolak", None))

        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        ___qtablewidgetitem = self.tabelAnggota.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Id Pengaduan", None));
        ___qtablewidgetitem1 = self.tabelAnggota.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Divisi", None));
        ___qtablewidgetitem2 = self.tabelAnggota.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Tanggal", None));
        ___qtablewidgetitem3 = self.tabelAnggota.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Keterangan", None));
        ___qtablewidgetitem4 = self.tabelAnggota.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Status", None));
    # retranslateUi

