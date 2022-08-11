from .base_model import BaseModel


class Search(BaseModel):
    def click_post(self):
        post = self.page.results[0]
        post.click()