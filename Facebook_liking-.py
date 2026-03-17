from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import random

# USING OPEN AI FOR COMMENTING





class FbAcc:
    def __init__(self):
        self.seen_posts = set()
        self.unique_posts = []
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)



        # Forcing minimising SSL errors and reduce logs
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument('--log-level=3')



        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://www.facebook.com/')
        self.driver.implicitly_wait(10)
        time.sleep(2)



    def login(self):
        try:
            username = 'anything@gmail.com'
            password = 'anyhting'

            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'email')))
            
            #  Funciton call, defined in the below code  
            self._human_type(username_field, username)

            password_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'pass')))
            password_field.send_keys(password)

            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
            login_button.click()

            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.find_elements(By.XPATH, "//div[@role='feed']") or 
                               driver.find_elements(By.XPATH, "//span[contains(text(),'Welcome to Facebook')]"))

            self._handle_post_login()

        except Exception as e:
            print(f'Login failed: {str(e)}')
            self.driver.save_screenshot('login_error.png')




    def _human_type(self, element, text):
        for letter in text:
            element.send_keys(letter)
            time.sleep(random.uniform(0.1, 0.3))

    def click_homepage(self):
        try:
            home_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Home']")))
            home_button.click()
            return True
        except Exception as e:
            print(f'Homepage click error: {e}')
            return False

    def not_remember_pw(self):
        try:
            not_now_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Not Now')]")))
            not_now_btn.click()
            return True
        except Exception as e:
            print(f'Password remember error: {e}')
            return False



    def reading_posts(self):
        try:
            for _ in range(3):  # scrolls 3 times
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)

                posts = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located(
                        (By.XPATH, "//div[@dir='auto' and string-length(normalize-space()) > 20]")
                    )
                )

                for idx, post in enumerate(posts):
                    content = post.text.strip()
                    signature = hash(content)

                    if content and signature not in self.seen_posts:
                        self.seen_posts.add(signature)
                        self.unique_posts.append(content)

                        print(f"\n🧾 New Post {len(self.unique_posts)}:\n{content[:100]}...")

                        try:
                            # Like only one post
                            like_button = post.find_element(
                                By.XPATH,
                                ".//following::span[@data-ad-rendering-role='like_button'][1]"
                            )
                            like_button.click()
                            print("👍 Post liked successfully.\n")
                            time.sleep(1)
                            return self.unique_posts  # Exit after first like

                        except Exception as like_err:
                            print(f"❌ Failed to like post: {like_err}")
                            return self.unique_posts

            return self.unique_posts

        except Exception as e:
            print(f'Error reading posts: {str(e)}')
            return self.unique_posts






    def _handle_post_login(self):
        try:
            time.sleep(2)
            if self.not_now():
                time.sleep(2)
                self.not_now()
        except Exception as e:
            print(f'Post-login error: {e}')

    def not_now(self):
        try:
            not_now_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Not now')]")))
            not_now_button.click()
            return True
        except Exception as e:
            print(f'Failed to click "Not now": {str(e)}')
            return False

    def close(self):
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()


if __name__ == "__main__":
    bot = FbAcc()
    try:
        bot.login()
        bot.click_homepage()
        time.sleep(3)
        bot.not_remember_pw()
        time.sleep(3)

        posts = bot.reading_posts()
        if posts:
            for i, post in enumerate(posts[:5], 1):
                print(f"\nPost {i}:")
                print(post[:100] + "...")

        input("Press Enter to exit...")

    except Exception as e:
        print(f"Script failed: {str(e)}")
    # finally:
        # bot.close()
