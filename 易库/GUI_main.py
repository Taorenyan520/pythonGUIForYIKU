import sys
from PyQt5.QtWidgets import QApplication
from myLodWidget import myLodWidget
from UseSQL import UseSQL

info = UseSQL()
data = info.selectSQL()
app = QApplication(sys.argv)
myLodWidget = myLodWidget()
banbeng = myLodWidget.ui.VersionLab.text()
print(banbeng)
if banbeng == data[0][0]:
    myLodWidget.show()
    sys.exit(app.exec_())
else:
    print("请联系管理员更新版本！")
