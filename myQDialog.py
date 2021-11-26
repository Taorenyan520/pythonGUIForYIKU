from PyQt5.QtWidgets import QDialog
from dialog import Ui_Dialog
from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtGui import QPalette

class QmyDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioRed.clicked.connect(self.do_setTextColor)
        self.ui.radioBlue.clicked.connect(self.do_setTextColor)
        self.ui.radioBlack.clicked.connect(self.do_setTextColor)

    def on_btnClear_clicked(self):
        self.ui.TextEdit.clear()

    def on_chkBoxBlod_toggled(self,checked):
        font = self.ui.TextEdit.font()
        font.setBold(checked)
        self.ui.TextEdit.setFont(font)

    def on_chkBoxUnder_clicked(self):
        checked = self.ui.chkBoxUnder.isChecked()
        font = self.ui.TextEdit.font()
        font.setUnderline(checked)
        self.ui.TextEdit.setFont(font)

    @pyqtSlot(bool)
    def on_chkBoxItalic_clicked(self,checked):
        font = self.ui.TextEdit.font()
        font.setItalic(checked)
        self.ui.TextEdit.setFont(font)

    def do_setTextColor(self):
        plet = self.ui.TextEdit.palette()
        if (self.ui.radioRed.isChecked()):
            plet.setColor(QPalette.Text,Qt.red)
        elif (self.ui.radioBlack.isChecked()):
            plet.setColor(QPalette.Text, Qt.black) # 颜色一定要小写
        elif (self.ui.radioBlue.isChecked()):
            plet.setColor(QPalette.Text, Qt.blue)
        self.ui.TextEdit.setPalette(plet)

