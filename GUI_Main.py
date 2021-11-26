import sys
from PyQt5.QtWidgets import QApplication
from myQDialog import QmyDialog
from UseSQL import UseSQL

info = UseSQL()
data = info.selectSQL()
app = QApplication(sys.argv)
myQDialog = QmyDialog()
banbeng = myQDialog.ui.TextEdit.toPlainText()
print(banbeng)
if banbeng == data[0][0]:
    myQDialog.show()
    sys.exit(app.exec_())
else:
    print("请联系管理员更新版本！")
