#encoding:utf-8

import commands
import json
import os
import re
import shutil

import sys
import time


from Config import Config
from VersionFile import VersionFile

PROJECT_DIR = Config.PROJECT_DIR
VERSION = Config.VERSION

class VersionHelper:

    def __init__(self):
        self.version_num = time.strftime('%Y%m%d%H%M')
        self.version_cdn_dir = PROJECT_DIR + "/bin-release/web/CDN/" + VERSION + ".h5-dfh3/"  + self.version_num + '/'
        self.test_version_dir = PROJECT_DIR + "/bin-release/web/" + VERSION + "/"
        self.project_dir = PROJECT_DIR + "/"

        print "version", self.version_num

    def publicProject(self):

        pCommandStr = ""
        pCommandStr = "cd " + PROJECT_DIR + "\n"
        pCommandStr += "egret publish -version " + VERSION

        (status, output) = commands.getstatusoutput(pCommandStr)

        print "publicProject", status
        print output


    def publishResFile(self):

        print "--------开始发布配置文件-------"

        pVersionFile = VersionFile()
        pVersionFile.readVersionFile()

        srcDir = PROJECT_DIR + "/resource/default.res.json"
        dstDir = PROJECT_DIR + "/bin-release/web/" + VERSION +"/resource/default.res.json"

        resourceDir = PROJECT_DIR + "/bin-release/web/" + VERSION +"/resource/"

        file_object = open(srcDir)
        all_the_text = file_object.read()
        file_object.close()

        decodejson = json.loads(all_the_text)

        pResource = decodejson['resources']

        for item in pResource:
            item['url'] = item['url'] + "?v=" + pVersionFile.getVersionFileNum(item['url'], self.version_num, resourceDir)

        writeText = json.dumps(decodejson)

        writeFile = open(dstDir, 'w')
        writeFile.write(writeText)
        writeFile.close()

        pVersionFile.saveVersionFile()

        print "--------结束发布配置文件-------"


#------测试服

    def publishPhpFile(self):

        dstFile = PROJECT_DIR + "/bin-release/web/" + VERSION + "/game.php"
        srcFile = PROJECT_DIR + "/game.php"

        writeFile = open(dstFile, 'w')
        rf = open(srcFile, 'r')

        line = rf.readline()
        while line:
            text = self.parsePhp(line)
            writeFile.write(text)
            line = rf.readline()

        rf.close()
        writeFile.close()

    def parsePhp(self, text):
        matchObj = re.search("(.*?script src=\"main.min.js\?v=)(.*?)(\"></script>.*)", text)
        if matchObj:
            text = matchObj.group(1) + self.version_num + matchObj.group(3)
            print text
        return text

    def publicGameJs(self):
        srcFile = self.project_dir + "game_config.js"
        dstFile = self.test_version_dir + "game_config.js"

        writeFile = open(dstFile, 'w')
        rf = open(srcFile, 'r')

        line = rf.readline()
        while line:
            text = self.parseGameJs(line)
            writeFile.write(text)
            line = rf.readline()

        rf.close()
        writeFile.close()

    def parseGameJs(self, text):
        if text.find("game_version") != -1:
            text = 'var game_version = "' + self.version_num + '";'
        return text;



    def copyHtmlFile(self):
        self.sysCopyFile(self.project_dir + "egret_require.js", self.test_version_dir + "egret_require.js")
        self.sysCopyFile(self.project_dir + "game.html", self.test_version_dir + "game.html")


    def copyLogin(self):
        dstDir = self.test_version_dir
        shutil.copytree(Config.SVN_DIR + "/dfh3_resource/login/css", dstDir + "css")
        shutil.copytree(Config.SVN_DIR + "/dfh3_resource/login/image", dstDir + "image")
        self.copyFile(Config.SVN_DIR + "/dfh3_resource/login/login.html", dstDir + "login.html", self.parse)

    def copyLoginWeb(self):
        dstDir = self.test_version_dir
        shutil.copytree(Config.SVN_DIR + "/dfh3_resource/loginWeb/css", dstDir + "css")
        shutil.copytree(Config.SVN_DIR + "/dfh3_resource/loginWeb/img", dstDir + "img")
        self.copyFile(Config.SVN_DIR + "/dfh3_resource/loginWeb/login.html", dstDir + "login.html", self.parse)

