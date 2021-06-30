import unittest
from selenium import webdriver

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
import unittest, time, re
from bs4 import BeautifulSoup
import pickle
import random
import csv
import traceback
import Automation.WebAutomation.alog
import xml.parsers.expat as xmlerr
import shutil,os,zipfile,socket,time
import json
import sys
import csv
import xml.etree.cElementTree as ET
import pprint
import requests
from collections import defaultdict
import datetime
import math
from decimal import Decimal
import os
import platform
import zipfile
import mmap
import uuid
import os
import traceback
from threading import Thread
from time import sleep
import subprocess
from subprocess import call
from subprocess import Popen, PIPE
import threading
import glob
from threading import Lock
lock = Lock()
import multiprocessing
import time
import mmap
import pprint
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.opera.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import Automation.WebAutomation.charlesProxyService as c
from Automation.WebAutomation.utilities import createFolder
import Automation.WebAutomation.webconfig as wc
from Automation.WebAutomation.mainWebTestRunner import _data

from sys import platform

pp = pprint.PrettyPrinter(indent=4)

BASE_DIR = os.getcwd()
print("The current directory is")
print(BASE_DIR)

#os.path.join(BASE_DIR,
base_path = BASE_DIR

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("The current directory is")
print(BASE_DIR)

BETA_URL = wc.BETA_URL
QA_URL = wc.QA_URL
PROD_URL = wc.PROD_URL

WEBDRIVERDIRECTORY = os.path.join(BASE_DIR,'Drivers','webdrivers')

############################################################
global test_results_dir_json_wire
global test_results_dir_csv
global test_results_dir_excel
global test_results_dir_html
global test_results_dir_json_reports

#############################  #############################
print("Getting the values for the Directories")
test_results_dir_json_wire = _data['test_results_dir_json_wire']
print(test_results_dir_json_wire)
test_results_dir_csv = _data['test_results_dir_csv']
print(test_results_dir_csv)
test_results_dir_excel = _data['test_results_dir_excel']
print(test_results_dir_excel)
test_results_dir_html = _data['test_results_dir_html']
print(test_results_dir_html)
test_results_dir_json_reports = _data['test_results_dir_json_reports']
print(test_results_dir_json_reports)

###########################################################

if platform == "linux" or platform == "linux2":
    print("Linux")
    platform = 'Linux'
    WEBDRIVERDIRECTORY_CHROMEDRIVER = os.path.join(WEBDRIVERDIRECTORY,'chromedriver','chromedriver_linux64')
    WEBDRIVERDIRECTORY_FIREFOXDRIVER = os.path.join(WEBDRIVERDIRECTORY, 'firefoxdriver','geckodriver-linux64')

if platform == "darwin":
    print("Darwin")
    platform = 'Darwin'
    WEBDRIVERDIRECTORY_CHROMEDRIVER = os.path.join(WEBDRIVERDIRECTORY, 'chromedriver', 'chromedriver_mac64')
    WEBDRIVERDIRECTORY_FIREFOXDRIVER = os.path.join(WEBDRIVERDIRECTORY, 'firefoxdriver', 'geckodriver-macos')
    WEBDRIVERDIRECTORY_SAFARIDRIVER = os.path.join(WEBDRIVERDIRECTORY, '', '')


if platform == "win32":
    print("Win32")
    platform = 'Win32'
    WEBDRIVERDIRECTORY_CHROMEDRIVER = os.path.join(WEBDRIVERDIRECTORY, 'chromedriver', 'chromedriver_win32')
    WEBDRIVERDIRECTORY_FIREFOXDRIVER = os.path.join(WEBDRIVERDIRECTORY, 'firefoxdriver', 'geckodriver-win64')

if platform == "win64":
    print("Win64")
    platform = 'Win64'
    WEBDRIVERDIRECTORY_CHROMEDRIVER = os.path.join(WEBDRIVERDIRECTORY, 'chromedriver', 'chromedriver_win32')
    WEBDRIVERDIRECTORY_FIREFOXDRIVER = os.path.join(WEBDRIVERDIRECTORY, 'firefoxdriver', 'geckodriver-win64')



@pytest.fixture(params=["firefox"],scope="class")
#@pytest.fixture(params=["firefox"],scope="class")

