import jieba
import json
import os
import jieba.analyse
def getKeyword():
	path = 'data/'
	#获取该路径下所有文件的文件名
	ls = os.listdir(path)
	#初始化
	all_keyword = []
	keywordlist = []
	final_sentence = ''
	#添加自定义字典
	jieba.load_userdict('mydict.txt')
	#添加自定义stopword
	jieba.analyse.set_stop_words('mystopword.txt')
	#对于每一个文件（每一个职位）
	for one_ls in ls:
		one_keyword = {}
		#加载数据
		with open(path+one_ls) as data:
			alldata = json.load(data)
		all_sentence = ''
		#将所有的职位描述信息添加到一起
		for one in alldata:
			all_sentence =all_sentence + ''.join(one['positionContent'])
		#将所有的英文变成小写
		all_sentence = all_sentence.lower()
		#对每一个职位提取关键词
		getanwer = jieba.analyse.extract_tags(all_sentence, topK=20, withWeight=False, allowPOS=())
		#getanwer = jieba.analyse.textrank(all_sentence)
		#获取该职位名称
		name = one_ls[0:-5]
		one_keyword[name] = getanwer
		keywordlist.extend(getanwer)
		all_keyword.append(one_keyword)
		all_key = ','.join(getanwer)
		print(name+':'+all_key+'\n')
		#获取所有的职位描述
		final_sentence = final_sentence + all_sentence
	#对所有的职位描述进行关键词分析
	finl_keyword = jieba.analyse.extract_tags(final_sentence, topK=20, withWeight=False, allowPOS=())
	print('所有职位：'+",".join(finl_keyword)+'\n')
	keywordlist.extend(finl_keyword)
	final_key = {}
	final_key['所有职位'] = finl_keyword
	all_keyword.append(final_key)
	keywordset = set(keywordlist)
	print('所有关键词：'+','.join(keywordset)+'\n')
	#存储获取到的信息
	with open('mydata.json','w') as mydata2:
		json.dump(all_keyword,mydata2)
		print('保存成功')
	return keywordset

def showdata():
	with open('data/Android.json') as data:
		alldata = json.load(data)
	all_sentence = ''
	for one in alldata:
		all_sentence =all_sentence + ''.join(one['positionContent'])
	all_sentence = all_sentence.lower()
	print(all_sentence)
	
def stopword():
	keywordset = list(getKeyword())
	getStopWord = []
	print('设置为停止词，1为是，任意字符为否')
	for key in keywordset:
		print('关键词：【'+key+'】')
		answer = input()
		if answer=='1':
			getStopWord.append(key)
			continue
		else:
			continue
	print('被停止的关键词有：'+','.join(getStopWord))
	if len(getStopWord) != 0:
		with open('mystopword.txt','a',encoding='utf-8') as stop_file:
			stop_file.write('\n'+'\n'.join(getStopWord))
	else:
		pass
		
#stopword()
path = 'data/'
#获取该路径下所有文件的文件名
ls = os.listdir(path)
allnumber = 0
for one_ls in ls:
	one_keyword = {}
	#加载数据
	with open(path+one_ls) as data:
		alldata = json.load(data)
	print(one_ls)
	print(len(alldata))
	allnumber = allnumber + len(alldata)
print(allnumber)