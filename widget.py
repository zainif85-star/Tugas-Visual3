import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from pengaduan import form_pengaduan
from tindakan import form_tindakan


class main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya=QFile('form.ui')
        filenya.open(QFile.ReadOnly)
        muatFile=QUiLoader()
        self.formUtama=muatFile.load(filenya,self)
        self.setMenuBar(self.formUtama.menuBar())
        self.resize(self.formUtama.size())
        #actionForm_Pengaduan
        self.formUtama.actionForm_Pengaduan.triggered.connect(self.bukaPengaduan)
        #actionForm_Tindakan
        self.formUtama.actionForm_Tindakan.triggered.connect(self.bukaTindakan)

    def bukaPengaduan(self):
        self.buka=form_pengaduan()
        self.buka.show()

    def bukaTindakan(self):
        self.buka=form_tindakan()
        self.buka.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    window.show()          # <- PENTING: tampilkan window
    sys.exit(app.exec())
