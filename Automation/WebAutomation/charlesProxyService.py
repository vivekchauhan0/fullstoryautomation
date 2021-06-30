import requests
import json
import urllib3
import os
import simplejson
import traceback
from urllib3 import ProxyManager, make_headers
from datetime import datetime
import Automation.WebAutomation.webconfig as wc

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_ROOT = os.path.join(BASE_DIR, 'MyApp')
CSV_DATA_ROOT = os.path.join(APP_ROOT, 'csv_data')
JSON_DATA_ROOT = os.path.join(APP_ROOT, 'json_data')
JSON_WIRE_ROOT = os.path.join(APP_ROOT, 'json_data_wire')
CSV_DATA_ROOT_TEMP = os.path.join(APP_ROOT, 'temp')
#Change this to the IP of the Machine which Charles Reports
charlesIP = 'http://' + wc.MITMHOST + ':' + wc.MITMPORT
urlHOST = wc.SNIFFHOST
urlPATH = wc.SNIFFPATH

def clearCache():
    try:
        print("Clearing Cache")

        http_proxy = charlesIP
        https_proxy = charlesIP
        ftp_proxy = "ftp://" + charlesIP

        proxyDict = {
            "http": http_proxy,
            "https": https_proxy,
            "ftp": ftp_proxy
        }
        # s = requests.Session()
        # s.proxies = proxyDict
        # r = s.get('http://control.charles/session/clear')
        # print(r)
        http = ProxyManager(charlesIP)

        # Now you can use `http` as you would a normal PoolManager
        r = http.request('GET', 'http://control.charles/session/clear')

    except:
        print(traceback.format_exc())
        print("Exception in Clearing Cache")

def getJSON(testname,path,urlpathtocheck=None):
    try:
        proxyCounter = 0
        dataValues = None
        returnValues = []
        http_proxy = charlesIP
        https_proxy = charlesIP
        ftp_proxy = "ftp://" + charlesIP

        proxyDict = {
            "http": http_proxy,
            "https": https_proxy,
            "ftp": ftp_proxy
        }

        r = requests.get('http://control.charles/session/export-json', proxies=proxyDict)
        print(r)

        # for item in json.loads(r.text):
        #     print(item['host'])
        #     print(item['path'] )
        #     if item['host'] == urlHOST:
        #     #if item['host'] == urlHOST and item['path'] == urlPATH :
        #         print("Getting the Data")
        #         dataValues = item
        #         returnValues.append(item)
        #         datatowrite = json.loads(r.text)
        #         # read_json(datatowrite)
        #         # f = open(os.path.join(path, testname + str(proxyCounter)  + '.json'), 'w')
        #         # f.write(json.dumps(datatowrite, indent=4, sort_keys=True))
        #         # f.close()
        #         print("Done saving the JSON file")
        #
        #     proxyCounter = proxyCounter + 1
        #
        # #return dataValues
        return json.loads(r.text)

    except:
        print("Exception in getting JSON")

def getCSV(testname,path):
    try:
        print("Getting CSV data for session")
        http_proxy = charlesIP
        https_proxy = charlesIP
        ftp_proxy = "ftp://" + charlesIP

        proxyDict = {
            "http": http_proxy,
            "https": https_proxy,
            "ftp": ftp_proxy
        }

        # r = requests.get('http://control.charles/session/export-csv', proxies=proxyDict)
        # print(r)

        http = ProxyManager(charlesIP)
        # Now you can use `http` as you would a normal PoolManager
        r = http.request('GET', 'http://control.charles/session/export-jso')
        datatowrite = r.read()
        # read_json(datatowrite)
        print(datatowrite)

        with open(os.path.join(path, testname), 'wb') as f:
            f.write(datatowrite)
        print("Done saving the file")

        with open(os.path.join(path, testname), 'wb') as f:
            f.write(datatowrite)
        print("Done saving the CSV file")

    except:
        print("Exception in getting CSV")

def prettyPrintJSON(file):
        # print charlesjson.text
        parsed = json.loads(file)
        print(json.dumps(parsed, indent=4, sort_keys=True))
        with open('charles.json', 'wb') as f:
            f.write(json.dumps(parsed, indent=4, sort_keys=True))
            print("Done Conversion")

def parse_json(file):
        f_path = file
        with open(f_path) as f:
            # j_data = json.load(f)      # ValueError: No JSON object could be decoded
            j_data = simplejson.load(f)  # right
            return j_data

def read_json(file):
        f_path = file
        with open(f_path) as f:
            # j_data = json.load(f)      # ValueError: No JSON object could be decoded
            j_data = simplejson.load(f)  # right

            return j_data

def file_finder():
        print("Checking if the file is present in Data Wire")
        os.chdir(JSON_WIRE_ROOT)
        # for file in glob.glob(""):
        #     print(file)

def checkJsonWire(file):

        print("Checking file presence")

        os.chdir(JSON_WIRE_ROOT)
        if os.path.exists(file) == True:
            return True
        else:
            return False
