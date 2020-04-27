import logging
import h5py
import sys, getopt
from mylogsetup import logfilesetup   
 
# filename = __file__ 
# logger = logfilesetup(filename.replace('.py',''))
logger = logfilesetup('h5shape')

# To do's:
# - Create function to print shape of all h5 files in a directory

def getfileproperties(infile):
    '''Get the properties of a HDF5 file'''
    
    f = h5py.File(infile, 'r')
    for filekey in list(f.keys()):
    #    breakpoint()
        dset = f[filekey]
        # logger.info(' file shape: %s \n file type: %s'%(dset.shape, dset.dtype))
        print(dset.shape)
        print(dset[2, 1, 200 ])
        

if __name__ == '__main__':
    inpath = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:", ["inpath="])
    except getopt.GetoptError:
        print('usage: HDF5Reader.py -i <input file path>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage: HDF5Reader.py -i <input file path>')
            sys.exit()
        elif opt in ("-i", "--inputfile"):
            inpath = arg
    
    if inpath:
        getfileproperties(inpath)
    else:
        print('Parameter -inpath required. try again.')

