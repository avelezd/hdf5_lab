#------------------------------------------------------------------------------
# Script name: exp001_3.py
# Description: 
# Creation date: 13/04/2020
# Author: avelezd
#------------------------------------------------------------------------------
import sys, getopt

from os import walk, path
from t4ctools.utils.h5shape import load_test_file, print_shape

def get_dataset_shape(inpath):
    f = []

    for (dirpath, dirnames, filenames) in walk(inpath):
        for dirname in dirnames:
            path.join(dirpath,dirname)
        for filename in filenames:
            file_path = "%s/%s"%(dirpath,filename)
            filedata = load_test_file(file_path)
            print_shape(filedata, file_path)


if __name__ == '__main__':

    inpath = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:",["inpath="])
    except getopt.GetoptError:
        print('usage: exp001_3.py -i <input directory path>')

    for opt, arg in opts:
        if opt == '-h':
            print('usage: exp001_3.py -i <input directory path>')
            sys.exit()
        elif opt in ('-i','--inpath'):
            inpath = arg

    if inpath:
        get_dataset_shape(inpath)
    else:
        print('parameter --inpath is required. try again.')
            
