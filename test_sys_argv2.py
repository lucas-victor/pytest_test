
import os, sys, getopt
import subprocess

def main(argv):

    try:
        opts, args = getopt.getopt(argv, "ht:", ["tfile="])
    except getopt.GetoptError:
        print('test_sys_argv2.py -t <tablefile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test_sys_argv2.py -t <testfile>')
            sys.exit()
        elif opt in ("-t", "--tfile"):
            testfile = arg
            print(f'testfile = {testfile}')


    print(len(sys.argv))
#    if not os.path.exists(outputdir):
#       os.makedirs(outputdir)

if __name__ == '__main__':
    main(sys.argv[1:])




