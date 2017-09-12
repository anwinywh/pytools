#encoding:utf-8

import sys

sys.path.append("../../libs")

from HotVersionFile import HotVersionFile

exit()

HotVersionFile.Version = "170818145524"   #版本

# HotVersionFile.IsKeepVerify = True    #是否保留审核版本号
# HotVersionFile.Timing = "2017-08-18 14:14:00"  #定时器

#----------检查下有没有新加文件------------
allFiles = [
    #安卓
    "android/hunfu.php",
    "android/yyb.php",

    #ios
    "ios/dfh3_wancms_20170721.php",
    "ios/dfhsan_20170113.php",
    "ios/dfhsan_20170321.php",
    "ios/dfhsan_20170510.php",
    "ios/dfhsan_20170713.php",
    "ios/dfhsana_20170223.php",
    "ios/dfhsanb_20170223.php",
    "ios/dfhsanc_20170223.php",
    "ios/egret.php",
    "ios/ios_20170113.php",
    "ios/ver_20170113.php",
];

HotVersionFile.parseAllFile(allFiles)