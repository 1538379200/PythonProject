# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import yaml
import xlrd
import threading

path = r'D:\PythonProject\PythonProject\RedThreading\devices.xls'
file = xlrd.open_workbook(path)
sheet = file.sheet_by_index(0)
for i in range (3):
    row_list = sheet.row_values(i)
    if '' not in row_list:
        name = str(row_list[1])
        version = int(row_list[2])
        port = int(row_list[3])
        print(name,version,port)
    else:
        name = str(row_list[1])
        version = row_list[2]
        port = row_list[3]
        print(name,version,port)


    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = "%r"%version
    caps["devicesName"] = "%r"%name
    caps["appPackage"] = "com.qiyuanku.app"
    caps["appActivity"] = "com.uzmap.pkg.EntranceActivity"
    caps["autoAcceptAlerts"] = "true"
    caps["noReset"] = "false"
    caps["ensureWebviewsHavePages"] = True

    driver = webdriver.Remote("http://localhost:%r/wd/hub"%port, caps)
def do():
    el1 = driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_always_button")
    el1.click()
    time.sleep(2)
    TouchAction(driver).tap(x=515, y=1995).perform()
    time.sleep(2)
    # el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[3]/android.widget.Button")
    # el2.click()
    # time.sleep(2)
    el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[3]/android.widget.Button")
    el3.click()
    time.sleep(2)
    el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.EditText")
    el4.click()
    el4.send_keys("18174551626")    #此处为手机号
    el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.EditText")
    el5.click()
    el5.send_keys("654321")         #此处为用户密码
    el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View[5]/android.widget.Button")
    el6.click()
    time.sleep(2)
    TouchAction(driver).tap(x=737, y=1502).perform()

    #抢红包界面操作
    el7 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.ImageView")
    el7.click()
    el8 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[5]/android.view.View[1]/android.widget.Image")
    el8.click()
    el9 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.widget.EditText")
    el9.send_keys("123456")      #此处为红包口令
    el10 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[3]")
    el10.click()
    time.sleep(2)
    el11 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[4]/android.view.View/android.widget.Image[2]")
    el11.click()
    time.sleep(1)

if __name__ == '__main__':
    threading.Thread(target=do())
