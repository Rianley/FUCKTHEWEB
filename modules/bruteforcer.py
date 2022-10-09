from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from modules.geturls import first_judg
from utils.output_utils import print_inf

# 启动chrome selenium
opt = Options()
opt.add_argument('--headless')
cdriver = webdriver.Chrome('chromedriver/chromedriver.exe', options=opt)  # win c driver
cdriver.implicitly_wait(100)  # wait
print_inf('selenium启动成功')


# 单个url爆破函数
def bruteforcer(url):
    first_judg(url)
    cdriver.get(url)
    cdriver.implicitly_wait(100)  # wait
