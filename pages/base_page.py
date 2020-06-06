
class BasePage():
    #konstruktor classy
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    #otwieramy strone za pomocą get
    def open(self):
        self.driver.get(self.url)