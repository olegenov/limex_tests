import datetime as dt

from selenium.webdriver.common.action_chains import ActionChains

from .base_model import BaseModel


class Main(BaseModel):
    def check_post_match(self, expected):
        got = self.page.post.text
        self.page.compare_texts(got, expected)
    
    def close_hint(self):
        self.page.hint.click()

    def publish_post(self):
        now = dt.datetime.now()
        text = now.strftime('%Y-%m-%d %H:%M:%S Comment notification test post')

        self.page.add_post.click()
        self.page.post_textarea.send_keys(text)

        self.driver.execute_script("arguments[0].scrollIntoView()", self.page.post_textarea)
        self.page.publish_button.click()
