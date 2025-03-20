from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

chrome_options = Options()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')  # Giảm bị detect bot
chrome_options.add_argument('--start-maximized')  # Mở to trình duyệt
# chrome_options.add_argument('--headless')  # Nếu muốn ẩn browser, bỏ dòng này nếu muốn xem chạy

service = Service('../chromedriver.exe')  # hoặc đường dẫn tuyệt đối tới file chromedriver.exe

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://itviec.com/sign_in')
time.sleep(2)

driver.find_element(By.ID, 'user_email').send_keys('22e1010008@hueuni.edu.vn')
driver.find_element(By.ID, 'user_password').send_keys('Duyvclra123!@#')
driver.find_element(By.CSS_SELECTOR, 'button.ibtn.ibtn-md.ibtn-primary.w-100[type="submit"]').click()

time.sleep(20)
job_data = []
for i in range(1, 51):
    driver.get(f'https://itviec.com/it-jobs?job_selected=&page={i}')
    time.sleep(5)

    jobs = driver.find_elements(By.CSS_SELECTOR, 'div.job-card')

    for job in jobs:
        data_job = {}
        try:
            data_job['title'] = job.find_element(By.CSS_SELECTOR, 'h3.imt-3').text.strip()
        except:
            data_job['title'] = 'N/A'
        try:
            data_job['company'] = job.find_element(By.CSS_SELECTOR, 'div.imy-3.d-flex.align-items-center > span > a').text.strip()
        except:
            data_job['company'] = 'N/A'
        try:
            data_job['salary'] = job.find_element(By.CSS_SELECTOR, 'div.ipb-3.fw-500 > div  span').text.strip()
        except:
            data_job['salary'] = 'N/A'
        try:
            info = job.find_elements(By.CSS_SELECTOR, 'div.d-flex.align-items-center.text-dark-grey.imt-1')
            data_job['work'] = info[0].find_element(By.CSS_SELECTOR, 'span').text.strip()
            data_job['place'] = info[1].find_element(By.CSS_SELECTOR, 'span').text.strip()
        except:
            data_job['work'] = 'N/A'
            data_job['place'] = 'N/A'
        try:
            skills = job.find_elements(By.CSS_SELECTOR, 'a.text-reset')
            skillls = ''
            for skill in range(len(skills)):
                skillls += skills[skill].find_element(By.CSS_SELECTOR, 'div').text.strip() + ', '
            data_job['skills'] = skillls
        except:
            data_job['skills'] = 'N/A'
        try:
            decriptions = job.find_elements(By.CSS_SELECTOR, 'li.imb-1')
            decription = ''
            for i in range(len(decriptions)):
                decription += decriptions[i].text.strip() + ', '
            data_job['decriptions'] = decription
        except:
            data_job['decriptions'] = 'N/A'
        job_data.append(data_job)

driver.quit()
df = pd.DataFrame(job_data)
df.to_csv('D:/Subject/Year 3/Do_an_2/jobs_data.csv', index=False, encoding='utf-8-sig')