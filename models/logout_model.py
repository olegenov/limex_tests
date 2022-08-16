from .base_model import BaseModel


class Logout(BaseModel):
    def __init__(self, *args, **kwargs):
        super(Logout, self).__init__(*args, **kwargs)
