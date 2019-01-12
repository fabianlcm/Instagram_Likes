from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        # setting up constructor
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        # opening browser
        driver = self.driver
        # opening instagram webpage
        driver.get('https://www.instagram.com/')
        time.sleep(random.randint(2, 2))

        # finding login button
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        # clicking login button
        login_button.click()
        time.sleep(random.randint(2))

        # finding username box
        username_box = driver.find_element_by_xpath("//input[@name='username']")
        # clearing username box in case there is something written
        username_box.clear()
        # sending your username into the username box
        username_box.send_keys(self.username)
        # finding the password box
        password_box = driver.find_element_by_xpath("//input[@name='password']")
        # clearing password box in case there is something written
        password_box.clear()
        # sending your password into the password box
        password_box.send_keys(self.password)
        # pressing RETURN key to login
        password_box.send_keys(Keys.RETURN)
        time.sleep(random.randint(2))

    def like_photo(self, hashtag):
        driver = self.driver
        # accessing instagram hashtags page with your hashtag
        driver.get("https://www.instagram.com/explore/tags/{}/".format(hashtag))
        time.sleep(random.randint(2, 4))

        # using loop to scroll down to load more pictures
        for i in range(1, 7):
            driver.execute_script('Window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(random.randint(2, 4))

            # getting hypertext references
            hypertext_references = driver.find_element_by_tag_name('a')
            hypertext_references = [elem.get_attribute('href') for elem in hypertext_references]
            hypertext_references = [href for href in hypertext_references if hashtag in href]

            # looping through each pic hypertext reference
            for pic_href in hypertext_references:
                driver.get(pic_href)
                time.sleep(random.randint(2, 4))
                driver.execute_script('Window.scrollTo(0, document.body.scrollHeight);')
                
                # findinf element 'like' within each picture
                try:
                    time.sleep(random.randint(2, 4))
                    driver.find_element_by_link_text('like').click()
                    time.sleep(random.randint(18, 20))
                except Exception as e:
                    time.sleep(random.randint(2, 4))


# type your username
username = 'your_username'
# type your password
password = 'your_password'

instagram = InstagramBot(username, password)
instagram.login()
instagram.like_photo('newyork')

# type your hashtags
hashtags = ['travel', 'traveling', 'adventure', 'traveller', 'world',
            'network', 'studentlife', 'travellife', 'passport', 'passportlife', 'fun', 'happy',
            'airplane', 'funny', 'me', 'followme', 'follow', 'tbt', 'airbnb',
            'airbnbexperience', 'instagood', 'instagood', 'fashion', 'sun', 'pro']

while True:
    try:
        hashtag = random.choice(hashtags)
        instagram.like_photo(hashtag)
    except Exception:
        instagram.closeBrowser()
        time.sleep(60)
        instagram = InstagramBot(username, password)
        instagram.login()
