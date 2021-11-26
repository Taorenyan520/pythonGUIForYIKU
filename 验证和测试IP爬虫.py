import requests,pymssql
#链接数据库函数
def conn():
    connect = pymssql.connect('(local)', 'sa', 'clf512014', 'PC_CLF') #服务器名,账户,密码,数据库名
    if connect:
        print("连接成功!")
    return connect
conn = conn()
cursor = conn.cursor()
sql = "select * from IP_info"
cursor.execute(sql)
data = cursor.fetchall()
for i in data:
    ip = i[0]
    url = 'https://www.amazon.com'
    proxies = {
        "http": "http://" + ip
    }

    # 使用IP代理访问amazon，测试代理地址是否有效
    try:
        data = requests.get(url=url, proxies=proxies, timeout=5)
        sql = "update IP_info set 是否存活='是' where IP = '"+ip+"'"
        cursor.execute(sql)
        conn.commit()
        print(ip +":yes")
    except:
        sql = "update IP_info set 是否存活='否' where IP = '" + ip + "'"
        cursor.execute(sql)
        conn.commit()
        print(ip + ":NO")
cursor.close()   #关闭游标
conn.close()
