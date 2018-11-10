#!/user/bin/env python
#!encoding=utf-8
import os

'''框架目录路径管理'''

#根目录
root_path=os.path.dirname(os.path.dirname(__file__))

#Data目录
data_path=os.path.join(root_path,'Data/').replace('\\','/')

#ElementLoc目录
elementloc=os.path.join(root_path,'ElementLoc/').replace('\\','/')

#Image目录
image_path=os.path.join(root_path,'Image/').replace('\\','/')

#Log目录
log_path=os.path.join(root_path,'Log/').replace('\\','/')

#Report目录
report_path=os.path.join(root_path,'Report/').replace('\\','/')

#apk目录
apk_path=os.path.join(root_path,'apk/').replace('\\','/')

#app路径（根据索引指定app包）
app_path=os.path.join(apk_path,os.listdir(apk_path)[0])

#Conf目录
conf_path=os.path.join(root_path,'Conf/').replace('\\','/')

#testcase目录
testcase_path=os.path.join(root_path,'TestCases/').replace('\\','/')