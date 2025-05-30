from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

chrome_options = Options()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--start-maximized')

service = Service('../chromedriver.exe')

driver = webdriver.Chrome(service=service, options=chrome_options)
job_data = []
for i in range(101, 201):
    driver.get(f"https://careerviet.vn/viec-lam/tat-ca-viec-lam-trang-{i}-vi.html")
    time.sleep(5)

    jobs = driver.find_elements(By.CSS_SELECTOR, 'div.job-item')
    for job in jobs:
        data_job = {}
        link = job.find_element(By.CSS_SELECTOR, 'div.title > h2 > a').get_attribute('href')
        main_tab = driver.current_window_handle  # Lưu tab chính

        # Mở tab mới
        driver.execute_script("window.open(arguments[0]);", link)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(5)

        #crawl
        try:
            data_job['title'] = driver.find_element(By.CSS_SELECTOR, 'div.job-desc > h1').text.strip()
        except:
            data_job['title'] = 'N/A'
        try:
            data_job['company'] = driver.find_element(By.CSS_SELECTOR, 'div.job-desc > a').text.strip()
        except:
            data_job['company'] = 'N/A'
        try:
            data_job['place'] = driver.find_element(By.CSS_SELECTOR, 'div.detail-box > div > p > a').text.strip()
        except:
            data_job['place'] = 'N/A'
        others = driver.find_elements(By.CSS_SELECTOR, 'div.detail-box.has-background > ul > li')
        try:
            data_job['publish day'] = others[0].find_element(By.CSS_SELECTOR, 'p').text.strip()
        except:
            data_job['publish day'] = 'N/A'
        try:
            fields = others[1].find_elements(By.CSS_SELECTOR, 'p > a')
            strings = ''
            for field in fields:
                strings += field.text.strip() +'. '
            data_job['field'] = strings
        except:
            data_job['field'] = 'N/A'
        try:
            data_job['employee status'] = others[2].find_element(By.CSS_SELECTOR, 'p').text.strip()
        except:
            data_job['employee status'] = 'N/A'
        try:
            data_job['salary'] = others[3].find_element(By.CSS_SELECTOR, 'p').text.strip()
        except:
            data_job['salary'] = 'N/A'
        try:
            data_job['experiment'] = others[4].find_element(By.CSS_SELECTOR, 'p').text.strip()
        except:
            data_job['experiment'] = 'N/A'
        try:
            data_job['level'] = others[5].find_element(By.CSS_SELECTOR, 'p').text.strip()
        except:
            data_job['level'] = 'N/A'
        try:
            data_job['due day'] = others[6].find_element(By.CSS_SELECTOR, 'p').text.strip()
        except:
            data_job['due day'] = 'N/A'
        try:
            welfares = driver.find_elements(By.CSS_SELECTOR, 'ul.welfare-list > li')
            welfare = ''
            for i in welfares:
                welfare += i.text.strip() +'. '
            data_job['welfares'] = welfare
        except:
            data_job['welfares'] = 'N/A'



        job_data.append(data_job)
        # Đóng tab chi tiết
        driver.close()
        # Quay về tab chính
        driver.switch_to.window(main_tab)
driver.quit()
df = pd.DataFrame(job_data)
df.to_csv('D:/Subject/Year 3/Do_an_2/jobs_data_careerviet.csv', index=False, encoding='utf-8-sig', header=False, mode='a')