#!/usr/bin/python

'''
    add a poem num into the collected_poem_num.txt
    if exist,do nothing,else add it to the file
    poem_num.txt reserve the line of collected_poem_num.txt
'''

import sys
def add_poem():
    poem_num = int(sys.argv[1])
    input_file = open("collected_poem_num.txt","r")
    for line in input_file:
        if poem_num == int(line):       #exist
            print 'poem exist,do nothing'
            return 1
    input_file.close()

    output_file = open("collected_poem_num.txt","a")    #not exist
    output_file.write(sys.argv[1]+"\n")
    output_file.close()
    
    #add line_number
    iutput = open("poem_num.txt","r")         
    line_num = iutput.readline()
    iutput.close()
    output = open("poem_num.txt","w")
    output.write(str(int(line_num)+1)+"\n")
    output.close()
    print "poem %d add successfully" % poem_num
    return 1

if __name__ == "__main__":
    add_poem()

