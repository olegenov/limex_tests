from .base_model import BaseModel


class Email(BaseModel):
    def __init__(self, *args, **kwargs):
        super(Email, self).__init__(*args, **kwargs)
