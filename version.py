#encoding:utf-8

import sys
sys.path.append("libs")

from Config import Config
from VersionHelper import VersionHelper

versionHelper = VersionHelper()

versionHelper.publicProject()
versionHelper.publishPhpFile()
versionHelper.publishResFile()
versionHelper.copyLogin()
# versionHelper.copyRelease()
# versionHelper.publishSDK()



