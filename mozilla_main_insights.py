import os
from selenium import webdriver
from MozillaInsights import mozilla_login, mozilla_details

# Initializing Variables...
driver = 0
username = str(input("Enter username to login: "))
password = str(input("Password of account: "))
two_fact_code = None
post_count = int(input("Number of posts: "))
mode = str(input("Enter what type of posts you want to get Insights on (either Photos or Videos): "))
account = str(input("Enter which account (if any) that you want to specify: "))
time_frame = str(input("Enter desired time frame to scrape posts from (7 days, 28 days, 90 days, This month, "
                       "or This quarter, or press 'space' for none): "))
if time_frame == ' ':
    time_frame = None
make_directory = str(input("Enter path where to create directory for files: "))
path_driver = str(input("Enter the path where your driver is located: "))


def main():
    global driver
    # Makes directory to hold image files
    os.mkdir(make_directory)
    print("Running...")
    # The below line of code will create an instance of Firefox using selenium
    driver = webdriver.Firefox(executable_path=path_driver)
    driver.delete_all_cookies()
    print("Logging In...")
    log = mozilla_login.Login(driver, username, password, two_fact_code)
    log.sign_in()
    print("Navigating...")
    mozilla_details.navigate(driver)
    # Getting Insights for Posts
    print("Getting Insights...")
    mozilla_details.posts(driver, post_count, mode, account, time_frame, make_directory)
    print("Done!")
    driver.quit()


if __name__ == '__main__':
    main()
