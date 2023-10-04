from base.base_class import Base


class Auth_page(Base):

    def __index__(self, driver):
        super().__init__(driver)
        self.driver = driver