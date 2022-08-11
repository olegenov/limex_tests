from .base_model import BaseModel


class Main(BaseModel):
    def check_post_match(self, expected):
        got = self.page.post.text
        self.page.compare_texts(got, expected)
    
    def close_hint(self):
        self.page.hint.click()
