'''
Created on Oct 08, 2021

@author: lucasvictor
'''

import os, sys, getopt


def main(argv):
#    configfile = '../conf/dump.cfg'
#    tablefile = '../conf/tables.cfg'
#    outputdir = '../out'

 #   configfile = '../conf/dump.cfg'
 #   tablefile = '../conf/tables.cfg'
    outputdir = '../teste'

    try:
        opts, args = getopt.getopt(argv, "ht:c:o:", ["tfile=", "cfile=", "odir="])
    except getopt.GetoptError:
        print('dump.py -t <tablefile> -c <configfile> -o <outputdir>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('dump.py -t <tablefile> -c <configfile> -o <outputdir>')
            sys.exit()
        elif opt in ("-t", "--tfile"):
            tablefile = arg
        elif opt in ("-c", "--cfile"):
            configfile = arg
        elif opt in ("-o", "--odir"):
            outputdir = arg

    if not os.path.exists(outputdir):
        os.makedirs(outputdir)

#    ReadConfig(configfile, tablefile)
#    Engine.getDump(outputdir)


if __name__ == "__main__":
    main(sys.argv[1:])



