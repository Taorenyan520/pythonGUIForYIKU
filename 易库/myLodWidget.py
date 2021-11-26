from PyQt5.QtWidgets import QWidget
from lodingwidget import Ui_LodingWidget


from UseSQL import UseSQL

class myLodWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_LodingWidget()
        self.ui.setupUi(self)
        self.ui.pushButtonLog.clicked.connect(self.on_pushButtonLog_clicked)

    def on_pushButtonLog_clicked(self):
        user = self.ui.lineEditUser.text()
        password = self.ui.lineEditPassword.text()
        if user=="":
            print("用户名为空！请输入用户名！")
        elif password=="":
            print("密码为空！请输入密码！")
        else:
            user_info = UseSQL()
            condition = "user_name = '"+user+"'"
            info = "user_password"
            data = user_info.selectSQL(tab='user_info',condition=condition,info=info)
            print(data)
            if password == data[0][0]:
                print("登录成功！")
            else:
                print("密码错误！登录失败！")

