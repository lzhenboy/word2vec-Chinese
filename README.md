# word2vec-Chinese
a tutorial for training Chinese-word2vec using Wiki corpus  

word2vec词向量是NLP领域的基础，如何快速地训练出符合自己项目预期的词向量是必要的。

【注】：本项目主要目的在于快速的构建通用中文word2vec词向量，关于word2vec原理后期有时间再补充（nlp新手，文中不足之处欢迎各位大神批评指正，亦可共同交流学习）。

## 0. 环境要求
* python 3.6<br>
* 依赖：numpy，gensim，opencc，jieba

## 1. 获取中文语料库
想要训练好word2vec模型，一份高质量的中文语料库是必要的，目前常用质量较好的中文语料库为维基百科的中文语料库。
* 维基百科的中文语料库质量高、领域广泛而且开放，其每月会将所有条目打包供大家下载使用，可以点击： https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2 直接下载最新版（也可以访问：https://dumps.wikimedia.org/zhwiki/ 获取历史版本）。
* 由于某些的原因，中文维基百科的条目到目前只有91万多条，而百度百科、互动百科都有千万条了（英文维基百科也有上千万了）。尽管中文维基百科语料条数较少，但仍不失为最高质量的中文语料库。（ps：百度百科、互动百科多用爬虫爬取内容，不少记录质量差。）

## 2. 中文语料库预处理
### 2.1 将xml的Wiki数据转换为text格式
* python的gensim包中提供了WikiCorpus方法可以直接处理Wiki的语料库（xml的baz格式，无需解压），具体可参见脚本[parse_zhwiki_corpus.py](https://github.com/lzhenboy/word2vec-Chinese/blob/master/parse_zhwiki_corpus.py/)。<br>
执行以下命令可以将xml的Wiki语料库转换为txt格式：<br>
```python
python parse_zhwiki.py -i zhwiki-latest-pages-articles.xml.bz2 -o corpus.zhwiki.txt
```
* 生成的```corpus.zhwiki.txt```有1.04G，共有32w+的documents（每行为1个doc）。
### 2.2 中文简繁体转换
* Wiki语料库中的文档含有繁体中文，可以利用工具包opencc将繁体转换为简体，具体可参见脚本[chinese_t2s.py](https://github.com/lzhenboy/word2vec-Chinese/blob/master/chinese_t2s.py)。<br>
执行以下命令可以将语料库中的繁体中文转化为简体中文：<br>
```python
python chinese_t2s.py -i corpus.zhwiki.txt -o corpus.zhwiki.simplified.txt
```
* 得到简体中文的Wiki语料库```corpus.zhwiki.simplified.txt```。

### 2.3 去除英文和空格
* 现在得到的语料库中有许多英文（也有些许日文、德文等），为避免影响所训练的词向量效果，我们将其中的英文以及空格做了删除（其他日文、德文等后续有时间再进行处理），具体可参见脚本[remove_en_blank.py](https://github.com/lzhenboy/word2vec-Chinese/blob/master/remove_en_blank.py)。<br>
执行以下命令可以将语料库中的英文以及空格删除：<br>
```python
python remove_en_blank.py -i corpus.zhwiki.simplified.txt -o corpus.zhwiki.simplified.done.txt
```
* 得到去除英文和空格的中文语料库```corpus.zhwiki.simplified.done.txt```。

### 2.4 中文分词（jieba分词）
* 想要完成word2vec的训练，语料库需要进行分词处理，这里采用python的jieba分词，具体可参见脚本[corpus_zhwiki_seg.py](https://github.com/lzhenboy/word2vec-Chinese/blob/master/corpus_zhwiki_seg.py)。<br>
执行以下命令可以将语料库中的中文语料进行分词：<br>
```python
python corpus_zhwiki_seg.py -i corpus.zhwiki.simplified.done.txt -o corpus.zhwiki.segwithb.txt
```
* 得到分词之后的中文语料库```corpus.zhwiki.segwithb.txt```。 


## 3. word2vec模型训练
* python的gensim模块提供了word2vec训练的函数，极大地方便了模型训练的过程。具体可参考脚本[word2vec_train.py](https://github.com/lzhenboy/word2vec-Chinese/blob/master/word2vec_train.py)。<br>
执行以下命令得到所训练的word2vec模型和词向量：<br>
```python
python word2vec_train.py -i corpus.zhwiki.segwithb.txt -m zhwiki.word2vec.model -v zhwiki.word2vec.vectors -s 400 -w 5 -n 5
```
* 得到基于Wiki中文语料库训练好的word2vec模型和词向量：<br>
word2vec模型文件：<br>
(1) ```zhwiki.word2vec.model```<br>
(2) ```zhwiki.word2vec.model.trainables.syn1neg.npy```<br>
(3) ```zhwiki.word2vec.model.wv.vectors.npy```<br>
word2vec词向量文件：<br>
```zhwiki.word2vec.vectors```


## 4. word2vec模型测试
* 模型训练好之后，对模型进行测试，具体可参见脚本[word2vec_test.py](https://github.com/lzhenboy/word2vec-Chinese/blob/master/word2vec_test.py)。<br>
示例代码如下：<br>
```python
from gensim.models import Word2Vec
word2vec_model = Word2Vec.load(zhwiki.word2vec.model)
# 查看词向量
print('北京：', word2vec_model['北京'])
# 查看相似词
sim_words = word2vec_model.most_similar('北京')
for w in sim_words:
print(w)
```


## 参考与致谢
1. https://github.com/zishuaiz/ChineseWord2Vec
2. https://www.jianshu.com/p/ec27062bd453
3. https://blog.csdn.net/jdbc/article/details/59483767<br>
ps:参考文献无法一一列举，如有问题请联系我添加！
