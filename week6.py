import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider, QVBoxLayout, QGroupBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette

class AplikasiSlider(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 6")
        self.setFixedSize(750, 500)
        self.inisialisasiUI()

    def inisialisasiUI(self):
        layout = QVBoxLayout()

        self.lbl_nim = QLabel("F1D022137")
        self.lbl_nim.setFont(QFont("Arial", 30))
        self.lbl_nim.setAlignment(Qt.AlignCenter)
        self.lbl_nim.setAutoFillBackground(True)
        self.lbl_nim.setFixedHeight(100)
        self.lbl_nim.setWordWrap(True)
        layout.addWidget(self.lbl_nim)

        grup_ukuran = self.buatGrupSlider("Ukuran Huruf", 20, 60, self.ubahUkuranFont)
        layout.addWidget(grup_ukuran)

        grup_warna_font = self.buatGrupSlider("Warna Huruf", 0, 255, self.ubahWarnaFont)
        layout.addWidget(grup_warna_font)

        grup_warna_bg = self.buatGrupSlider("Warna Latar", 0, 255, self.ubahWarnaLatar)
        layout.addWidget(grup_warna_bg)

        # Nama dan NIM
        lbl_nama = QLabel("Nama: Muh. Ressa | NIM: F1D022137")
        lbl_nama.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl_nama)

        self.setLayout(layout)

    def buatGrupSlider(self, judul, min_val, max_val, fungsi):
        grup = QGroupBox(judul)
        tata = QVBoxLayout()

        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min_val)
        slider.setMaximum(max_val)
        slider.setValue((min_val + max_val) // 2)
        slider.valueChanged.connect(fungsi)
        tata.addWidget(slider)

        grup.setLayout(tata)
        return grup

    def ubahUkuranFont(self, nilai):
        font = self.lbl_nim.font()
        font.setPointSize(nilai)
        self.lbl_nim.setFont(font)

    def ubahWarnaFont(self, nilai):
        warna = QColor(nilai, nilai, nilai)
        palet = self.lbl_nim.palette()
        palet.setColor(QPalette.WindowText, warna)
        self.lbl_nim.setPalette(palet)

    def ubahWarnaLatar(self, nilai):
        warna = QColor(nilai, nilai, nilai)
        palet = self.lbl_nim.palette()
        palet.setColor(QPalette.Window, warna)
        self.lbl_nim.setPalette(palet)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AplikasiSlider() 
    window.show()
    sys.exit(app.exec_())
