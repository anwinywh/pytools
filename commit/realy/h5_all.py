#encoding:utf-8

import sys
import commands

sys.path.append("../libs")

import common

pSrcDirectory = "/Users/yaowan/liyan/h5_resource"
pClean = "chmod -R 777 " + pSrcDirectory
pSrcDirectory += "/"

(status, output) = commands.getstatusoutput(pClean)

print output
print pSrcDirectory

# pPlatform = "awy.h5-dfh3"    #爱微游
# pPlatform = "youku.h5-dfh3"  #游酷
# pPlatform = "youku2.h5-dfh3" #游酷2
# pPlatform = "yw.h5-dfh3"     #官服
# pPlatform = "yyb.h5-dfh3"    #应用宝
# pPlatform = "qqbrowser.h5-dfh3"  #qq浏览器
# pPlatform = "wanba.h5-dfh3"  #玩吧   注意CDN

if not pPlatform:
    exit()

#外网
pDstDirectory = "root@182.254.194.28:/ryzc/h5-dfh3-web/" + pPlatform

print pDstDirectory

pFilterArr = []

print common.commit(pSrcDirectory, pDstDirectory, pFilterArr, "20163")