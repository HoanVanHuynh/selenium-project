from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
# navigate to google page
# navigate to the application home page
driver.get("https://www.w3schools.com/")

title = driver.title

print("Title of google page is: ", title)

#login = driver.find_element_by_id("w3loginbtn")


# driver.find_element(By.XPATH, '//button[text()="Some text"]')
# driver.find_elements(By.XPATH, '//button')

login = driver.find_element(By.ID, 'w3loginbtn')

login.click()

#search = driver.find_element_by_class_name("q")

#print("result of search: ", search)

#page_source = driver.page_source

#print("page source of google page is: ", page_source)

#driver.quit()

