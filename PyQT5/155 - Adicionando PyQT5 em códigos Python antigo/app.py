import sys
from validacpf import valida_cpf
from geradorcpf import gera_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow
import design


class GeraValidaCPF(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGeraCPF.clicked.connect(self.gera_cpf)
        self.btnValidaCPF.clicked.connect(self.valida_cpf)

    def gera_cpf(self):
        self.labelRetorno.setText(
            str(gera_cpf())
        )

    def valida_cpf(self):
        cpf = self.inputValidaCPF.text()
        self.labelRetorno.setText(
            str(valida_cpf(cpf))
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida_cpf = GeraValidaCPF()
    gera_valida_cpf.show()
    qt.exec_()
