import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


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
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.signin")))
    button.click()
    recruiter_part = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Recruiter')]")))
    recruiter_part.click()
    email_input = browser.find_element_by_name("email").send_keys("qa1@daily.jobs")
    password_input = browser.find_element_by_name("password").send_keys("Test1357")

    # Push log in button
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    button.click()



    #Create 10 000 jobs with variable
    list_of_job = browser.find_elements_by_css_selector("div.table__row")

    while True:
        # Create new job
        new_job_button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn--newJob")))
        new_job_button.click()

        quick_upload = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Quick Upload')]")))
        quick_upload.click()
        time.sleep(1)
        input1 = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "headline"))).send_keys("QAtest")
        #time.sleep(1)
        input2 = browser.find_element_by_name("company").send_keys("test")
        #time.sleep(1)

        # TODO Create new job Location (required)
        input_select_sity = browser.find_element_by_name("city-state").send_keys("Chicago,IL")
        # TODO need wait until
        #time.sleep(3)

        select = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.dropdown-item")))
        #"//a[contains(text(), 'Chicago')]"
        # TODO may need sleep
        #time.sleep(2)
        #select.click()
        select.click()
        input_select_address = browser.find_element_by_name("address").send_keys("Test road")
        #time.sleep(1)
        input_full_description = browser.find_element_by_css_selector("textarea[name='description']").send_keys("Selenium, Python, Postman")
        time.sleep(3)

        # Push log in button
        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn--small")))
        button.click()
        time.sleep(2)

        # Back button
        button_back = browser.find_element_by_css_selector("button.btn--back")
        button_back.click()


        #time.sleep(5)

        # TODO Publish
        publish_button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Job post is not visible to candidates']")))
        publish_button.click()

        # TODO need wait until
        #time.sleep(2)

        on_job_board = browser.find_element_by_xpath("//a[contains(text(), 'Visible for search on job board')]")
        # TODO may need sleep
        #time.sleep(1)
        on_job_board.click()

        if len(list_of_job) == 4:
            break



finally:
    # Wait
    time.sleep(3)
    # Close browser
    browser.quit()

# Don't forget leave last field