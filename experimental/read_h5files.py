import logging # log generator library
import pdb # python code debugger

import h5py # HDF5 files library
import numpy

from mylogsetup import logfilesetup

filename = __file__
log = logfilesetup(filename.replace('.py','')) 

def looking4activity(hdf5str):
    log.info(type(hdf5str))
    
    idxb=idxh=idxw=idxc=0
    # breakpoint() 
    for block5m in hdf5str[0]:
        for heightpx in block5m:
            for widthpx in heightpx:
                for channelpx in widthpx:
                    log.info('position block[%s] h[%s] w[%s] c[%s]'%(idxb,idxh,idxw,idxc))
                    # breakpoint()
                    
                    if channelpx > 0:
                        log.info(channelpx)
                        idxc+=1


                # print('position block[%s] h[%s] w[%s]'%(idxb,idxh,idxw))
                idxw+=1
                idxc=0
                # breakpoint() 

            idxh+=1
            idxw=0
            # breakpoint() 

        log.info(block5m.shape)
        idxb+=1
        idxh=0

        # breakpoint() 


if __name__ == "__main__":

    log.info('BOF')

    # f = h5py.File('tstfolder/20180809_100m_bins.h5', 'r')
    f = h5py.File('../datasets/input/experiments/databenchmark/reduce/Berlin/Berlin_test/20180102_100m_bins.h5', 'r')
    keys = list(f.keys())
    log.info('File load OK')
        
    a_group_key = list(f.keys())[0]
    data = list(f[a_group_key])
    data = [data[0:]]
    data = numpy.stack(data,axis=0)
    log.info(data.shape)
    
    #breakpoint()
    looking4activity(data)

    log.info('EOF')


