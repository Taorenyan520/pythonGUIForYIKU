import requests,pymssql,re,time
#链接数据库函数
def conn():
    connect = pymssql.connect('(local)', 'sa', 'clf512014', 'PC_CLF') #服务器名,账户,密码,数据库名
    if connect:
        print("连接成功!")
    return connect

conn = conn()
cursor = conn.cursor()   #创建一个游标对象,python里的sql语句都要通过cursor来执行

#获取免费IP网站的网页信息
for i in range(39,90):
    url = 'http://www.taiyanghttp.com/free/page'+ str(i+1)
    print(url)
    html = requests.get(url)
    html.encoding = "utf-8"
    data = html.text
    print(data)
    f1 = open('../test.txt', 'w')
    f1.write(data)
    f1.close()
    f2 = open('../test.txt', 'r+')
    data = f2.read()
    info = data.replace('\n', '')
    print(info)
    #将网页信息中有用的信息通过正则表达式获取
    pattern1 = re.compile(
           r'<div class="tr ip_tr">                            <div class="td td-4">(.*?)</div>                            <div class="td td-2">(.*?)</div>                            <div class="td td-2">(.*?)</div>                            <div class="td td-2">(.*?)</div>                            <div class="td td-2">(.*?)</div>                                <div class="td td-2">(.*?)</div>                            <div class="td td-2">(.*?)</div>                                <div class="td td-4">(.*?)</div>                            <div class="td td-2">(.*?)</div>'
    )
    try:
        result1 = pattern1.findall(info)
        print(result1)
        for x in result1:
            ipdata = x[0]  # IP
            dkdata = x[1]  # 端口
            dzdata = x[2]  # 地址
            fwsdata = x[3]  # 服务商
            sjdata = x[4]  # 开通时间
            djdata = x[5]  # 等级
            lxdata = x[6]  # 类型
            print(
                "ip:" + ipdata + "\n" + "端口:" + dkdata + "\n" + "地址:" + dzdata + "\n" + "服务商:" + fwsdata + "\n" + "开通时间:" + sjdata + "\n" + "等级:" + djdata + "\n" + "类型:" + lxdata + "\n")
            sql = "insert into IP_info (IP,端口,地址,服务商,类型,等级,开通时间,是否存活) values ('" + ipdata + "','" + dkdata + "','" + dzdata + "','" + fwsdata + "','" + lxdata + "','" + djdata + "','" + sjdata + "','未知')"
            cursor.execute(sql)  # 执行sql语句
            conn.commit()  # 提交
    except:
        pass
    time.sleep(5)
cursor.close()   #关闭游标
conn.close()

