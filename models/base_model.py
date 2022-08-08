class BaseModel:
    def __init__(self, driver, page):
        self.driver = driver
        self.page = page
    
    def go_to(self, url):
        self.driver.get(url)
        self.page.should_be_right_page(url)
