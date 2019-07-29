from selenium import webdriver
from selenium import common
from selenium.webdriver.common.keys import Keys
import time

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page


class instaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        driver.get(
            'https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(3)
        email = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

    def like_post(self, hashtag):
        count = 0
        time.sleep(5)
        driver.get('https://www.instagram.com/explore/tags/'+hashtag+'/')
        time.sleep(5)
        for i in range(1, 3):
            driver.execute_script(
                'window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(5)
            posts = driver.find_elements_by_class_name('v1Nh3')
            links = [elem.find_element_by_css_selector(
                'a').get_attribute('href') for elem in posts]
            # we get links in the format of instagram.com/p/id

            for link in links:
                count = count+1
                if(count < 45):
                    driver.get(link)
                    try:

                        div = driver.find_elements_by_class_name('dCJp8')

                        lov = [el.find_element_by_class_name(
                            'glyphsSpriteHeart__outline__24__grey_9').click() for el in div]

                        time.sleep(10)
                    except Exception as ex:
                        time.sleep(60)
                else:
                    driver.close()


obj = instaBot('twtuvyj2019', 'pro@dota2')
obj.login()
obj.like_post('jessypinkman')