#############################  #############################


def driver_init(request):
    if request.param == "chrome":
        # Local webdriver implementation
        print("Starting Chrome test")
        if _data['MITM'] == 'True':
            print("Since the MITM Proxy is TRUE we will Set the Proxy option")
            myProxy = wc.MITMHOST + ':' + wc.MITMPORT
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server=%s' % myProxy)
            chrome_options.add_argument('ignore-certificate-errors')
            if _data['HEADLESS'] == 'True':
                print("Setting the Headless option for Chrome")
                chrome_options.add_argument("--headless")
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
            print("Chromedriver Location")
            print(WEBDRIVERDIRECTORY_CHROMEDRIVER + '/chromedriver')
            web_driver = webdriver.Chrome(executable_path=WEBDRIVERDIRECTORY_CHROMEDRIVER + '/chromedriver',options=chrome_options)
        else:
            print("Since the MITM Proxy is FALSE we will NOT Set the Proxy option")
            print("Chromedriver Location")
            print(WEBDRIVERDIRECTORY_CHROMEDRIVER + '/chromedriver')
            chrome_options = webdriver.ChromeOptions()
            if _data['HEADLESS'] == 'True':
                print("Setting the Headless option for Chrome")
                chrome_options.add_argument("--headless")
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
            web_driver = webdriver.Chrome(executable_path=WEBDRIVERDIRECTORY_CHROMEDRIVER + '/chromedriver',options=chrome_options)

    if request.param == "firefox":
        print("Starting Firefox test")
        if _data['MITM'] == 'True':
            print("Since the MITM Proxy is TRUE we will Set the Proxy option")
            # Local webdriver implementation
            myProxy = wc.MITMHOST + ':' + wc.MITMPORT
            proxy = Proxy({
                'proxyType': ProxyType.MANUAL,
                'httpProxy': myProxy,
                'ftpProxy': myProxy,
                'sslProxy': myProxy,
                'noProxy': ''  # set this value as desired
            })

            fireFoxOptions = webdriver.FirefoxOptions()
            if _data['HEADLESS'] == 'True':
                print("Setting the Headless option for Firefox")
                fireFoxOptions.set_headless()
            fireFoxOptions.set_preference('network.http.phishy-userpass-length', 255)
            fireFoxOptions.set_preference("network.automatic-ntlm-auth.trusted-uris", BETA_URL)
            fireFoxOptions.set_preference("network.proxy.type", 1)
            fireFoxOptions.set_preference("network.proxy.http", wc.MITMHOST)
            fireFoxOptions.set_preference("network.proxy.http_port", wc.MITMPORT)
            ###############################
            # fireFoxOptions.set_preference('network.proxy.type', 1)
            # # Set the host/port.
            # fireFoxOptions.set_preference('network.proxy.http', proxy_host)
            fireFoxOptions.set_preference("browser.cache.disk.enable", False)
            fireFoxOptions.set_preference("browser.cache.memory.enable", False)
            fireFoxOptions.set_preference("browser.cache.offline.enable", False)
            fireFoxOptions.set_preference('network.proxy.https_port', wc.MITMPORT)
            fireFoxOptions.set_preference("network.proxy.ssl", wc.MITMHOST)
            fireFoxOptions.set_preference("network.proxy.ssl_port", int(wc.MITMPORT))
            print("Gecko Location")
            print(WEBDRIVERDIRECTORY_FIREFOXDRIVER + '/geckodriver')
            web_driver = webdriver.Firefox(executable_path=WEBDRIVERDIRECTORY_FIREFOXDRIVER + '/geckodriver', firefox_options=fireFoxOptions)
            web_driver.implicitly_wait(1)
            web_driver.delete_all_cookies()
        else:
            print("Since the MITM Proxy is FALSE we will NOT Set the Proxy option")
            print("Gecko Location")
            print(WEBDRIVERDIRECTORY_FIREFOXDRIVER + '/geckodriver')
            fireFoxOptions = webdriver.FirefoxOptions()
            if _data['HEADLESS'] == 'True':
                print("Setting the Headless option for Firefox")
                fireFoxOptions.set_headless()

            web_driver = webdriver.Firefox(executable_path=WEBDRIVERDIRECTORY_FIREFOXDRIVER + '/geckodriver', firefox_options=fireFoxOptions)
            web_driver.implicitly_wait(1)
            web_driver.delete_all_cookies()

    # if request.param == "safari":
    #     # Local webdriver implementation
    #     options = Options()

    request.cls.driver = web_driver
    yield
    web_driver.close()

