#encoding:utf-8

import sys
sys.path.append("libs")

import Config

Config.Config.PROJ_DIR = "dfh3"
Config.resetConfig()

from VersionHelper import VersionHelper

versionHelper = VersionHelper()

versionHelper.publicProject()
versionHelper.publicGameJs()
versionHelper.copyHtmlFile()
versionHelper.publishResFile()
versionHelper.copyLogin()