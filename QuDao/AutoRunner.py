from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://sso.test.ustax.tech/")

# 登录表单在页面的框架中中，所以要切换到该框架
driver.switch_to_frame('login_frame')

# 通过使用选择器选择到表单元素进行模拟输入和点击按钮提交
driver.find_element_by_xpath('//*[@type="text"]').send_keys('19922026290')
driver.find_element_by_xpath('//*[@type="password"]').send_keys("resico2021")
driver.find_element_by_xpath('//*[@type="button"]').click()


# do something

# 退出窗口
driver.quit()