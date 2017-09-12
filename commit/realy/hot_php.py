#encoding:utf-8

import sys
import commands

sys.path.append("../../libs")
import common

# exit()

platform = "test"

# platform = "android"
# platform = "ios"

pSrcDirectory = "/Users/yaowan/liyan/yaowan/dfh3/dfh3_hot/" + platform +"/"
pClean = "chmod -R 777 " + pSrcDirectory

(status, output) = commands.getstatusoutput(pClean)

print output
print pSrcDirectory

#外网
pDstDirectory = "root@182.254.194.28:/ryzc/h5-dfh3-web/rgzy.dfh3/" + platform + "/"

print pDstDirectory

print common.commit(pSrcDirectory, pDstDirectory, [], "20163")