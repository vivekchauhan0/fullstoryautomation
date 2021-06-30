import xml.dom.minidom as minidom
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Application_ROOT = os.path.join(BASE_DIR,'MyApp')
CONFIG_FILE = os.path.join(Application_ROOT,'config.xml')
class ATTsettings:
    def __int__(self):
        self.localtemp = ''
    def readAllSettings(self):
        configfile = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        xmldom = minidom.parse(CONFIG_FILE)
        root = xmldom.getElementsByTagName("Settings")
        for node_1 in root[0].childNodes:
            if node_1.nodeName == 'filepath':
                for node_2 in node_1.childNodes:
                    if node_2.nodeName == 'log':
                        self.logpath = node_2.getAttribute('path')
                        print(self.logpath)

if __name__ == '__main__':
    '''test code'''
    test = ATTsettings()
    test.readAllSettings()
    print(test.readAllSettings())