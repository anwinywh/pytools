#encoding:utf-8

import sys

sys.path.append("../../libs")

from HotVersionFile import HotVersionFile

HotVersionFile.Version = "170818145524"   #版本

# HotVersionFile.IsKeepVerify = True    #是否保留审核版本号
# HotVersionFile.Timing = "2017-08-18 14:14:00"  #定时器

allFiles = [
    "test/egret.php",
    "test/test248.php",
];

HotVersionFile.parseAllFile(allFiles)