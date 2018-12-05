# 2018.11.28
# -*- coding:utf-8 -*-
# maxzjs
# md5 加盐：由于常用的MD5值很容易被计算出来，通过对原始口令加一个复杂字符串来实现加强保护

import os, hashlib

def calc_md5(password):
    return get_md5(password + 'the-Salt')

# 确保Salt这个添加的字符串不被黑客知道，简单口令也很难反推明文口令


def get_md5(pw):
    md5 = hashlib.md5()
    md5.update(pw.encode('utf-8'))
    return md5.hexdigest()

def getmd5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()   #简写形式