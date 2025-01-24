import requests
import random
import undetected_chromedriver as uc
from selenium import webdriver

# URL of the proxy list
url = "https://proxylist.geonode.com/api/proxy-list?country=KH&limit=500&page=1&sort_by=lastChecked&sort_type=desc"

# Fetch the proxy list
response = requests.get(url)
proxies_data = response.json()  # Assuming the response is in JSON format

# Extract proxies from the response
proxies = []
for proxy in proxies_data['data']:
    if 'ip' in proxy and 'port' in proxy:
        proxy_str = f"{proxy['ip']}:{proxy['port']}"
        proxies.append(proxy_str)

# Check if we got proxies
if not proxies:
    print("No proxies found.")
else:
    print(f"Found {len(proxies)} proxies.")

# Randomly select a proxy from the list
selected_proxy = random.choice(proxies)

# Set up undetected ChromeDriver with the selected proxy
options = uc.ChromeOptions()
options.add_argument(f'--proxy-server={selected_proxy}')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--lang=en-US")
options.add_argument('--incognito')

# Initialize the driver with the selected proxy
driver = uc.Chrome(options=options)

# Example usage: Open a website
driver.get("https://www.google.com")
print("Website loaded using proxy:", selected_proxy)

# Close the driver after usage
driver.quit()
