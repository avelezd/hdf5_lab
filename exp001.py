#------------------------------------------------------------------------------
# Script name: exp001.py
# Description: Creating submission datasets.
# Creation date: 11/04/2020
# Author: avelezd
#------------------------------------------------------------------------------
import datetime
import sys
import logging
import numpy as np

from t4ctools.utils.create_submissiontest_like import write_output_files

logger = logging.getLogger()

def write_random_output_files(input_path, output_path):

    logger.info('Parameters:\ninput_path:[%s]\noutput_path:[%s]'%(input_path, output_path))

    outvalue = np.uint8(0)

    d = datetime.datetime.today()
    d = d.strftime('%y%m%d%H%M%S')
    outpath = '%s%s_script_random'%(output_path, d)
    random = True

    # generate output data structure
    out_data = np.full(shape = (5,3,495,436,3), fill_value = outvalue, dtype = np.dtype(np.uint8)  )
    write_output_files(input_path, outpath, out_data, random=random)

    logger.info('New random dataset path:[%s]'%outpath)


def write_scalar_output_files(input_path, output_path, output_value):
    
    logger.info('Parameters:\ninput_path:[%s]\noutput_path:[%s]\noutput_value:[%s]'%(input_path, output_path, output_value))

    outvalue = np.uint8(output_value)
   
    d = datetime.datetime.today()
    d = d.strftime('%y%m%d%H%M%S')
    # outpath = '%s%s_script_scalar_%s'%(output_path, d, output_value)
    outpath = '%sscript_scalar_%s'%(output_path, output_value)

    random = False

    # generate output data structure
    out_data = np.full(shape = (5,3,495,436,3), fill_value = outvalue, dtype = np.dtype(np.uint8)  )
    write_output_files(input_path, outpath, out_data, random=random)

    logger.info('New scalar dataset path:[%s]'%outpath)


def write_zeros_output_files(input_path, output_path):
    
    logger.info('Parameters:\ninput_path:[%s]\noutput_path:[%s]'%(input_path, output_path))

    outvalue = np.uint8(0)
   
    d = datetime.datetime.today()
    d = d.strftime('%y%m%d%H%M%S')
    # outpath = '%s%s_script_zeros'%(output_path, d)
    outpath = '%sscript_zeros'%output_path
    random = False

    # generate output data structure
    out_data = np.full(shape = (5,3,495,436,3), fill_value = outvalue, dtype = np.dtype(np.uint8)  )
    write_output_files(input_path, outpath, out_data, random=random)

    logger.info('New zeros dataset path:[%s]'%outpath)


if __name__ == "__main__":
    print('Not implemented yet!')
    sys.exit(2)

