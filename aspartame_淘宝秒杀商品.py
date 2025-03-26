from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

# 创建 Service 对象，指定 ChromeDriver 的路径
service = Service('/Users/chengjiahui/Downloads/chromedriver-mac-x64/chromedriver')
driver = webdriver.Chrome(service=service)

# 窗体最大化
driver.maximize_window()


def login(url):
    """登录模块,用于登录淘宝，并选中需要购买的商品按钮，结束"""
    # 获取网页源信息
    driver.get(url)
    # 等浏览器与Selenium完美契合之后再进行下一步动作
    driver.implicitly_wait(2)
    """账号密码登陆: 但是有验证框 需要拖拽"""
    # driver.find_element(By.NAME, "TPL_username").send_keys("187")  # user_pwd
    # driver.find_element(By.NAME, "TPL_password").send_keys("xld")  # user_pwd
    # time.sleep(4)
    # 有滑块验证，没加
    # driver.find_element(By.ID, "J_SubmitStatic").click()  # 寻找id类型的确认
    """扫码登陆(自己扫码)："""
    time.sleep(1)
    try:
        driver.find_element(By.ID, "J_Static2Quick").click()
    except:
        print("切换扫码登录失败，请手动操作")
    try:
        # 显式等待扫码登录成功，假设登录成功后页面会出现用户名元素，你可以根据实际情况修改
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.site-nav-login-info-nick'))
        )
    except:
        print("扫码登录超时，请检查登录情况")
        return

def buy_good(buy_time):
    """毫秒级抢购实现"""
    # 将目标时间转换为datetime对象
    target_time = datetime.datetime.strptime(buy_time, '%Y-%m-%d %H:%M:%S')
    submit_button = None
    while True:
        current_time = datetime.datetime.now()

        # 计算时间差
        delta = (target_time - current_time).total_seconds()

        if 19 < delta <= 20:
            try:
                submit_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//div[text()="提交订单"]'))
                )
                print("已在预设时间前20秒定位到提交订单按钮")
            except:
                print("在预设时间前20秒未能定位到提交订单按钮")

        # 当时间差小于1秒时进入高频检查
        if delta <= 1:
            # 高频检查循环
            while True:
                current_time = datetime.datetime.now()
                if current_time >= target_time:
                    try:
                        # 毫秒级时间记录
                        success_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        print(f"抢购成功！时间：{success_time}")

                        # 使用提前定位的按钮
                        if submit_button is None:
                            submit_button = WebDriverWait(driver, 0.5, 0.01).until(
                                EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn--QDjHtErD'))
                            )
                        submit_button.click()
                        return
                    except:
                        print("提交失败，重试...")
                        break
                time.sleep(0.000001)  # 1毫秒间隔
        else:
            # 低频检查
            print(f"等待中... 剩余时间：{delta:.2f}秒")
            time.sleep(0.1)  # 100毫秒间隔


if __name__ == "__main__":
    url = 'https://login.taobao.com/member/login.jhtml'
    login(url=url)
    """（修改）定时购买，可以在每个框中输入支付宝密码"""
    buy_good('2025-03-26 16:09:00')
    success_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(f"提交订单成功，时间为: {success_time}")

