# This Python file uses the following encoding: utf-8
import mysql.connector

class crud:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_pengaduan'
        )

    def simpanPengaduan(self, id, dvs, tgl, ktrg, sts):
        cekkursor = self.koneksi.cursor()
        sql = "INSERT INTO pengaduan (IdPengaduan, divisi, tanggal, keterangan, status) VALUES (%s, %s, %s, %s, %s)"
        val = (id, dvs, tgl, ktrg, sts)
        cekkursor.execute(sql, val)
        self.koneksi.commit()
        cekkursor.close()

    def ubahPengaduan(self, id, dvs, tgl, ktrg, sts):
        cekkursor = self.koneksi.cursor()
        sql = "UPDATE pengaduan SET divisi=%s, tanggal=%s, keterangan=%s, status=%s WHERE IdPengaduan=%s"
        val = (dvs, tgl, ktrg, sts, id)
        cekkursor.execute(sql, val)
        self.koneksi.commit()
        cekkursor.close()

    def hapusPengaduan(self, id):
        cekkursor = self.koneksi.cursor()
        sql = "DELETE FROM pengaduan WHERE IdPengaduan=%s"
        val = (id,)
        cekkursor.execute(sql, val)
        self.koneksi.commit()
        cekkursor.close()


    def simpanTindakan(self, id, tgl):
        cekkursor = self.koneksi.cursor()
        sql = "INSERT INTO tindakan (IdTindakan, tanggal) VALUES (%s, %s)"
        val = (id, tgl)
        cekkursor.execute(sql, val)
        self.koneksi.commit()
        cekkursor.close()

    def ubahTindakan(self, id, tgl):
        cekkursor = self.koneksi.cursor()
        sql = "UPDATE tindakan SET tanggal=%s WHERE IdTindakan=%s"
        val = (tgl, id)
        cekkursor.execute(sql, val)
        self.koneksi.commit()
        cekkursor.close()

    def hapusTindakan(self, id):
        cekkursor = self.koneksi.cursor()
        sql = "DELETE FROM tindakan WHERE IdTindakan=%s"
        val = (id,)
        cekkursor.execute(sql, val)
        self.koneksi.commit()
        cekkursor.close()
