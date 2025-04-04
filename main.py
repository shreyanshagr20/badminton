from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome WebDriver (you can replace this with another browser driver like Firefox if needed)

### headless options
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to the login page of your app
driver.get('https://walmart.clubautomation.com/')

# username and password
u_name = 'sagrawal'
password = 'Myfitnesspass01@'


# login
driver.find_element(By.XPATH,'//*[@id="login"]').send_keys(u_name)
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
driver.find_element(By.XPATH,'//*[@id="loginButton"]').click()

time.sleep(3)

# go to reservations
driver.find_element(By.XPATH,'//*[@id="menu_reserve_a_court"]').click()

# Select "Gym"
driver.find_element(By.XPATH,'//*[@id="component_chosen"]').click()
driver.find_element(By.XPATH,'//*[@id="component_chosen"]/div/ul/li[1]').click()


# go to reservations
driver.find_element(By.XPATH,'//*[@id="menu_reserve_a_court"]').click()

# Select "Gym"
driver.find_element(By.XPATH,'//*[@id="component_chosen"]').click()
driver.find_element(By.XPATH,'//*[@id="component_chosen"]/div/ul/li[1]').click()


time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="location_chosen"]').click()
driver.find_element(By.XPATH,'//*[@id="location_chosen"]/div/ul/li[4]').click()
time.sleep(5)


#selecting date
driver.find_element(By.XPATH,'//*[@id="date"]').clear()
driver.find_element(By.XPATH,'//*[@id="date"]').send_keys('04/11/2025')

#90 mins
driver.find_element(By.XPATH,'//*[@id="reserve-court-filter"]/div[3]/div[7]/div[3]/div/div/label[3]/span').click()

#search click
driver.find_element(By.XPATH,'//*[@id="reserve-court-search"]').click()

# driver.find_element(By.XPATH,'//*[@id="timeFrom_chosen"]').click()

## select slot time
slot_times = driver.find_elements(By.XPATH,'//*[@id="times-to-reserve"]/tbody/tr/td/a')

to_book = ['5:30pm', '6:00pm', '6:30pm']

for e in slot_times:
    slot_time = e.get_attribute('text')
    slot_time = slot_time.strip()

    print(slot_time)

    if slot_time in to_book:
        e.click()
        print("Badminton slot booked: ", slot_time)
        break
    
####

# final reservation click
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="confirm"]').click()

driver.quit()
