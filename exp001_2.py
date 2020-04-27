#------------------------------------------------------------------------------
# Script name: exp001_2.py
# Description: Transforms full length files in the test folders of all 3 cities into a similar
#   folder structure at the given output path, with the same file names but where the files are
#   of shape (1,5,3,495,436,3).
# Creation date: 12/04/2020
# Author: avelezd
#------------------------------------------------------------------------------

import sys, getopt
import os
import h5py
import numpy as np

from t4ctools.benchmarks.naive_moving_average.naive_baseline_mavg import list_filenames, load_test_file, load_input_data, write_data, create_directory_structure

cities = ['Berlin','Istanbul','Moscow']

def write_golden_dataset(utcPlus2, utcPlus3, inpath, outpath):
    create_directory_structure(outpath)
    # go through all cities
    for city in cities:
        # set relevant list
        indicies = utcPlus3
        if city == 'Berlin':
            indicies = utcPlus2
        
        # get file names
        data_dir = os.path.join(inpath, city, city+'_test')
        sub_files = list_filenames(data_dir)
        for f in sub_files:
            # load data
            data_sub = load_input_data(os.path.join(data_dir,f),indicies)
            
            # Modification to generate golden dataset
            outdata = data_sub
            
            #generate output file path
            outfile = os.path.join(outpath, city, city+'_test',f)
            write_data(outdata, outfile)
            print("City:{}, just wrote file {}".format(city, outfile))

            

if __name__ == '__main__':

    # gather command line arguments.
    inpath = ''
    outpath = ''
    # The following indicies are the start indicies of the 3 images to predict in the 288 time bins (0 to 287)
    # in each daily test file. These are time zone dependent. Berlin lies in UTC+2 whereas Istanbul and Moscow
    # lie in UTC+3.
    utcPlus2 = [30, 69, 126, 186, 234]
    utcPlus3 = [57, 114, 174,222, 258]

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hu:t:i:o:", ["utc2=", "utc3=","inpath=","outpath="])
    except getopt.GetoptError:
        print('usage: exp001_2.py -u <list utc+2> -t <list utc-3> -i <input directory path> -o <output path>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('usage: exp001_2.py -u <list utc+2> -t <list utc-3> -i <input directory path> -o <output path>')
            sys.exit()
        elif opt in ("-i","--inpath"):
            inpath = arg
        elif opt in ("-o","--outpath"):
            outpath = arg
        elif opt in ("-u","--utc2"):
            utcPlus2 = arg
        elif opt in ("-t","--utc3"):
             utcPlus3 = arg

    if inpath and outpath:
        write_golden_dataset(utcPlus2, utcPlus3, inpath, outpath)
    else:
        print('parameters --inpath and --outpath are required. try again.')

