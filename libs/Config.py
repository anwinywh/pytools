#encoding:utf-8

import os
import sys
import ConfigParser

class Config:

    #发布版本
    VERSION = "new"

    #协议文件目录
    PROBUF_DIR = ""

    #csv路径
    CSV_DIR = ""

    #工程目录
    PROJECT_DIR = ""

    #svn目录
    SVN_DIR = ""

    #当前路径
    CUR_DIR = ""

    #工程项目
    PROJ_DIR = "dfh3"

    #md5文件
    MD5_FILE = "md5Files/version.txt"


def resetConfig():
    Config.CUR_DIR = os.path.split( os.path.realpath( sys.argv[0] ) )[0]

    config = ConfigParser.ConfigParser()
    config.readfp(open(Config.CUR_DIR + "/config.ini"))

    Config.PROBUF_DIR = config.get("config", "probuf_dir")
    Config.CSV_DIR = config.get("config", "csv_dir")

    Config.SVN_DIR = os.path.dirname(Config.CUR_DIR)
    Config.PROJECT_DIR = Config.SVN_DIR + "/" + Config.PROJ_DIR

resetConfig()



