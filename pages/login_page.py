from pages.Base import Base
from utils.driver_utils import DriverUtils
class LoginPage(Base):

    username = ("account")  #name

    password = ("password")  #name

    login_btn = ("submit")   #class_name


    def input_username(self, username):
        self.by_name(self.username).send_keys(username)

    def input_password(self, password):
        self.by_name(self.password).send_keys(password)

    def click_submit(self):
        self.by_class_name(self.login_btn).click()



