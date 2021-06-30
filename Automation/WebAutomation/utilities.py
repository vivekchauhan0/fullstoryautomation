import os
import shutil
import zipfile

def createFolder(foldername):
    try:
        if not os.path.exists(foldername):
            os.makedirs(foldername)
            print('Created:', foldername)
    except OSError:
        print ("Creation of the directory %s failed" % foldername)
    else:
        print ("Successfully created the directory %s " % foldername)

def createZIP(foldername,filename):
    try:
        shutil.make_archive(foldername, 'zip', foldername)
        return os.path.join(foldername, filename)
    except OSError:
        print ("Creation of the zip %s failed" % filename)
    else:
        print ("Successfully created the directory %s " % filename)
