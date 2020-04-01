#------------------------------------------------------------------------------
# Script name: run.py
# Description: Script to read HDF5 files and testing.
# Creation date: 28/03/2020
# Author: avelezd
#------------------------------------------------------------------------------

# import pdb
# import torch
# import numpy
# import h5py
import sys, getopt
import logging

import HDF5Reader as h5r

from utils.constants import _LOG_NAME_, _LOG_FORMAT_, _LOG_INFO_FILENAME_, _LOG_FILEPATH_

# Create logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# File Handler which logs even degug messages
fh = logging.FileHandler(_LOG_FILEPATH_ + _LOG_INFO_FILENAME_)
fh.setLevel(logging.INFO)

# Console Handler with higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# Create formater and add it to handlers
formatter = logging.Formatter(_LOG_FORMAT_)
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add Handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)


def main(inputfile):

    logger.info('BOF')

    # breakpoint()
    h5obj = h5r.HDF5Reader(inputfile)
    h5obj.getfileproperties()
    # breakpoint()

    logger.info('EOF')


if __name__ == "__main__":
    hdf5filepath = 'datasets/input/20180622_100m_bins.h5'
    inputfile =  ''
    outputfile = ''
    
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
       print ('script_name.py -i <inputfile> -o <outputfile>')
       logger.info('Script parameters error')
       logger.info('EOF')
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

