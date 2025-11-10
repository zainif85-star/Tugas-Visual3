# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud_pengaduan import crud


class form_pengaduan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya=QFile('formPengaduan.ui')
        filenya.open(QFile.ReadOnly)
        muatFile=QUiLoader()
        self.formPengaduan=muatFile.load(filenya,self)
        self.mycrud=crud()
        self.formPengaduan.btnSimpan.clicked.connect(self.doSimpanPengaduan)
        self.formPengaduan.btnUbah.clicked.connect(self.doUbahPengaduan)
        self.formPengaduan.btnHapus.clicked.connect(self.doHapusPengaduan)

    def doSimpanPengaduan(self):
        tempid=self.formPengaduan.EditId.text()
        tempdivisi=self.formPengaduan.ComboDivisi.currentText()
        temptanggal=self.formPengaduan.EditTanggal.date().toString("yyyy-MM-dd")
        tempketerangan=self.formPengaduan.EditKeterangan.text()
        tempstatus=self.formPengaduan.ComboStatus.currentText()
        self.mycrud.simpanPengaduan(tempid, tempdivisi, temptanggal, tempketerangan, tempstatus)

    def doUbahPengaduan(self):
        tempid=self.formPengaduan.EditId.text()
        tempdivisi=self.formPengaduan.ComboDivisi.currentText()
        temptanggal=self.formPengaduan.EditTanggal.date().toString("yyyy-MM-dd")
        tempketerangan=self.formPengaduan.EditKeterangan.text()
        tempstatus=self.formPengaduan.ComboStatus.currentText()
        self.mycrud.ubahPengaduan(tempid, tempdivisi, temptanggal, tempketerangan, tempstatus)

    def doHapusPengaduan(self):
        tempid=self.formPengaduan.EditId.text()
        self.mycrud.hapusPengaduan(tempid)

