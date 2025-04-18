from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from datetime import date, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time

# Set up Chrome WebDriver (you can replace this with another browser driver like Firefox if needed)

print("code triggered at:")
print(datetime.datetime.now().time())

### headless options
options = Options()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# service = Service('/usr/bin/chromedriver')  # path to your installed chromedriver
# driver = webdriver.Chrome(service=service, options=options)

print("DRIVER INITIALIZED")

# Navigate to the login page of your app
driver.get('https://walmart.clubautomation.com/')
print("step 1")

print("opened website at:")
print(datetime.datetime.now().time())

target_time = datetime.time(12,0,0) # set to trigger at 7 AM CDT (12,0,0 UTC due to daylight savings)
while True:
    now = datetime.datetime.now().time()
    if now >= target_time:
        break
    time.sleep(1)
    
print("booking process started now:")    
print(datetime.datetime.now().time())

# username and password
u_name = 'sagrawal'
password = 'Myfitnesspass01@'

#date time
next_week = date.today() + timedelta(days=6) # make it default as 7
next_week = next_week.strftime("%m/%d/%Y")


# login
WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH,'//*[@id="login"]'))).send_keys(u_name)
WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH,'//*[@id="password"]'))).send_keys(password)
WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH,'//*[@id="loginButton"]'))).click()

#time.sleep(3)
print("LOGGED IN")

# # go to reservations
# WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH,'//*[@id="menu_reserve_a_court"]').click()

# # Select "Gym"
# WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH,'//*[@id="component_chosen"]').click()
# WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH,'//*[@id="component_chosen"]/div/ul/li[1]').click()

WebDriverWait(driver, 10).until(
EC.visibility_of_element_located((By.XPATH, '//*[@id="menu_reserve_a_court"]'))
).click()


# go to reservations
#WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH,'//*[@id="menu_reserve_a_court"]').click()
print("step 2")

# Select "Gym"
WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH,'//*[@id="component_chosen"]'))).click()
print("step 3")

#WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH,'//*[@id="component_chosen"]/div/ul/li[1]'))).click()
driver.find_element(By.XPATH,'//*[@id="component_chosen"]/div/ul/li[1]').click()
time.sleep(2)
print("step 4")

#WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH,'//*[@id="location_chosen"]'))).click()

driver.find_element(By.XPATH,'//*[@id="location_chosen"]').click()

print("step 5")

time.sleep(1)
WebDriverWait(driver, 20).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
)

#WebDriverWait(driver, 10).until( EC.element_to_be_clickable((By.XPATH,'//*[@id="location_chosen"]/div/ul/li[4]'))).click()
driver.find_element(By.XPATH,'//*[@id="location_chosen"]/div/ul/li[4]').click()
print("step 6")
#time.sleep(5)


#selecting date
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="date"]').clear()
print("step 7")
driver.find_element(By.XPATH,'//*[@id="date"]').send_keys(next_week)
print("step 8")

#90 mins
#WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH,'//*[@id="reserve-court-filter"]/div[3]/div[7]/div[3]/div/div/label[3]/span'))).click()
driver.find_element(By.XPATH,'//*[@id="reserve-court-filter"]/div[3]/div[7]/div[3]/div/div/label[3]/span' ).click()
#WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH,'//*[@id="reserve-court-filter"]/div[3]/div[7]/div[3]/div/div/label[1]/span').click() #for 30 mins, change to 2 for 6 mins
print("step 9")

#driver.save_screenshot("before_click1.png")
#search click
WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH,'//*[@id="reserve-court-search"]'))).click()
print("step 10")
#time.sleep(2)

# WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH,'//*[@id="timeFrom_chosen"]').click()

## select slot time
time.sleep(2)
#slot_times = driver.find_elements(By.XPATH,'//*[@id="times-to-reserve"]/tbody/tr/td/a')
#driver.save_screenshot("before_click1.png")
#slot_times = WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH,'//*[@id="times-to-reserve"]/tbody/tr/td/a')))
slot_times = driver.find_elements(By.XPATH,'//*[@id="times-to-reserve"]/tbody/tr/td/a')

print("step 11")
print(len(slot_times))

to_book = ['6:00pm', '6:30pm', '5:30pm', '7:00pm']

if len(slot_times)>0:

    # booking slot
    for e in slot_times:
        slot_time = e.get_attribute('text')
        slot_time = slot_time.strip()

        print(slot_time)

        if slot_time in to_book:
            e.click()
            
            # final reservation click
            #time.sleep(3)
            WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH,'//*[@id="confirm"]'))).click()
            print("step final")
            print("Badminton slot booked: ", slot_time)
            
            break

        # else:
        #     print("No relevant slots found")

else:
    print("No slots found")
    
####
driver.quit()
