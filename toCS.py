#coding=utf-8
import os,sys,json
print ('by Rodger @Gzccc 14Soft class 3')

ROOT_DIR = os.getcwd()
CUR_DIR = os.getcwd() + "/res"
#三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
res = {}
for parent,dirname,filenames in os.walk(CUR_DIR):
	for dirname in dirname:
		#取子目录
		folder = parent[parent.find("res"):] + '/' + dirname
		folder = folder.replace('\\','/')
		#print ('::::::::::::' + folder)

	for filename in filenames:
		endP = filename.rindex('.');
		key = (filename[:endP] + '_' + filename[endP+1:]).upper()
		#print(filename)
		res[key] = folder + filename

#print (res)


## 替换res内容
# Resource
RES = ROOT_DIR + '/src/res.js'
'''
if not os.path.exists(RES):
	exit(-1)
lines = open(RES).readlines()
data = ''
for s in lines:
	data += s

match = re.match(r'var res = {',data)
#print (data)
print (match.group())
'''
### Update Resource.js File ###
data = json.dumps(res)
fp = open(RES,'w')
fp.write(data)
print 
print ('    The File is  "src/res.js" !!')

fp.close()
