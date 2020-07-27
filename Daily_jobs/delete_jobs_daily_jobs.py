import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


try:
    link = "https://test:stagingtest456@staging.daily.jobs/"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.set_window_size(1280, 768)


    #TODO may need sleep
    #time.sleep(2)

    # Confirm Alerts
    #prompt = browser.switch_to.alert
    #prompt.send_keys("My answer")
    #prompt.accept()


    # Log in Form
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.signin")))
    button.click()
    time.sleep(1)
    recruiter_part = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Recruiter')]")))
    recruiter_part.click()
    time.sleep(1)
    email_input = browser.find_element_by_name("email").send_keys("qa@daily.jobs")
    password_input = browser.find_element_by_name("password").send_keys("Test1357")

    # Push log in button
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    button.click()
    time.sleep(2)

    # Remove New job (not published)
    list_of_jobs = WebDriverWait(browser, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.table__row")))
    #time.sleep(1)
    for i in list_of_jobs[1:]:
        not_published = i.text
        x = not_published.find('Not', 90)
        if x != -1:
            # 'Senior Sofware QA Engineer in automation 8131\nWonderful Automation Company 8131\n0 Applicants\nNot Published\nRemote\nPreview\nEdit\nRemove'
            remove_button = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//div/section/div/div[2]/div[1]/div/div[6]/div[3]")))
           # // span[contains(text(), 'Remove')] //div/section/div/div[2]/div[1]/div/div[6]/div[3]  // span[contains(text(), 'Remove')]
            remove_button.click()
            #time.sleep(0.5)

            # Confirm Alerts

            WebDriverWait(browser, 5).until(
                EC.alert_is_present())
            alert = browser.switch_to.alert
            alert.accept()



        # elif x == -1:
        #     switch_to_next = browser.find_elements_by_css_selector("div.pagination a")
        #     #try to find element right after .active
        #
        #
        #
        #
        #     # Confirm Alerts
        #     alert = browser.switch_to.alert
        #     alert.accept()

        else:
            print("All done")


finally:
    # Wait
    time.sleep(3)
    # Close browser
    browser.quit()

# Don't forget leave last field