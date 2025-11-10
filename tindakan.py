# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud_pengaduan import crud


class form_tindakan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya=QFile('formTindakan.ui')
        filenya.open(QFile.ReadOnly)
        muatFile=QUiLoader()
        self.formTindakan=muatFile.load(filenya,self)
        self.mycrud=crud()
        self.formTindakan.btnSimpan.clicked.connect(self.doSimpanTindakan)
        self.formTindakan.btnUbah.clicked.connect(self.doUbahTindakan)
        self.formTindakan.btnHapus.clicked.connect(self.doHapusTindakan)

    def doSimpanTindakan(self):
        tempid=self.formTindakan.EditId.text()
        temptanggal=self.formTindakan.EditTanggal.date().toString("yyyy-MM-dd")
        self.mycrud.simpanTindakan(tempid, temptanggal)

    def doUbahTindakan(self):
        tempid=self.formTindakan.EditId.text()
        temptanggal=self.formTindakan.EditTanggal.date().toString("yyyy-MM-dd")
        self.mycrud.ubahTindakan(tempid, temptanggal)

    def doHapusTindakan(self):
        tempid=self.formTindakan.EditId.text()
        self.mycrud.hapusTindakan(tempid)

