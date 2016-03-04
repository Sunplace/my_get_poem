#!/usr/bin/python

'''
    download the http page
'''

import sys
from urllib import urlopen

def download_page(page_num):
    url = "http://so.gushiwen.org/view_" + page_num + ".aspx"
    webdata = urlopen(url).read()
    output = open("__" + page_num + "__" + ".html" ,'w')
    output.write(webdata)
    output.close()

if __name__ == "__main__":
    download_page(sys.argv[1])
