import jieba
import json
import os
import jieba.analyse
def test():
    path = 'data/'
    ls = os.listdir(path)
    #print(ls[0][0:-5])
    all_keyword = []
    final_sentence = ''
    jieba.load_userdict('mydict.txt')
    jieba.analyse.set_stop_words('mystopword.txt')
    for one_ls in ls[0:1]:
        one_keyword = {}
        with open(path+one_ls) as data:
            alldata = json.load(data)
        all_sentence = ''
        for one in alldata:
            all_sentence =all_sentence + ''.join(one['positionContent'])
        all_sentence = all_sentence.lower()
        getanwer = jieba.analyse.extract_tags(all_sentence, topK=50, withWeight=False, allowPOS=())
        #getanwer = jieba.analyse.textrank(all_sentence)
        name = one_ls[0:-5]
        one_keyword[name] = getanwer
        all_keyword.append(one_keyword)
        all_key = ','.join(getanwer)
        print(name+':'+all_key)
        final_sentence = final_sentence + all_sentence
    with open('mydata.json','w') as mydata2:
        json.dump(all_keyword,mydata2)
        
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