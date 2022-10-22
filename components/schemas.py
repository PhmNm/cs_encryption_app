
class User:
    def __init__(self, info: dict):
        self.fullname=info['info']['fullname']
        self.email=info['info']['email']
        self.password=info['info']['password']
        self.phone=info['info']['phone']
        self.dob=info['info']['dob']
        self.storage=info['info']['storage']