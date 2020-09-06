
def desired_time(driver, time_frame):
    """
    This function will select the desired time frame for posts to be scraped from
    :param driver: Driver from insights_login
    :param time_frame: 7, 28, or 90 days OR this month, this quarter, or custom
    :return: None, will select time frame
    """
    driver.implicitly_wait(2)
    calendar = driver.find_element_by_css_selector("#mediaManagerFilterAndSearch > div > span:nth-child(2) > span > "
                                                   "span > button")
    calendar.click()

    if time_frame == "7 days":
        driver.implicitly_wait(2)
        date_preset = driver.find_element_by_xpath('//*[@id="globalContainer"]/div[2]/div/div/div/div/div/div[1]/ul/'
                                                   'li[2]')
        date_preset.click()

    if time_frame == "28 days":
        driver.implicitly_wait(2)
        date_preset = driver.find_element_by_xpath('//*[@id="globalContainer"]/div[2]/div/div/div/div/div/div[1]/ul/'
                                                   'li[3]')
        date_preset.click()
    if time_frame == "90 days":
        driver.implicitly_wait(2)
        date_preset = driver.find_element_by_xpath('//*[@id="globalContainer"]/div[2]/div/div/div/div/div/div[1]/ul/'
                                                   'li[4]')
        date_preset.click()
    if time_frame == "This month":
        driver.implicitly_wait(2)
        date_preset = driver.find_element_by_xpath('//*[@id="globalContainer"]/div[2]/div/div/div/div/div/div[1]/ul/'
                                                   'li[5]')
        date_preset.click()
    if time_frame == "This quarter":
        driver.implicitly_wait(2)
        date_preset = driver.find_element_by_xpath('//*[@id="globalContainer"]/div[2]/div/div/div/div/div/div[1]/ul/'
                                                   'li[6]')
        date_preset.click()
