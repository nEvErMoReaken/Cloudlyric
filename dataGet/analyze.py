# -*- coding: utf-8 -*-
import logging
import os
import json
import jieba.posseg as posseg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.preprocessing import normalize


from dataGet import naming

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

pos_retained = set('nvsat')  # 应该被保留的词性

def load_stopwords():
    """
    加载停用词
    :return:
    """
    stopwords = set()
    with open(os.path.join(naming.ProjectPath, naming.DictDirectory, naming.StopwordsFileName),encoding='utf-8') as file:
        for line in file:
            stopwords.add(line[:-1])  # 切除换行符
    stopwords.add(' ')
    return stopwords


def get_words_freq(stopwords, lyrics_dir):
    """
    统计词频
    :param stopwords: 停用词集合
    :type stopwords: set(stopword1, stopword2, ...)
    :param lyrics_dir: 歌词路径
    :return: {word1: freq, word2: freq, ...}
    """
    # 迭代每个文件，对每个文件，每一行分词，去除停用词后，统计词频
    words_freq = {}
    for file_name in os.listdir(lyrics_dir):
        try:
            with open(os.path.join(lyrics_dir, file_name),encoding='utf-8') as file:
                for line in file:
                    words = posseg.cut(line.strip())
                    for word, pos in words:
                        if word not in stopwords and pos[0] in pos_retained:  # 过滤停用词,词性筛选
                            if word not in words_freq:
                                words_freq[word] = 1
                            else:
                                words_freq[word] += 1
        except IOError as ioe:
            logger.warning('异常信息:%s' % ioe)
        except BaseException as be:
            logger.warning('异常信息:%s' % be)
    return words_freq




if __name__ == '__main__':
    stop_words = load_stopwords()
    words_freq = get_words_freq(stop_words, os.path.join(naming.ProjectPath, naming.LyricsDirectory))
    print(words_freq)
    with open(r"C:\Users\admin\PycharmProjects\Cloudlyric\data\dirtydata.json","w",encoding='utf-8') as f:
        json.dump(words_freq,f)
