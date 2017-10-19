#!/usr/bin/env python
# encoding:utf8
def next(pattern):
    p_len = len(pattern) #模版字符串长度

    next = [-1] * p_len #模版字符串的所有字符的最大前后缀长度为0
    k = -1

    for i in range(1, p_len): #for循环，从第二个字符开始，依次计算每一个字符对应的next值
        while k > -1 and pattern[k + 1] != pattern[i]:
            k = next[k]
        if pattern[k + 1] == pattern[i]:#如果相等，那么最大相同前后缀长度加1
            k = k + 1
        next[i] = k
    return next

def kmp(fString, pattern):
    pNext = next(pattern)

    ss_len = len(fString)
    pattern_len = len(pattern)
    pj = -1
    for si in range(ss_len):
        #pattern首字母相同进入比较运算
        while pj > -1 and pattern[pj + 1] != fString[si]:
            pj = pNext[pj]
        if pattern[pj + 1] == fString[si]:
            pj = pj + 1
        if pj == pattern_len - 1:
            print ('matched @: %s' % str(si - pattern_len + 1))
            pj = pNext[pj]

kmp(u'BBC ABCDAB AGCTAGCAGCTAGCTsAGCTAGCAGCTAGCT', u'AGCTAGCAGCTAGCT')
