@classmethod
def setUp(self):
    # super().setUp()
    print('selenium version =', selenium.__version__)
    desired_caps ={}
    desired_caps['platformName'] ='Android'
    desired_caps['platformVersion'] = '4.4'
    desired_caps['deviceName'] = '192.168.1.54:5555'
    desired_caps['appPackage'] = '' # 再调查必要
    desired_caps['appActivity'] = '' # 再调查必要
    self.driver = webdriver.Remote()

@classmethod
def tearDown(self) :
    time.sleep(5)
    print('tearDown ------ ')
    self.driver.quit()