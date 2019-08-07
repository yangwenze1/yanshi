import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ddt import ddt,data,unpack

@ddt
class PythonOrgSearch(unittest.TestCase):

    @classmethod
    def setUp(self):
       self.driver = webdriver.Firefox()


    @data(("8123456789111", "123456789abc", "search"),
          ("812345678", "123456789abc", "search"),
          ("812345678", "123456abc", "search")
          )
    @unpack
    def test_search_in_python_org(self,account,password,asserttext):
        driver = self.driver
        driver.get("https://bjw.halodigit.com:9060/nereus/merchant/index#/login")
        # 定位在指定的URL网页
        print(driver.title)
        assert "QRindo Merchant" in driver.title  # 断言  用来判断标题中有“”字段
        print(driver.page_source)

        elem = driver.find_element_by_name("login.loginName")  # 使用find_element_by_ *方法查找页面元素
        elem.clear()  # 发送密匙这类似于使用键盘输入，账号密码
        elem.send_keys(account)

        elem = driver.find_element_by_name("loginPwd")
        elem.clear()
        elem.send_keys(password)

        elem.send_keys(Keys.RETURN)

        assert asserttext not in driver.page_source
        #driver.close()



    #
    # def setUp(self):
    #   self.driver = webdriver.Firefox()
    # def test_search_in_python_org(self):
    #     driver = webdriver.Firefox()  # 创建Firefox WebDriver的实例
    #     driver.get("https://bjw.halodigit.com:9060/nereus/merchant/index#/login")
    #     # 定位在指定的URL网页
    #     print(driver.title)
    #     assert "QRindo Merchant" in driver.title  # 断言  用来判断标题中有“”字段
    #     print(driver.page_source)
    #
    #     elem = driver.find_element_by_name("login.loginName")  # 使用find_element_by_ *方法查找页面元素
    #     elem.clear()  # 发送密匙这类似于使用键盘输入，账号密码
    #     elem.send_keys("123456789")
    #
    #     elem = driver.find_element_by_name("loginPwd")
    #     elem.clear()
    #     elem.send_keys("123456abc")
    #
    #     elem.send_keys(Keys.RETURN)
    #
    #     assert "search" not in driver.page_source
    #     driver.close()
    #
    # def test_search_in_python_org(self):
    #     driver = webdriver.Firefox()  # 创建Firefox WebDriver的实例
    #     driver.get("https://bjw.halodigit.com:9060/nereus/merchant/index#/login")
    #     # 定位在指定的URL网页
    #     print(driver.title)
    #     assert "QRindo Merchant" in driver.title  # 断言  用来判断标题中有“”字段
    #     print(driver.page_source)
    #
    #     elem = driver.find_element_by_name("login.loginName")  # 使用find_element_by_ *方法查找页面元素
    #     elem.clear()  # 发送密匙这类似于使用键盘输入，账号密码
    #     elem.send_keys("8123456789111")
    #
    #     elem = driver.find_element_by_name("loginPwd")
    #     elem.clear()
    #     elem.send_keys("123456ccc")
    #
    #     elem.send_keys(Keys.RETURN)
    #
    #     assert "search" not in driver.page_source
    #     #driver.close()
    #
    # def test_search_in_python_org(self):
    #     driver = webdriver.Firefox()  # 创建Firefox WebDriver的实例
    #     driver.get("https://bjw.halodigit.com:9060/nereus/merchant/index#/login")
    #     # 定位在指定的URL网页
    #     print(driver.title)
    #     assert "QRindo Merchant" in driver.title  # 断言  用来判断标题中有“”字段
    #     print(driver.page_source)
    #
    #     elem = driver.find_element_by_name("login.loginName")  # 使用find_element_by_ *方法查找页面元素
    #     elem.clear()  # 发送密匙这类似于使用键盘输入，账号密码
    #     elem.send_keys("8123456789111")
    #
    #     elem = driver.find_element_by_name("loginPwd")
    #     elem.clear()
    #     elem.send_keys("123456abc")
    #
    #     elem.send_keys(Keys.RETURN)
    #
    #     assert "search" not in driver.page_source
    #     #driver.close()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()