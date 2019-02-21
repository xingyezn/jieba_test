import jieba
import json
import os
import jieba.analyse
def test():
    path = 'data/'
    #获取该路径下所有文件的文件名
    ls = os.listdir(path)
    #初始化
    all_keyword = []
    final_sentence = ''
    #添加自定义字典
    jieba.load_userdict('mydict.txt')
    #添加自定义stopword
    jieba.analyse.set_stop_words('mystopword.txt')
    #对于每一个文件（每一个职位）
    for one_ls in ls[0:1]:
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
        getanwer = jieba.analyse.extract_tags(all_sentence, topK=50, withWeight=False, allowPOS=())
        #getanwer = jieba.analyse.textrank(all_sentence)
        #获取该职位名称
        name = one_ls[0:-5]
        one_keyword[name] = getanwer
        all_keyword.append(one_keyword)
        all_key = ','.join(getanwer)
        print(name+':'+all_key)
        #获取所有的职位描述
        final_sentence = final_sentence + all_sentence
    #存储获取到的信息
    with open('mydata.json','w') as mydata2:
        json.dump(all_keyword,mydata2)
    #对所有的职位描述进行关键词分析
    finl_keyword = jieba.analyse.extract_tags(final_sentence, topK=10, withWeight=False, allowPOS=())
    print(",".join(finl_keyword))
    #print(all_keyword)

        #for g in getanwer:
        #    print(g)
        #for w in jieba.cut(one_data):
        #    print(w)

def showdata():
    with open('data/Android.json') as data:
        alldata = json.load(data)
    all_sentence = ''
    for one in alldata:
        all_sentence =all_sentence + ''.join(one['positionContent'])
    all_sentence = all_sentence.lower()
    print(all_sentence)
    
test()
#showdata()