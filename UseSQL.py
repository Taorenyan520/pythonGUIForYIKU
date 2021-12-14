import pymssql
class UseSQL():
    def __init__(self):
        self.IP = 'gudao19.is-very-good.org'
        self.SQLDataBase = 'work_in_dada'
        self.SQLUser = 'sa'
        self.SQLPassword = 'yikupassword123'
        self.port = '33614'
        self.connect = pymssql.connect(host=self.IP, user=self.SQLUser, password=self.SQLPassword, database=self.SQLDataBase,
                           charset='utf8', port=self.port)

    def selectSQL(self,tab = "banbeng_info",info="*",condition=None,joininfo=None):
        cursor = self.connect.cursor()
        print("链接数据库成功！")
        if condition is None:
            cdt = ""
        else:
            cdt = " where "+ condition
        if joininfo is None:
            join = ""
        else:
            join = "left join" + joininfo
        sqlinfo = "select "+info+" from "+tab+join+cdt
        print(sqlinfo)
        try:
            cursor.execute(sqlinfo)
            data = cursor.fetchall()
            cursor.close()
            print("数据查询成功！")
            return data
        except:
            cursor.close()
            print("查询失败！")


    def updateSQL(self,setinfo,condition,tab="product_info"):
        cursor = self.connect.cursor()
        print("链接数据库成功！")
        sqlinfo = "update " + tab + " set " + setinfo + "where" + condition
        try:
            cursor.execute(sqlinfo)
            cursor.close()
            print("数据更新成功！")
        except:
            cursor.close()
            print("数据更新失败！")


    def insertSQL(self,tab,values,valuesinfo=None):
        cursor = self.connect.cursor()
        print("链接数据库成功！")
        if valuesinfo in None:
            info = ""
        else:
            info = "("+valuesinfo+")"
        sqlinfo = "insert into " + tab + info + "values (" + values+")"
        try:
            cursor.execute(sqlinfo)
            cursor.close()
            print("数据上传成功！")
        except:
            cursor.close()
            print("数据上传失败！")
