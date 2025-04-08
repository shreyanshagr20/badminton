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
print("DRIVER INITIALIZED")

# Navigate to the login page of your app
driver.get('https://walmart.clubautomation.com/')
print("step 1")

# username and password
u_name = 'sagrawal'
password = 'Myfitnesspass01@'


# login
driver.find_element(By.XPATH,'//*[@id="login"]').send_keys(u_name)
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
driver.find_element(By.XPATH,'//*[@id="loginButton"]').click()

time.sleep(3)
print("LOGGED IN")

# # go to reservations
# driver.find_element(By.XPATH,'//*[@id="menu_reserve_a_court"]').click()

# # Select "Gym"
# driver.find_element(By.XPATH,'//*[@id="component_chosen"]').click()
# driver.find_element(By.XPATH,'//*[@id="component_chosen"]/div/ul/li[1]').click()


# go to reservations
driver.find_element(By.XPATH,'//*[@id="menu_reserve_a_court"]').click()
print("step 2")

# Select "Gym"
driver.find_element(By.XPATH,'//*[@id="component_chosen"]').click()
print("step 3")
driver.find_element(By.XPATH,'//*[@id="component_chosen"]/div/ul/li[1]').click()
print("step 4")


time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="location_chosen"]').click()
print("step 5")
driver.find_element(By.XPATH,'//*[@id="location_chosen"]/div/ul/li[4]').click()
print("step 6")
time.sleep(5)


#selecting date
driver.find_element(By.XPATH,'//*[@id="date"]').clear()
print("step 7")
driver.find_element(By.XPATH,'//*[@id="date"]').send_keys('04/11/2025')
print("step 8")

#90 mins
driver.find_element(By.XPATH,'//*[@id="reserve-court-filter"]/div[3]/div[7]/div[3]/div/div/label[3]/span').click()
print("step 9")

#search click
driver.find_element(By.XPATH,'//*[@id="reserve-court-search"]').click()
print("step 10")

# driver.find_element(By.XPATH,'//*[@id="timeFrom_chosen"]').click()

## select slot time
slot_times = driver.find_elements(By.XPATH,'//*[@id="times-to-reserve"]/tbody/tr/td/a')
print("step 11")

to_book = ['5:30pm', '6:00pm', '6:30pm']

# booking slot
for e in slot_times:
    slot_time = e.get_attribute('text')
    slot_time = slot_time.strip()

    print(slot_time)

    if slot_time in to_book:
        e.click()
        
        # final reservation click
        time.sleep(3)
        driver.find_element(By.XPATH,'//*[@id="confirm"]').click()
        print("step final")
        print("Badminton slot booked: ", slot_time)
        
        break
    
####
driver.quit()