@pytest.mark.usefixtures("driver_init")
class BasicTest:
    print("Initializing Basic Test")
    pass
class Test_URL(BasicTest):
        print("Initializing URL Open Test")

        def test_open_url(self):
            try:

                _t = None
                print("Running the Test Open Url")
                if _data['MITM'] == 'True':
                    print("Clearing Cache as flag is True")
                    c.clearCache()
                time.sleep(2)
                ######################### Using Proxy Service ##########################################
                self.driver.delete_all_cookies()
                self.driver.get(BETA_URL)
                print(self.driver.title)

                sleep(5)
                #########################################################
                print("Creating Local Test Folders for Test")
                simpleTest_Folder_dir_json_wire = os.path.join(test_results_dir_json_wire, "SimpleTest" + self.driver.name + "/test_open_url")
                print(simpleTest_Folder_dir_json_wire)
                createFolder(simpleTest_Folder_dir_json_wire)
                simpleTest_Folder_dir_csv = os.path.join(test_results_dir_csv, "SimpleTest" + self.driver.name + "/test_open_url")
                print(simpleTest_Folder_dir_csv)
                createFolder(simpleTest_Folder_dir_csv)
                simpleTest_Folder_dir_excel = os.path.join(test_results_dir_excel, "SimpleTest" + self.driver.name + "/test_open_url")
                print(simpleTest_Folder_dir_excel)
                createFolder(simpleTest_Folder_dir_excel)
                simpleTest_Folder_dir_html = os.path.join(test_results_dir_html, "SimpleTest" + self.driver.name + "/test_open_url")
                print(simpleTest_Folder_dir_html)
                createFolder(simpleTest_Folder_dir_html)

                ############## API ##############
                # if _data['MITM'] == 'True':
                #     print("Not Proxy data as flag is On")
                #     _t = c.getJSON("test_open_url", simpleTest_Folder_dir_json_wire)
                #     if _t == None:
                #         print("No Data")
                #     else:
                #         print("Got JSON Data")
                #         print("We will perform assertion now")

            except:
                print(traceback.format_exc())

        def test_injector(self):
            try:

                _t = None
                print("Running the Test Open Url")
                if _data['MITM'] == 'True':
                    print("Clearing Cache as flag is True")
                    c.clearCache()
                time.sleep(2)
                ######################### Using Proxy Service ##########################################
                self.driver.delete_all_cookies()
                print(self.driver.title)
                self.driver.get(BETA_URL)
                self.driver.set_window_size(550, 693)
                self.driver.find_element(By.CSS_SELECTOR, ".col-sm-12 .featured-fruit-name").click()
                self.driver.find_element(By.CSS_SELECTOR, "span:nth-child(1)").click()
                self.driver.find_element(By.LINK_TEXT, "Checkout").click()
                self.driver.find_element(By.ID, "billing-firstname").click()
                self.driver.find_element(By.ID, "billing-firstname").send_keys("vivek")
                self.driver.find_element(By.ID, "billing-lastname").send_keys("chauhan")
                self.driver.find_element(By.ID, "billing-address-1").send_keys("1234 street")
                self.driver.find_element(By.ID, "billing-city").send_keys("detroit")
                self.driver.find_element(By.ID, "billing-zip").click()
                self.driver.find_element(By.ID, "billing-zip").send_keys("48123")
                self.driver.find_element(By.ID, "shipping-same-billing").click()
                self.driver.find_element(By.ID, "credit_card_number").click()
                self.driver.find_element(By.ID, "credit_card_number").click()
                self.driver.find_element(By.ID, "credit_card_number").send_keys("12345678901234")
                self.driver.find_element(By.CSS_SELECTOR, ".form-inline > .form-control:nth-child(2)").click()
                dropdown = self.driver.find_element(By.CSS_SELECTOR, ".form-inline > .form-control:nth-child(2)")
                dropdown.find_element(By.XPATH, "//option[. = '4']").click()
                self.driver.find_element(By.CSS_SELECTOR,
                                         ".col-xs-6 > .form-control:nth-child(2) > .ng-binding:nth-child(4)").click()
                self.driver.find_element(By.CSS_SELECTOR, ".form-control:nth-child(3)").click()
                dropdown = self.driver.find_element(By.CSS_SELECTOR, ".form-control:nth-child(3)")
                dropdown.find_element(By.XPATH, "//option[. = '2023']").click()
                self.driver.find_element(By.CSS_SELECTOR,
                                         ".form-control:nth-child(3) > .ng-binding:nth-child(3)").click()
                self.driver.find_element(By.ID, "credit_card_cvv").click()
                self.driver.find_element(By.ID, "credit_card_cvv").send_keys("023")
                self.driver.find_element(By.CSS_SELECTOR, ".ng-scope > .checkbox-inline").click()
                self.driver.find_element(By.LINK_TEXT, "Purchase").click()
                sleep(2)
                #########################################################
                print("Creating Local Test Folders for Test")
                simpleTest_Folder_dir_json_wire = os.path.join(test_results_dir_json_wire, "SimpleTest" + self.driver.name + "/test_injector")
                print(simpleTest_Folder_dir_json_wire)
                createFolder(simpleTest_Folder_dir_json_wire)
                simpleTest_Folder_dir_csv = os.path.join(test_results_dir_csv, "SimpleTest" + self.driver.name + "/test_injector")
                print(simpleTest_Folder_dir_csv)
                createFolder(simpleTest_Folder_dir_csv)
                simpleTest_Folder_dir_excel = os.path.join(test_results_dir_excel, "SimpleTest" + self.driver.name + "/test_injector")
                print(simpleTest_Folder_dir_excel)
                createFolder(simpleTest_Folder_dir_excel)
                simpleTest_Folder_dir_html = os.path.join(test_results_dir_html, "SimpleTest" + self.driver.name + "/test_injector")
                print(simpleTest_Folder_dir_html)
                createFolder(simpleTest_Folder_dir_html)

                ############## API ##############
                if _data['MITM'] == 'True':
                    print("Get Proxy data as flag is On")
                    _t = c.getJSON("test_injector", simpleTest_Folder_dir_json_wire)
                    if _t == None:
                        print("No Data")
                    else:
                        for _i in _t:
                            print("Path")
                            print(_i['path'] )
                            print("Performance Data")
                            print(_i['times'])

                            # Verify Injector.js
                            if _i['path'] == '/injector.js':
                                print("Validating if injector.js is loaded")
                                assert _i['path'] == '/injector.js'




                        print("Got JSON Data")
                        print("We will perform assertion now")

            except:
                print(traceback.format_exc())

        def test_page_parameters(self):
            try:

                _t = None
                print("Running the Test Open Url")
                if _data['MITM'] == 'True':
                    print("Clearing Cache as flag is True")
                    c.clearCache()
                time.sleep(2)
                ######################### Using Proxy Service ##########################################

                print(self.driver.title)
                self.driver.get(BETA_URL)
                self.driver.set_window_size(550, 693)
                self.driver.find_element(By.CSS_SELECTOR, ".col-sm-12 .featured-fruit-name").click()
                self.driver.find_element(By.CSS_SELECTOR, "span:nth-child(1)").click()
                self.driver.find_element(By.LINK_TEXT, "Checkout").click()
                self.driver.find_element(By.ID, "billing-firstname").click()
                self.driver.find_element(By.ID, "billing-firstname").send_keys("vivek")
                self.driver.find_element(By.ID, "billing-lastname").send_keys("chauhan")
                self.driver.find_element(By.ID, "billing-address-1").send_keys("1234 street")
                self.driver.find_element(By.ID, "billing-city").send_keys("detroit")
                self.driver.find_element(By.ID, "billing-zip").click()
                self.driver.find_element(By.ID, "billing-zip").send_keys("48123")
                self.driver.find_element(By.ID, "shipping-same-billing").click()
                self.driver.find_element(By.ID, "credit_card_number").click()
                self.driver.find_element(By.ID, "credit_card_number").click()
                self.driver.find_element(By.ID, "credit_card_number").send_keys("12345678901234")
                self.driver.find_element(By.CSS_SELECTOR, ".form-inline > .form-control:nth-child(2)").click()
                dropdown = self.driver.find_element(By.CSS_SELECTOR, ".form-inline > .form-control:nth-child(2)")
                dropdown.find_element(By.XPATH, "//option[. = '4']").click()
                self.driver.find_element(By.CSS_SELECTOR,
                                         ".col-xs-6 > .form-control:nth-child(2) > .ng-binding:nth-child(4)").click()
                self.driver.find_element(By.CSS_SELECTOR, ".form-control:nth-child(3)").click()
                dropdown = self.driver.find_element(By.CSS_SELECTOR, ".form-control:nth-child(3)")
                dropdown.find_element(By.XPATH, "//option[. = '2023']").click()
                self.driver.find_element(By.CSS_SELECTOR,
                                         ".form-control:nth-child(3) > .ng-binding:nth-child(3)").click()
                self.driver.find_element(By.ID, "credit_card_cvv").click()
                self.driver.find_element(By.ID, "credit_card_cvv").send_keys("023")
                self.driver.find_element(By.CSS_SELECTOR, ".ng-scope > .checkbox-inline").click()
                self.driver.find_element(By.LINK_TEXT, "Purchase").click()
                sleep(2)
                #########################################################
                print("Creating Local Test Folders for Test")
                simpleTest_Folder_dir_json_wire = os.path.join(test_results_dir_json_wire, "SimpleTest" + self.driver.name + "/test_page_parameters")
                print(simpleTest_Folder_dir_json_wire)
                createFolder(simpleTest_Folder_dir_json_wire)
                simpleTest_Folder_dir_csv = os.path.join(test_results_dir_csv, "SimpleTest" + self.driver.name + "/test_page_parameters")
                print(simpleTest_Folder_dir_csv)
                createFolder(simpleTest_Folder_dir_csv)
                simpleTest_Folder_dir_excel = os.path.join(test_results_dir_excel, "SimpleTest" + self.driver.name + "/test_page_parameters")
                print(simpleTest_Folder_dir_excel)
                createFolder(simpleTest_Folder_dir_excel)
                simpleTest_Folder_dir_html = os.path.join(test_results_dir_html, "SimpleTest" + self.driver.name + "/test_page_parameters")
                print(simpleTest_Folder_dir_html)
                createFolder(simpleTest_Folder_dir_html)

                ############## API ##############
                if _data['MITM'] == 'True':
                    print("Get Proxy data as flag is On")
                    _t = c.getJSON("test_page_parameters", simpleTest_Folder_dir_json_wire)
                    if _t == None:
                        print("No Data")
                    else:
                        for _i in _t:
                            print("Path")
                            print(_i['path'])
                            print("Performance Data")
                            print(_i['times'])



                            # verify if the KEY VALUE is in page
                            if _i['path'] == '/rec/page':
                                print("Validating if /rec/page KVP exists?")
                                _pagedata = json.loads(_i['response']['body']['text'])

                                # Do KVP Mapping Here
                        print("Got JSON Data")
                        print("We will perform assertion now")

            except:
                print(traceback.format_exc())

        def test_fs_recording(self):
            try:

                _t = None
                print("Running the Test Open Url")
                if _data['MITM'] == 'True':
                    print("Clearing Cache as flag is True")
                    c.clearCache()
                time.sleep(2)
                ######################### Using Proxy Service ##########################################

                print(self.driver.title)
                self.driver.get(BETA_URL)
                #self.driver.set_window_size(550, 693)
                self.driver.find_element(By.CSS_SELECTOR, ".col-sm-12 .featured-fruit-name").click()
                self.driver.find_element(By.CSS_SELECTOR, "span:nth-child(1)").click()
                self.driver.find_element(By.LINK_TEXT, "Checkout").click()
                self.driver.find_element(By.ID, "billing-firstname").click()
                self.driver.find_element(By.ID, "billing-firstname").send_keys("vivek")
                self.driver.find_element(By.ID, "billing-lastname").send_keys("chauhan")
                self.driver.find_element(By.ID, "billing-address-1").send_keys("1234 street")
                self.driver.find_element(By.ID, "billing-city").send_keys("detroit")
                self.driver.find_element(By.ID, "billing-zip").click()
                self.driver.find_element(By.ID, "billing-zip").send_keys("48123")
                self.driver.find_element(By.ID, "shipping-same-billing").click()
                self.driver.find_element(By.ID, "credit_card_number").click()
                self.driver.find_element(By.ID, "credit_card_number").click()
                self.driver.find_element(By.ID, "credit_card_number").send_keys("12345678901234")
                self.driver.find_element(By.CSS_SELECTOR, ".form-inline > .form-control:nth-child(2)").click()
                dropdown = self.driver.find_element(By.CSS_SELECTOR, ".form-inline > .form-control:nth-child(2)")
                dropdown.find_element(By.XPATH, "//option[. = '4']").click()
                self.driver.find_element(By.CSS_SELECTOR,
                                         ".col-xs-6 > .form-control:nth-child(2) > .ng-binding:nth-child(4)").click()
                self.driver.find_element(By.CSS_SELECTOR, ".form-control:nth-child(3)").click()
                dropdown = self.driver.find_element(By.CSS_SELECTOR, ".form-control:nth-child(3)")
                dropdown.find_element(By.XPATH, "//option[. = '2023']").click()
                self.driver.find_element(By.CSS_SELECTOR,
                                         ".form-control:nth-child(3) > .ng-binding:nth-child(3)").click()
                self.driver.find_element(By.ID, "credit_card_cvv").click()
                self.driver.find_element(By.ID, "credit_card_cvv").send_keys("023")
                self.driver.find_element(By.CSS_SELECTOR, ".ng-scope > .checkbox-inline").click()
                self.driver.find_element(By.LINK_TEXT, "Purchase").click()
                sleep(2)
                #########################################################
                print("Creating Local Test Folders for Test")
                simpleTest_Folder_dir_json_wire = os.path.join(test_results_dir_json_wire, "SimpleTest" + self.driver.name + "/test_fs_recording")
                print(simpleTest_Folder_dir_json_wire)
                createFolder(simpleTest_Folder_dir_json_wire)
                simpleTest_Folder_dir_csv = os.path.join(test_results_dir_csv, "SimpleTest" + self.driver.name + "/test_fs_recording")
                print(simpleTest_Folder_dir_csv)
                createFolder(simpleTest_Folder_dir_csv)
                simpleTest_Folder_dir_excel = os.path.join(test_results_dir_excel, "SimpleTest" + self.driver.name + "/test_fs_recording")
                print(simpleTest_Folder_dir_excel)
                createFolder(simpleTest_Folder_dir_excel)
                simpleTest_Folder_dir_html = os.path.join(test_results_dir_html, "SimpleTest" + self.driver.name + "/test_fs_recording")
                print(simpleTest_Folder_dir_html)
                createFolder(simpleTest_Folder_dir_html)

                ############## API ##############
                if _data['MITM'] == 'True':
                    print("Get Proxy data as flag is On")
                    _t = c.getJSON("test_page_parameters", simpleTest_Folder_dir_json_wire)
                    if _t == None:
                        print("No Data")
                    else:
                        for _i in _t:
                            print("Path")
                            print(_i['path'])
                            print("Performance Data")
                            print(_i['times'])

                            # Verify if the recording is initialized
                            if _i['path'] == '/s/fs.js':
                                print("Validating if /s/fs.js is present?")
                                assert _i['path'] == '/s/fs.js'


                        print("Got JSON Data")
                        print("We will perform assertion now")

            except:
                print(traceback.format_exc())



        def test_page_seq(self):
            try:

                _t = None
                print("Running the Test Open Url")
                if _data['MITM'] == 'True':
                    print("Clearing Cache as flag is True")
                    c.clearCache()
                time.sleep(2)
                ######################### Using Proxy Service ##########################################

                print(self.driver.title)
                self.driver.get(BETA_URL)
                self.driver.set_window_size(550, 693)
                self.driver.find_element(By.CSS_SELECTOR, ".col-sm-12 .featured-fruit-name").click()
                self.driver.find_element(By.CSS_SELECTOR, "span:nth-child(1)").click()
                self.driver.find_element(By.LINK_TEXT, "Checkout").click()
                self.driver.find_element(By.ID, "billing-firstname").click()
                self.driver.find_element(By.ID, "billing-firstname").send_keys("vivek")
                self.driver.find_element(By.ID, "billing-lastname").send_keys("chauhan")
                self.driver.find_element(By.ID, "billing-address-1").send_keys("1234 street")
                self.driver.find_element(By.ID, "billing-city").send_keys("detroit")
                self.driver.find_element(By.ID, "billing-zip").click()
                self.driver.find_element(By.ID, "billing-zip").send_keys("48123")
                self.driver.find_element(By.ID, "shipping-same-billing").click()
                self.driver.find_element(By.ID, "credit_card_number").click()
                self.driver.find_element(By.ID, "credit_card_number").click()
                self.driver.find_element(By.ID, "credit_card_number").send_keys("12345678901234")
                self.driver.find_element(By.CSS_SELECTOR, ".form-inline > .form-control:nth-child(2)").click()
                dropdown = self.driver.find_element(By.CSS_SELECTOR, ".form-inline > .form-control:nth-child(2)")
                dropdown.find_element(By.XPATH, "//option[. = '4']").click()
                self.driver.find_element(By.CSS_SELECTOR,
                                         ".col-xs-6 > .form-control:nth-child(2) > .ng-binding:nth-child(4)").click()
                self.driver.find_element(By.CSS_SELECTOR, ".form-control:nth-child(3)").click()
                dropdown = self.driver.find_element(By.CSS_SELECTOR, ".form-control:nth-child(3)")
                dropdown.find_element(By.XPATH, "//option[. = '2023']").click()
                self.driver.find_element(By.CSS_SELECTOR,
                                         ".form-control:nth-child(3) > .ng-binding:nth-child(3)").click()
                self.driver.find_element(By.ID, "credit_card_cvv").click()
                self.driver.find_element(By.ID, "credit_card_cvv").send_keys("023")
                self.driver.find_element(By.CSS_SELECTOR, ".ng-scope > .checkbox-inline").click()
                self.driver.find_element(By.LINK_TEXT, "Purchase").click()
                sleep(2)
                #########################################################
                print("Creating Local Test Folders for Test")
                simpleTest_Folder_dir_json_wire = os.path.join(test_results_dir_json_wire,
                                                               "SimpleTest" + self.driver.name + "/test_fs_recording")
                print(simpleTest_Folder_dir_json_wire)
                createFolder(simpleTest_Folder_dir_json_wire)
                simpleTest_Folder_dir_csv = os.path.join(test_results_dir_csv,
                                                         "SimpleTest" + self.driver.name + "/test_fs_recording")
                print(simpleTest_Folder_dir_csv)
                createFolder(simpleTest_Folder_dir_csv)
                simpleTest_Folder_dir_excel = os.path.join(test_results_dir_excel,
                                                           "SimpleTest" + self.driver.name + "/test_fs_recording")
                print(simpleTest_Folder_dir_excel)
                createFolder(simpleTest_Folder_dir_excel)
                simpleTest_Folder_dir_html = os.path.join(test_results_dir_html,
                                                          "SimpleTest" + self.driver.name + "/test_fs_recording")
                print(simpleTest_Folder_dir_html)
                createFolder(simpleTest_Folder_dir_html)

                ############## API ##############
                if _data['MITM'] == 'True':
                    print("Get Proxy data as flag is On")
                    _t = c.getJSON("test_page_parameters", simpleTest_Folder_dir_json_wire)
                    if _t == None:
                        print("No Data")
                    else:
                        for _i in _t:
                            print("Path")
                            print(_i['path'])
                            print("Performance Data")
                            print(_i['times'])

                            # Verify Bundle is generated for every POST Sequence
                            if _i['path'] == '/rec/bundle':
                                print("Validating if Bundle ID is created for the sequence?")
                                print(json.loads(_i['request']['body']['text']))
                                # This is a perfect example where the bundle id is '' or empty and the code will fail. Need to check if the Recording was Sent
                                print(json.loads(_i['response']['body']['text']))
                                _seq = json.loads(_i['response']['body']['text']) # Handle Empty Bundle id
                                if ('BundleTime' in _seq):
                                    print("Bundle is Present in /rec/bundle")
                                    assert True

                        print("Got JSON Data")
                        print("We will perform assertion now")

            except:
                print(traceback.format_exc())