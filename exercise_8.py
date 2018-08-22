#-*- coding:utf-8 -*-
import getopt
import sys
opts,args = getopt.getopt(sys.argv[1:],"h|i:o:",["help","in=","out="])
print(opts)
def usage():
    info = '''
            rediff ORIGINAL EDITED
            rediff EDITED
        '''
    print(info)
for opt,value in opts:
    if opt =="-i"or opt == "--in":
        input_file = value
    elif opt =="-o"or opt == "--out":
        output_file = value
    elif opt == "-h" or opt == "--help":
        print(123)
        usage()
