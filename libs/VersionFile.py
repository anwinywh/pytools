#encoding:utf-8

import os
import hashlib
import json

from Config import Config

class VersionFile:

    def __init__(self):
        self.m_pVersionConfig = {}

    #大文件的MD5值
    def getFileMd5(self, filename):
        if not os.path.isfile(filename):
            return
        myhash = hashlib.md5()
        f = file(filename,'rb')
        while True:
            b = f.read(8096)
            if not b :
                break
            myhash.update(b)
        f.close()
        return myhash.hexdigest()

    #读取配置文件
    def readVersionFile(self):

        md5FileDir = Config.CUR_DIR + "/md5Files"

        if not os.path.exists(md5FileDir):
            os.mkdir(md5FileDir)

        self.md5File = Config.CUR_DIR + "/" + Config.MD5_FILE

        print "md5File", self.md5File

        if not os.path.exists(self.md5File):
            return

        rf = open(self.md5File, 'r')
        jsonText = rf.read()
        rf.close()

        self.m_pVersionConfig = json.loads(jsonText)


    #获取文件版本号
    def getVersionFileNum(self, url, defaultNum, resourceDir):
        adsUrl = resourceDir + url

        fileMd5 = self.getFileMd5(adsUrl)

        if self.m_pVersionConfig.has_key(url):
            versionCfg = self.m_pVersionConfig[url]
            if versionCfg['md5'] == fileMd5:
                defaultNum = versionCfg['num']
            else:
                print "文件修改:", url

        self.m_pVersionConfig[url] = {'md5':fileMd5, "num":defaultNum}

        return defaultNum

    #保存配置文件
    def saveVersionFile(self):
        in_json = json.dumps(self.m_pVersionConfig)
        writeFile = open(self.md5File, 'w')
        writeFile.write(in_json)
        writeFile.close()