#------测试服

    def copyRelease(self):
        srcDir = PROJECT_DIR + "/bin-release/web/" + VERSION
        dstDir = self.version_cdn_dir

        # shutil.rmtree(dstDir)
        shutil.copytree(srcDir, dstDir)
        shutil.rmtree(srcDir)

    def publishSDK(self):
        sdkDir = PROJECT_DIR + '/sdk/'
        versionDir = sdkDir + VERSION + 'SDK/'
        
        self.publishConfigJS()
        self.copyFile(sdkDir + '/egret_require.js', self.version_cdn_dir + 'egret_require.js', self.parse)
        self.copyFile(versionDir + VERSION + '.php', self.version_cdn_dir + VERSION + '.php', self.parse)
        self.copyFile(sdkDir + 'game.config.php', self.version_cdn_dir + 'game.config.php', self.parse)
        self.copyFile(sdkDir + 'game.sdk.php', self.version_cdn_dir + 'game.sdk.php', self.parse)

    def parseHtml(self, text):
        # "<img id="loading" src="resource/assets/preloading/loaading.gif" width="30%"/>"
        matchObj = re.search("(.*?)(<img id=\"FLogin_logo\" src=\")(.*?)(\" width=\"100%\" height=\"100%\"/>)(.*)", text)

        if matchObj:
            print matchObj.groups()
            text = matchObj.group(2) + matchObj.group(3) + '?' + self.version_num +  matchObj.group(4)
            print text

        return text

    def publishConfigJS(self):
        srcDir = PROJECT_DIR + '/sdk/' + VERSION + 'SDK/'
        dstFile = self.version_cdn_dir + 'game_config.js'

        writeFile = open(dstFile, 'w')

        writeFile.write('var game_version = "'+self.version_num+'";\r\n')
        writeFile.write('var game_preload_list = [\r\n')

        self.writeSRCFile(srcDir+'game_config.templete', writeFile, self.parse);
        self.writeSRCFile(PROJECT_DIR + '/sdk/game_config.templete', writeFile, self.parse);

        writeFile.write('\r\n];')
        writeFile.close()

    def parse(self, text):
        return text

    def copyFile(self, srcFile, dstFile, parseFunc):
        print srcFile,dstFile
        writeFile = open(dstFile, 'w')
        self.writeSRCFile(srcFile, writeFile, parseFunc)

        writeFile.close()

    def writeSRCFile(self, srcFile, writeFile, parseFunc):
        if os.path.isfile(srcFile):
            rf = open(srcFile, 'r')

            line = rf.readline()
            while line:
                text = parseFunc(line)
                writeFile.write("  " + text)
                line = rf.readline()

            rf.close()

    def copyDir(self, srcDir, dstDir):
        if os.path.exists(dstDir):
            shutil.rmtree(dstDir)
        shutil.copytree(srcDir, dstDir)

    def sysCopyFile(self, srcDir, dstDir):
        print "sysCopyFile", srcDir, dstDir
        shutil.copyfile(srcDir, dstDir)

    #拷贝到命令行提交的目录
    def copyToComDir(self, isAll = True):

        print "-----------copyToComDir-----------------"

        dstDir = "/Users/yaowan/liyan/h5_resource/"

        if isAll:
            self.copyDir(self.version_cdn_dir + "libs", dstDir + "libs")
            self.copyDir(self.version_cdn_dir + "resource", dstDir + "resource")
            shutil.copyfile(self.version_cdn_dir + "egret_require.js", dstDir + "egret_require.js")

        self.sysCopyFile(self.version_cdn_dir + "main.min.js", dstDir + "main.min.js")
        self.sysCopyFile(self.version_cdn_dir + "game_config.js", dstDir + "game_config.js")

    def doEuibooster(self):
        comand = "euibooster " + PROJECT_DIR + " " + self.test_version_dir
        print "doEuibooster", comand
        (status, output) = commands.getstatusoutput(comand)
        print output
