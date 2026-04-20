import jieba
jieba.load_userdict('user_dictionary.txt')
# user_dict.txt 每行: 詞語 詞頻 詞性（詞頻為可選）
s = '你好，請問雲林科技大學有數據分析的教授嗎?'
print(list(jieba.cut(s)))
# 全模式
print(list(jieba.cut(s, cut_all=True)))
# 搜索引擎模式
print(list(jieba.cut_for_search(s)))