import jieba

# 1.jieba分词
# 有三种模式，精确模式、全模式、搜索引擎模式

str = "小明毕业于北京邮电大学，后来在百度工作"

# 精确模式，试图将句子最精确地切开，适合文本分析
seg_list = jieba.cut(str, cut_all=False)
print(' '.join(seg_list))

# 默认是精确模式
seg_list = jieba.cut(str, cut_all=False)
print(' '.join(seg_list))

# 全模式，把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义
seg_list = jieba.cut(str, cut_all=True)
print(' '.join(seg_list))

# 搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词
seg_list = jieba.cut_for_search(str)
print(' '.join(seg_list))


# 2.jieba扩充词库分词

sentence = "张三是创新办主任也是云计算方面的专家"

words1 = jieba.cut(sentence)
print(' '.join(words1))

jieba.load_userdict("userdict.txt")

words2 = jieba.cut(sentence)
print(' '.join(words2))


# 3.统计词频
data = ["中国北京海淀西土城10号 ，", "中国海淀西土城6号。", "中国上海世博园东方明珠10号"]

stopwords = []
with open('stopwords.txt', "r", encoding='utf-8') as f:
    line = f.readline()
    while line:
        stopwords.append(line[:-1])
        line = f.readline()
stopwords = set(stopwords)

words = []
for i in range(len(data)):
    seg_list = list(jieba.cut(data[i]))
    word = [w for w in seg_list if w not in stopwords]
    words.extend(word)
print(len(words))

word_frequency = {}
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

print(word_frequency) # 字典
print(word_frequency.items()) # 以列表返回可遍历的(键, 值)元组数组

word_frequency_sorted = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True) # reverse=True 降序
print(word_frequency_sorted[0:3])




