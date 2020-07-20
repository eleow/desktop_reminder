
import os
import errno
from time import sleep
from datetime import datetime
import random
import configparser
import numpy as np
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

# goto https://chromedriver.chromium.org/downloads
# and download a chromedriver that corresponds to your chrome version, and place it in the same directory
chrome_driver = 'chromedriver'

def input_temperature(url, email, pw, temperature):
    """
        Function to enter temperature using Selenium
        This will be specific to your organisation's webpage, so customise accordingly

    """
    # Using Chrome to access web
    driver = webdriver.Chrome(chrome_driver)
    driver.get(url)

    # wait until page loads before sending keys
    max_delay = 10
    try:
        # email_box = driver.find_element_by_xpath("//input[@type='email']")
        email_box = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        email_box.send_keys(email)
        sleep(random.uniform(0.5,2.0))
        button = driver.find_element_by_xpath("//input[@type='submit']")
        button.click()

        # pw_box = driver.find_element_by_xpath("//input[@type='password']")
        pw_box =  WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
        pw_box.send_keys(pw)
        sleep(random.uniform(1.0,2.0))
        button = driver.find_element_by_xpath("//input[@type='submit']")
        button.click()

        # stay_signed_in = driver.find_element_by_xpath("//input[@type='button' and @value='No']")
        # stay_signed_in = driver.find_element_by_xpath("//input[@type='submit' and @value='Yes']")
        stay_signed_in = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, "//input[@type='button' and @value='No']")))
        stay_signed_in.click()

        # temp_box = driver.find_element_by_xpath("//input[@type='number']")
        temp_box = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, "//input[@type='number']")))
        temp_box.send_keys(5*Keys.BACKSPACE)
        temp_box.send_keys(5*Keys.DELETE)
        temp_box.send_keys(str(temperature))
        button = driver.find_element_by_xpath("//input[@type='submit']")
        # button.click()

        # final close button
        # button_close = WebDriverWait(driver, max_delay).until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit' and @value='Close']")))
        # button_close.click()


    except TimeoutException:
        print("Page took too long to load!")

    timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    # save value into a csv file
    import csv
    with open('temperature_history.csv', 'a+', newline='') as csvfile:
        tempwriter = csv.writer(csvfile, delimiter=',')
        tempwriter.writerow([timestamp, temperature])


def retrieve_iot_temperature():
    """
        Get your body temperature from your IOT-enabled wearable
    """

    # Use your IOT-enabled wearable API to get temperature
    #
    #

    # STUB
    # temperature - assume normal distribution with mean = 36.8, stdev = 0.4
    # mu, sigma = 36.8, 0.2
    # temperature = np.random.normal(mu, sigma, 1).round(1)
    temperature = f"{np.random.uniform(low=35.8, high=37.0):.1f}"
    return temperature


if __name__ == "__main__":
    configpath = './config.ini'
    config = configparser.ConfigParser()

    if not os.path.isfile(configpath):
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), configpath)

    else:
        config.read(configpath)

        # get params
        url = config['CREDENTIALS']['url']
        email = config['CREDENTIALS']['email']
        password = config['CREDENTIALS']['password']

        # temperature - assume normal distribution with mean = 36.8, stdev = 0.4
        # mu, sigma = 36.8, 0.2
        # temperature = np.random.normal(mu, sigma, 1).round(1)
        temperature = f"{np.random.uniform(low=35.8, high=37.0):.1f}"
        print(temperature)

        input_temperature(url, email, password, temperature)
