# coding=gbk
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

if __name__ == '__main__':
    # ����getֱ�ӷ��أ����ٵȴ�����������
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["pageLoadStrategy"] = "none"
    chrome_options = webdriver.ChromeOptions()
    # �޴���ģʽ
    # chrome_options.add_argument('--headless')
    # ��ֹӲ�����٣���������ռ��cpu
    chrome_options.add_argument('--disable-gpu')
    # �رհ�ȫ����
    chrome_options.add_argument("disable-web-security")
    # ��ֹͼƬ����
    # chrome_options.add_experimental_option('prefs', {'profile.managed_default_content_settings.images': 2})
    # ����"Chrome�����ܵ��Զ�����Ŀ���
    chrome_options.add_argument('disable-infobars')
    # ���ÿ�����ģʽ��������ģʽ��webdriver����Ϊ����ֵ
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # ģ�������
    chrome_options.add_argument(
        'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"')
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.com")
    driver.add_cookie({'name':'session-id','value':'147-4744469-5639660','domain':'.amazon.com','path':'/'})
    driver.add_cookie({'name': 'session-id-time', 'value': '2082787201l', 'domain': '.amazon.com', 'path': '/'})
    driver.add_cookie({'name': 'i18n-prefs', 'value': 'USD', 'domain': '.amazon.com', 'path': '/'})
    driver.add_cookie({'name': 'lc-main', 'value': 'en_US', 'domain': '.amazon.com', 'path': '/'})
    driver.add_cookie({'name': 'ubid-main', 'value': '131-5871659-1812530', 'domain': '.amazon.com', 'path': '/'})
    driver.add_cookie({'name': 'session-token', 'value': '"WsNXcrR5BzTVA3crtERrCKpvwVhB52g8XGjzQBKrqrTwpnxwo4JUS0UCRQIjU6tf0ivY2lf2zK60tSc8dtg+9d0MGSkPxZbygeBLz6N65VCnP1Q51Li7SfKbE31kSNT2pKOnj1wGAI2mUN6nA+mAe3S9LQG/wZ3dveTn7DI7PUveQMhLA007+JvRoYcysUsXLNdRnCo0osxBIQVYfBNgSurT22Og/cfLCTbmdSnhBHPUVgjzIObTTNNNyLzZc+L9t0d6TzOByeM="', 'domain': '.amazon.com', 'path': '/'})
    # �̶��������ݣ��仯��ֻ��ҳ��

    search_page_url = "https://www.amazon.com/s?k={}&page={}&qid=1639730568&ref=sr_pg_{}"
    keyword = input("������׼ȷ�Ĺؼ��ʣ�")
    for i in range(1, 2):
        print("������ȡ", search_page_url.format(keyword,i,i))
        driver.get(search_page_url.format(keyword,i,i))
        date = str(driver.page_source)
        info = date.replace('\n', '')
        with open(keyword+'.txt', 'w',encoding='utf-8') as output_file:
            output_file.write(info)
        time.sleep(3)
    print(time.strftime("end %Y-%m-%d %H:%M:%S", time.localtime()))
    driver.quit()
