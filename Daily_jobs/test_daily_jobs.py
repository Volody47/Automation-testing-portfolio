from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import Select
import math
from random import randint
import time

try:
    link = "https://test:stagingtest456@staging.daily.jobs/"
    browser = webdriver.Chrome()
    browser.get(link)

    #TODO may need sleep
    #time.sleep(2)

    # Confirm Alerts
    #prompt = browser.switch_to.alert
    #prompt.send_keys("My answer")
    #prompt.accept()




    # Log in Form
    button = browser.find_element_by_css_selector("button.signin")
    button.click()
    recruiter_part = browser.find_element_by_xpath("//span[contains(text(), 'Recruiter')]")
    recruiter_part.click()
    email_input = browser.find_element_by_name("email").send_keys("volody.sharapov@daily.jobs")
    password_input = browser.find_element_by_name("password").send_keys("We1c0me02")

    # Push log in button
    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()
    time.sleep(2)

    #Create 10 000 jobs with variable
    list_of_job = browser.find_elements_by_css_selector("div.table__row")

    while len(list_of_job) <= 1000:
        # Create new job
        new_job_button = browser.find_element_by_css_selector("button.btn--newJob")
        new_job_button.click()
        quick_upload = browser.find_element_by_xpath("//span[contains(text(), 'Quick Upload')]")
        quick_upload.click()
        input1 = browser.find_element_by_name("headline").send_keys("QAtest")
        input2 = browser.find_element_by_name("company").send_keys("test")

        # TODO Create new job Location (required)
        input_select_sity = browser.find_element_by_name("city-state").send_keys("Chicago,IL")
        # TODO need wait until
        time.sleep(3)

        select = browser.find_element_by_xpath("//a[contains(text(), 'Chicago')]")
        # TODO may need sleep
        time.sleep(2)
        select.click()
        input_select_address = browser.find_element_by_name("address").send_keys("Test road")
        input_full_description = browser.find_element_by_css_selector("textarea[name='description']").send_keys("Test")

        # Push log in button
        button = browser.find_element_by_css_selector("button.btn--small")
        button.click()
        time.sleep(1)

        # Back button
        button = browser.find_element_by_css_selector("button.btn--back")
        button.click()
        time.sleep(1)



        # # TODO Publish
        # publish_button = browser.find_element_by_name("city-state")
        # publish_button = browser.find_element_by_name("city-state")
        #
        # # TODO need wait until
        # time.sleep(2)
        #
        # select = browser.find_element_by_xpath("//a[contains(text(), 'Visible for search on job board')]")
        # # TODO may need sleep
        # # time.sleep(1)
        # select.click()

        if len(list_of_job) == 1000:
            break



finally:
    # Wait
    time.sleep(5)
    # Close browser
    browser.quit()

# Don't forget leave last field