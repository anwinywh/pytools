#encoding:utf-8

import re
import os
import os.path

class HotVersionFile:

    BaseDir = "/Users/yaowan/liyan/yaowan/dfh3/dfh3_hot/"

    Version = "170816222246"  #版本号
    Timing = ""       #定时器
    IsTiming = False  #是否定时器
    IsKeepVerify = False #是否保持审核版本号

    @staticmethod
    def parseAllFile(allFiles):
        HotVersionFile.IsTiming = HotVersionFile.Timing != ""

        for fileName in allFiles:
            path = HotVersionFile.BaseDir + fileName
            HotVersionFile.parseFile(path, path)

    @staticmethod
    def parseFile(srcFile, dstFile):
        print "解析文件:" + srcFile

        rf = open(srcFile, 'r')

        line = rf.readline()
        allText = ""

        while line:
            text = HotVersionFile.parse(line)
            allText += text
            line = rf.readline()

        rf.close()

        writeFile = open(dstFile, 'w')
        writeFile.write(allText)
        writeFile.close()

    @staticmethod
    def parse(text):

        if not HotVersionFile.IsTiming:  #定时器不改变默认的
            text = HotVersionFile.parseDefault(text)

        text = HotVersionFile.parseTiming(text)
        text = HotVersionFile.parseTimingVersion(text)
        text = HotVersionFile.parseVerifyVersion(text)

        return text

    @staticmethod
    def parseDefault(text):
        regStr = "(.*\"default\".*?=>.*?\")(.*?)(\"[\s\S]*)"
        matchObj = re.search(regStr, text)

        if matchObj:
            text = matchObj.group(1) + HotVersionFile.Version + matchObj.group(3)
            print "修改默认版本号:" + text
        return text

    @staticmethod
    def parseTiming(text):
        regStr = "(.*?define\(\"Timing\",.*?\")(.*?)(\"\)[\s\S]*)"
        matchObj = re.search(regStr, text)

        if matchObj:
            if HotVersionFile.IsTiming:
                text = matchObj.group(1) + HotVersionFile.Timing + matchObj.group(3)
                print "修改定时器时间:" + text
            else:
                text = matchObj.group(1) + matchObj.group(3)
        return text

    @staticmethod
    def parseTimingVersion(text):

        regStr = "(.*\"Timing\".*?=>.*?\")(.*?)(\"[\s\S]*)"
        matchObj = re.search(regStr, text)

        if matchObj:
            if HotVersionFile.IsTiming:
                text = matchObj.group(1) + HotVersionFile.Version + matchObj.group(3)
                print "修改定时器版本:" + text
            else:
                text = matchObj.group(1) + matchObj.group(3)

        return text

    @staticmethod
    def parseVerifyVersion(text):

        regStr = "(.*\"2017.*?\".*?=>.*?\")(.*?)(\"[\s\S]*)"
        matchObj = re.search(regStr, text)

        if matchObj:
            print "-----注意,有审核版本号---"
            if not HotVersionFile.IsKeepVerify:
                print "-----审核版本号已被删除----"
                text = ""
            else:
                print "-----审核版本号保留----"
        return text


