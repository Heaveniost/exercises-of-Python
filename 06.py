"""
 你有一个目录，放了你一个月的日记，都是txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
"""
from collections import Counter

import os, re 


def get_diary_path():
    list = []
    dir_path = './diary'
    for path in os.listdir(dir_path):
        list.append(dir_path + '/' + path)
    return list


def get_common_word(paths):
    common_words = []
    for path in paths:
        words = []
        with open(path, 'r') as f:  # 打开文件
            data = f.read().lower()
            words = re.findall(r"[a-z\']+", data)
        common_word = Counter(words).most_common(1)  # 获取此篇中出现频率最高的一个词汇
        common_words.append(common_word)
    return common_words


if __name__ == '__main__':
    paths = get_diary_path()
    words = get_common_word(paths)
    print(words)