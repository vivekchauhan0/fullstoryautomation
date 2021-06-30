import logging,os,datetime,traceback
import Automation.WebAutomation.sys_config as attset

class alog(object):
    """this class is used to log logs."""


    def __init__(self,logname):
        self.logger=logging.getLogger(logname)

        try:
            test = attset.ATTsettings()
            test.readAllSettings()
            log_dir_path = test.logpath
            if not os.path.exists(log_dir_path):
                os.makedirs(log_dir_path)
            log_path=log_dir_path+'/'+str(datetime.date.today())+'.txt'
            if not os.path.exists(log_path):
                f=open(log_path,'w+')
                f.write('Logging')
                f.close()
            hdlr = logging.FileHandler(log_path)

            formatter = logging.Formatter('%(asctime)s %(levelname)s \r\n %(message)s')
            hdlr.setFormatter(formatter)
            self.logger.addHandler(hdlr)
            self.logger.setLevel(logging.DEBUG)
        except:
            self.logger.error ( 'Error when read config file')
            print(traceback.format_exc())

    def debug(self,msg,arg):
        self.logger.debug('%s \r %s' % (arg,msg))
    def info(self,msg,arg):
        self.logger.info('%s \r %s' % (arg,msg))
    def warning(self,msg,arg):
        self.logger.warning('%s \r %s' % (arg,msg))
    def error(self,msg,arg):
        self.logger.error('%s \r %s' % (arg,msg))
