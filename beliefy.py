#!/usr/bin/python

'''
   read the downloaded file,analize it,select something useful 
'''

import sys

def beliefy(input_filename,output_filename):
    input_file = open(input_filename,"r")
    output_file = open(output_filename,"a")
    tag = False
    for line in input_file:
        if line.find("原文：") != -1:
            tag = True
            continue
        if tag:
            if line.find("</div>") != -1:
                return
            output_file.write(line)




if __name__ == "__main__":
    beliefy(sys.argv[1],sys.argv[2])
