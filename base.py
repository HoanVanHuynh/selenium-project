from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# navigate to google page
driver.get("https://google.com")

title = driver.title

print("Title of google page is: ", title)

#search = driver.find_element_by_class_name("q")

#print("result of search: ", search)

page_source = driver.page_source

print("page source of google page is: ", page_source)

driver.quit()

