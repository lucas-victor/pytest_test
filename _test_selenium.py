from selenium import webdriver
from selenium.webdriver.common import keys

#driver = webdriver.Chrome() #executable_path="/home/lucasvictor/PycharmProjects/AluraCursoPython/venv/bin/chromedriver"
#
# driver.get("https://google.com.br")
#
# driver.find_element_by_name("q").send_keys("teste automatizado em python3")
#
# driver.find_element_by_name("q").send_keys(keys.Keys.RETURN)



#driver.find_element_by_name("btnK").click()

class Driver:

    driver = webdriver.Chrome() #executable_path="/home/lucasvictor/PycharmProjects/AluraCursoPython/venv/bin/chromedriver"

    def __init__(self):
        pass


    def get(self, url):
        self.driver.get(url)

    def click_by_id(self, _id):
        self.driver.find_element_by_id(_id).click()

    def click_by_name(self, name):
        self.driver.find_element_by_name(name).click()

    def escreve_by_id(self, _id, text):
        self.driver.find_element_by_id(_id).send_keys(text)

    def escreve_by_name(self, name, text):
        self.driver.find_element_by_name(name).send_keys(text)
        self.driver.find_element_by_name(name).send_keys(keys.Keys.RETURN)

    def close(self):
        self.driver.close()
    def wait(self, time):
        self.driver.implicitly_wait(time)

d = Driver()

d.get("https://google.com.br")
d.escreve_by_name("q", "teste automatizado em python3")
#d.click_by_name("btnK")
d.close()
