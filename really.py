#encoding:utf-8

import sys
sys.path.append("libs")
import Config

Config.Config.VERSION = 'really'

######
######
#--------检查版本--------
# Config.Config.PROJ_DIR = 'dfh3'
Config.Config.PROJ_DIR = 'branches/dfh3_1_3_3'
#--------检查版本--------

Config.Config.MD5_FILE = "md5Files/really.txt"

Config.resetConfig()

from VersionHelper import VersionHelper

versionHelper = VersionHelper()

versionHelper.publicProject()
versionHelper.publishResFile()
versionHelper.copyRelease()
versionHelper.publishConfigJS()
versionHelper.publishSDK()

versionHelper.copyToComDir(False)  #只改代码
# versionHelper.copyToComDir(True) #所有



