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

def kmp(ss, pattern):
    pos = next(pattern)

    ss_len = len(ss)
    pattern_len = len(pattern)
    j = -1
    for i in range(ss_len):
        while j > -1 and pattern[j + 1] != ss[i]:
            j = pos[j]
        if pattern[j + 1] == ss[i]:
            j = j + 1
        if j == pattern_len - 1:
            print ('matched @: %s' % str(i - pattern_len + 1))
            j = pos[j]

kmp(u'BBC ABCDAB AGCTAGCAGCTAGCTsAGCTAGCAGCTAGCT', u'AGCTAGCAGCTAGCT')
