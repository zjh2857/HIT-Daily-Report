from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import requests
import os

user = os.environ["USER"]
password = os.environ["PASSWORD"]
location = os.environ["LOCATION"]
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
token = requests.post("https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xs/getToken",cookies={'JSESSIONID':sessionid}).text

data = f'''
{location}
'''

print(data)
data = data[:data.find("\"token\"")] + "\"token\":\"%s\"}"%token
print(data)
res = requests.post("https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsMrsbNew/save",data={"info":data},cookies={'JSESSIONID':sessionid}).text
print(res)
