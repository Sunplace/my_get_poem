#!/usr/bin/python

'''
    read the poem_num.txt from the collected_poem_num.txt select a
    random poem.
'''

import random

def rand_poem():
    #generate a random number
    input_file = open("poem_num.txt","r")
    line_num = input_file.readline()
    rand_num = random.randint(1,int(line_num))
    input_file.close()

    #select the random line of collected_poem_num.txt
    input_file2 = open("collected_poem_num.txt","r")
    for line in input_file2:
        rand_num = rand_num-1
        if rand_num == 0:
            print '%s' %line
            return int(line)

if __name__ == "__main__":
    rand_poem()

