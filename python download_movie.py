from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains
import os

# Path to the uBlock Origin extension .crx file
ublock_extension_path = 'uBlock origin.crx'

# Setup Chrome options to include the uBlock Origin extension
chrome_options = Options()

chrome_options.add_extension(ublock_extension_path)
#chrome_options.add_argument("--headless")

# Initialize Chrome driver with options
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

# URL of the initial page
initial_url = 'https://tech.unblockedgames.world/?sid=bnpxOTF5Uk9VOVFZM2lEMkxXUmp0Y1dhWTZGUU8vUkluNmtDZ0FITDhrL0tBSDVUTEdWTmdBNnpPajczek1EQ2lkYXc1b0IzQTJnc1MrbUhRRjJ3cU1Nc0pEYXNuNmwwcmNzMDJRVHZhd1AwTDhrc0kvWXFMckU2VFp0RVF4d0lIYzEzUmlEbWFTQk5saXpzRTBpclg0eXdMMm5sMk92T1dqSVRNS0dEOThXSnk1ZnduekRheVc1cGMwZGZSbGVpTS9jTnBzaUpJcHY4NjFIcjJmYXdwZFp4NnB0T0Q2K0ZkczFGWEVKbTNUQ3RiRHRzcmo0VWpnTVZXcEx2TjVObg=='
params = {'behavior': 'allow', 'downloadPath': os.getcwd()}
driver.execute_cdp_cmd ('Page.setDownloadBehavior', params)

try:
    # Step 1: Open the initial page
    driver.get(initial_url)

    # Explicit wait setup
    wait = WebDriverWait(driver, 60)  # Increased wait time for robustness

    # Function to check and switch to an iframe if the element is inside one
    def find_element_with_iframes(by, value):
        iframes = driver.find_elements(By.TAG_NAME, 'iframe')
        for iframe in iframes:
            driver.switch_to.frame(iframe)
            try:
                element = wait.until(EC.element_to_be_clickable((by, value)))
                return element
            except:
                driver.switch_to.default_content()  # Switch back to main content if not found in the iframe
        return wait.until(EC.element_to_be_clickable((by, value)))  # If not found in iframes, find in main content


    time.sleep(40)
    start_verification = driver.find_element(By.XPATH, "//*[@id='landing']/span/a")
    start_verification.click()

    time.sleep(20)
    verify_button = driver.find_element(By.XPATH, "//*[@id='verify_button2']")
    verify_button.click()

    # Step 3: Click "Click Here to Continue"
    time.sleep(20)
    continue_button = find_element_with_iframes(By.XPATH, "//*[@id='verify_button']")
    continue_button.click()

    time.sleep(10)
    go_to_download = driver.find_element(By.XPATH,"//*[@id='two_steps_btn']")
    go_to_download.click()

    driver.switch_to.window(driver.window_handles[-1])

    time.sleep(10)
    instant_download = driver.find_element(By.XPATH,"//*[@id='cf_captcha']/div[2]/div[2]/a[1]")
    instant_download.click()

    driver.switch_to.window(driver.window_handles[-1])


    time.sleep(10)
    download_start = driver.find_element(By.XPATH,"//*[@id='ins']")
    download_start.click()


    time.sleep(40)



   
finally:
    print('Download process completed!')


