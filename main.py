from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import requests
import os

user = os.environ["user"]
password = os.environ["password"]
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.get("https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsMrsbNew/edit")
comd = f'''
        document.getElementById('username').value='{user}';\n
        document.getElementById('password').value='{password}';\n
        document.getElementById('login_submit').click();
        '''
driver.execute_script(comd)
sessionid = driver.get_cookies()[0]['value']
driver.quit()
print(sessionid)
token = requests.post("https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xs/getToken",cookies={'JSESSIONID':sessionid}).text
print(token)

data = '''
{"model":{"gpsjd":126.631834,"gpswd":45.729538,"jzdz":"","kzl1":"1","kzl2":"","kzl3":"","kzl4":"","kzl5":"","kzl6":"黑龙江省","kzl7":"哈尔滨市","kzl8":"南岗区","kzl9":"新苗圃街57号","kzl10":"黑龙江省哈尔滨市南岗区新苗圃街57号","kzl11":"","kzl12":"","kzl13":"0","kzl14":"","kzl15":"0","kzl16":"","kzl17":"1","kzl18":"0;","kzl19":"","kzl20":"","kzl21":"","kzl22":"","kzl23":"0","kzl24":"0","kzl25":"","kzl26":"","kzl27":"","kzl28":"0","kzl29":"","kzl30":"","kzl31":"","kzl32":"2","kzl33":"","kzl34":{},"kzl38":"黑龙江省","kzl39":"哈尔滨市","kzl40":"南岗区","kzl41":"0","kzl42":""},"token":"%s"}
'''%(token)
res = requests.post("https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsMrsbNew/save",data={"info":data},cookies={'JSESSIONID':sessionid}).text
print(res)
