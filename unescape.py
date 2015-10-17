#!/usr/bin/env python
#-*- coding:utf-8 -*-

from xml.sax.saxutils import *
import sys
import cgi
import urllib

class JsEDcode(object):
    """docstring for JsEDcode"""
    def __init__(self):
        super(JsEDcode, self).__init__()
        
    def encode(self, raw_str):
        return unicode(urllib.quote(raw_str), 'gbk')

    def decode(self, en_str):
        return urllib.unquote(en_str.replace("%u", "\\u").decode("unicode-escape"))

def usage():
    print '*'*60
    print "Usage: python unescape.py -[e|d] [-f <file>] [-o <file>]"
    print "-e       escape input string or file."
    print "-d       unescape string."
    print "-f       input from file."
    print "-o       output to file."
    print "-h       for help."
    print '*'*60
    exit(0)

def main():
    args = sys.argv
    ed = JsEDcode()

    if len(args) < 2 or '-h' in args:
        usage()

    if '-e' in args:
        flag = False
    elif '-d' in args:
        flag = True
    else:
        usage()

    if '-f' in args:
        in_file = args[3]
        r = open(in_file, "r")
        raw_str = r.read()
        r.close()
    else:
        raw_str = raw_input("请输入：")

    if flag:
        result = ed.decode(raw_str)
    else:
        result = ed.encode(raw_str)

    if '-o' in args:
        out_file = args[5]
        w = open(out_file, "w")
        w.write(result.encode('utf-8'))
        w.close()
    else:
        print flag and "解密结果：" or "加密结果："
        print "\033[1;32m" + result + "\033[0m"

        
if __name__ == '__main__':
    main()
