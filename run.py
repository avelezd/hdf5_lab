#------------------------------------------------------------------------------
# Script name: run.py
# Description: Script to read HDF5 files and testing.
# Creation date: 28/03/2020
# Author: avelezd
#------------------------------------------------------------------------------

# import pdb
# import torch
import numpy as np
# import h5py
import datetime
import sys, getopt
import logging
# import os
from os import walk, path

import HDF5Reader as h5r
from experimental.mylogsetup import logfilesetup
from t4ctools.utils.create_submissiontest_like import dummy_funk, write_output_files
from t4ctools.utils.h5shape import load_test_file, print_shape
from utils.constants import _source_path_, _output_path_

filename = __file__
logger = logfilesetup(filename.replace('.py',''))

def getdatashape(inpath):

    f = []
    
    for (dirpath, dirnames, filenames) in walk(inpath):

        logger.info('loop walk --  dirpath = %s'%dirpath)
        # breakpoint()
        
        for dirname in dirnames:
            logger.info(path.join(dirpath,dirname))
    
        for filename in filenames:
            file_path = "%s/%s"%(dirpath,filename)
            logger.info(path.join(dirpath,filename))
            filedata = load_test_file(file_path)
            print_shape(filedata, file_path)



# def submissiongenerator(input_path, output_path, out_data, random = False):
def submissiongenerator():
    
    logger.info('BOF')
    # dummy_funk()
    
    # Only zeros output setup
    # -----------------------------------------------------------
    outvalue = np.uint8(0)
    inpath = _source_path_
 
    logger.info(inpath)
    # getdatashape(inpath)
     
    d = datetime.datetime.today()
    d = d.strftime('%y%m%d%H%M%S')
    outpath = '%s%s_script'%(_output_path_, d)
    random = False
    
   #generate output data structure
    out_data = np.full(shape = (5,3,495,436,3), fill_value = outvalue, dtype = np.dtype(np.uint8)  )
    write_output_files(inpath, outpath, out_data, random=random)
    # -----------------------------------------------------------
    
    logger.info(outpath)
    getdatashape(outpath)

    # breakpoint()
    # h5obj = h5r.HDF5Reader(inputfile)
    # h5obj.getfileproperties()
    # breakpoint()

    logger.info('EOF')


if __name__ == "__main__":
    
    #--------------------------------------------------------
    # -i = inpath -o = outpath -v = outvalue
    #--------------------------------------------------------

#    inpath = ''
#    outpath = ''
#    outvalue = int(0)
#    out_data = np.zeros((5,3,495,436,3))
#    random = False
#    # breakpoint() 
# 
#    try:
#        opts, args = getopt.getopt(sys.argv[1:],"hi:o:v",["inpath=","outpath=","outvalue="])
#    except getopt.GetoptError:
#       print ('usage: run.py -i <inputpath> -o <outputpath> -v <constant value or "random">')
#       logger.info('Script parameters error')
#       logger.info('EOF')
#       sys.exit(2)
# 
#    for opt, arg in opts:
#       if opt == '-h':
#          print('run.py -i <inputpath> -o <outputpath> -v <constant value or "random">')
#          sys.exit()
#       elif opt in ("-i", "--inpath"):
#          inpath = arg
#       elif opt in ("-o", "--outpath"):
#          outpath = arg
#       elif opt in ("-v","--outvalue"):
#           if arg =='random':
#               random = True
#           else:
#               outvaluestr = arg
#               outvalue = np.uint8(int(outvaluestr))
#               
#               #generate output data structure
#               out_data = np.full(shape = (5,3,495,436,3), fill_value = outvalue, dtype = np.dtype(np.uint8))
#
#    submissiongenerator(inpath, outpath, out_data, random=random)

    submissiongenerator()

