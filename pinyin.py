#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com

    Modified by glide.ming@gmail.com:
    - add Python 3 support
    - some adjustments
    note: not test setup script yet.
"""

__version__ = '0.9'
__all__ = ["PinYin"]

import sys
import os.path

if sys.version < '3':
    import codecs

    def u(x):
        return codecs.unicode_escape_decode(x)[0]
else:
    def u(x):
        return x


class PinYin(object):
    def __init__(self, dict_file='word.data'):
        self.__word_dict = {}
        self.__dict_file = dict_file
        self.__load_word()

    def __load_word(self):
        if not os.path.exists(self.__dict_file):
            raise IOError("word file not found: %s" % self.__dict_file)

        with open(self.__dict_file) as fh:
            for line in fh:
                values = line.split('    ')
                if len(values) < 2:  # invalid record
                    continue
                self.__word_dict[values[0]] = values[1]

    def get_full_pinyin(self, chinese_string):
        result = []

        for char in u(chinese_string):
            key = '%X' % ord(char)
            pinyin = self.__word_dict.get(key, char).split()[0][:-1].lower()
            result.append(pinyin)

        return result

    def get_abbr_pinyin(self, chinese_string):
        full_result = self.get_full_pinyin(chinese_string)
        result = [v[0] if v else '' for v in full_result]
        return ''.join(result)

    def get_full_pinyin_separated(self, chinese_string, sep=" "):
        full_result = self.get_full_pinyin(chinese_string)
        return sep.join(full_result)


if __name__ == "__main__":
    test = PinYin()
    string = "钓鱼岛是中国的"
    print("in: %s" % string)
    print("full pinyin: %s" % str(test.get_full_pinyin(string)))
    print("full pinyin: %s" % test.get_full_pinyin_separated(string, sep="-"))
    print("abbr: %s" % test.get_abbr_pinyin(string))
