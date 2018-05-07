from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

my_url = 'https://arion.aut.ac.nz/ArionMain/CourseInfo/Information/Qualifications/PaperSearch.aspx'
driver.get(my_url)

print(driver.page_source)