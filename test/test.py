import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import undetected_chromedriver as uc
from faker import Faker
import random

faker = Faker()
init(autoreset=True)

# دالة لفحص البروكسي
def thread_check_proxy(proxy):
    try:
        # محاولة الاتصال بالموقع باستخدام البروكسي
        print(f"Checking proxy: {proxy}")
        
        # إعداد البروكسي مع بيانات الاعتماد
        proxies = {
            "http": f"http://{proxy['user']}:{proxy['pass']}@{proxy['host']}:{proxy['port']}",
            "https": f"http://{proxy['user']}:{proxy['pass']}@{proxy['host']}:{proxy['port']}"
        }
        
        # محاولة الاتصال بالموقع
        response = requests.get("http://google.com", proxies=proxies, timeout=5)
  
        if response.status_code == 200:
            print(Fore.GREEN + f"GOOD: Proxy {proxy['host']}:{proxy['port']} is working!")  # اللون الأخضر
        else:
            print(Fore.RED + f"BAD: Proxy {proxy['host']}:{proxy['port']} failed with status code {response.status_code}")  # اللون الأحمر
    
    except requests.RequestException as e:
        # في حالة حدوث خطأ
        print(Fore.RED + f"BAD: Error with proxy {proxy['host']}:{proxy['port']}: {e}")  # اللون الأحمر

# بيانات البروكسي
proxy = {
    "host": "resi-ww.lightningproxies.net",
    "port": "9999",
    "user": "sfbrxuufteprixr115446-zone-resi",
    "pass": "ljgdacsxij"
}

def generate_random_user_data():
    name = faker.name().split(' ')
    first_name = name[0]
    last_name = ' '.join(name[1:])
    password = faker.password()
    return first_name, last_name, password

def generate_random_username():
    first_name, last_name, _ = generate_random_user_data()
    number = random.randint(1000, 9999) 
    username = f"{first_name}{last_name}{number}"
    return username

options = uc.ChromeOptions()
# إضافة البروكسي لمتصفح Chrome
options.add_argument(f"--proxy-server=http://{proxy['user']}:{proxy['pass']}@{proxy['host']}:{proxy['port']}")
options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--lang=en-US")
options.add_argument('--incognito')  # وضع التصفح الخفي
options.add_argument("--proxy-server=https://username:password@proxy_host:proxy_port")


proxy = {
    "host": "resi-ww.lightningproxies.net",
    "port": "9999",
}
options.add_argument(f"--proxy-server=http://{proxy['host']}:{proxy['port']}")



driver = uc.Chrome(options=options)
driver.set_window_position(1, 1)
driver.set_window_size(900, 700)

try:
    driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Faccounts.google.com%2F")
    first_name, last_name, password = generate_random_user_data()

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//button[span[text()="Create account"]]'))).click()
    time.sleep(0.3)

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div[2]/div/div/div[2]/div/ul/li[1]'))).click()
    time.sleep(0.2)
    
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="firstName"]'))).send_keys(first_name)
    time.sleep(0.3)

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="lastName"]'))).send_keys(last_name)
    time.sleep(0.3)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="collectNameNext"]/div/button'))).click()
    time.sleep(0.2)

    select = Select(WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "month"))))
    select.select_by_value("1") 
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="day"]'))).send_keys("15")
    time.sleep(0.3)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="year"]'))).send_keys("1990")
    time.sleep(0.3)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gender"]'))).send_keys("Male")
    time.sleep(0.2)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="birthdaygenderNext"]/div/button'))).click()
    time.sleep(0.3)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'//input[@name="Username"]'))).send_keys(generate_random_username())
    time.sleep(0.2)

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="next"]'))).click()
    time.sleep(0.3)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '(//input[@type="password"])[1]'))).send_keys("www421qqq")
    time.sleep(0.2)

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '(//input[@type="password"])[2]'))).send_keys("www421qqq")
    time.sleep(0.2)

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="createpasswordNext"]/div/button'))).click()
    time.sleep(0.2)

    print(f"{first_name}:{last_name}:{password}")
    time.sleep(1)
    print(f"{generate_random_username}")

finally:
    time.sleep(13330)
    driver.quit()
    print("Driver closed successfully.")

# استخدام ThreadPoolExecutor لفحص البروكسي
with ThreadPoolExecutor() as executor:
    executor.map(thread_check_proxy, [proxy])
