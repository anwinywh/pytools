#encoding:utf-8

import commands

#过滤工程文件
def filterProjectFile(pFilterArr):
    #工程
    pFilterArr.append("- *.pyc")
    pFilterArr.append("- .settings")
    pFilterArr.append("- .buildpath")
    pFilterArr.append("- .project")
    pFilterArr.append("- .idea")
    pFilterArr.append("- .svn")
    pFilterArr.append("- .DS_Store")


def getSrcPath(proName, version, isBranches = True):
    path = "/Users/yaowan/liyan/yaowan/dfh3/"
    if isBranches:
        path += "branches/"
    path += proName + "/" + "bin-release/web/CDN/really.h5-dfh3/" + version + "/"
    return path

def commit(pSrcDirectory, pDstDirectory, pFilterArr, port = "22"):

    if not pFilterArr:
        pFilterArr = []

    filterProjectFile(pFilterArr)

    #目录

    pFilterStr = ""
    for item in pFilterArr:
        pFilterStr += " --filter='" + item + "'"
    pCommandStr = "rsync -e 'ssh -p " + port +"' -av" + pFilterStr + " " + pSrcDirectory + " " + pDstDirectory

    print pCommandStr

    (status, output) = commands.getstatusoutput(pCommandStr)

    return output