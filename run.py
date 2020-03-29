# Name:
# Description: Script to read HDF5 files and testing

# import numpy
import h5py
import sys, getopt
# import pdb

import torch

class Snake:
    pass



def getfileproperties(filepath):
    print('hello world from script!')

    # hdf5filepath = '/home/avelezd/code/02_thesis/01_datasets/01_iarai_berlin/Berlin/Berlin_training/20180220_100m_bins.h5'

    # print(filepath)
    # h5py.run_tests()
    f = h5py.File(filepath, 'r')
    # ltkeys = list(f.keys())
    
    for filekey in list(f.keys()):
        print('key: %s'%filekey)
    
        dset = f[filekey]
        print(' file shape: %s \n file type: %s'%(dset.shape, dset.dtype))
        print(dset[100, 100])
       
# =================================================================================

def main(argv):
    
    hdf5filepath = 'datasets/input/20180622_100m_bins.h5'
    inputfile =  ''
    outputfile = ''
    
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
       print ('script_name.py -i <inputfile> -o <outputfile>')
       sys.exit(2)
 
    for opt, arg in opts:
       if opt == '-h':
          print ('script_name.py -i <inputfile> -o <outputfile>')
          sys.exit()
       elif opt in ("-i", "--ifile"):
          inputfile = arg
       elif opt in ("-o", "--ofile"):
          outputfile = arg
    
    if not inputfile:
        inputfile = hdf5filepath
     
    getfileproperties(inputfile)

    # breakpoint()
    # print('Input file is "', inputfile)
    # print('Output file is "', outputfile)

# =================================================================================


if __name__ == "__main__":
    main(sys.argv[1:])

