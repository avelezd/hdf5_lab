import logging
import h5py

class HDF5Reader:
 
    # logger = logging.getLogger(__name__)
    __filename__ = ''

    def __init__(self, inputfilename):
        self.logger = logging.getLogger(__name__)
        #__filename__ = None
        self.__filename__ = inputfilename
        self.logger.info(inputfilename)
        self.logger.info('HDF5File Instance created')

    def getfileproperties(self):
        '''Get the properties of a HDF5 file'''
    
        self.logger.info('start')
    
        f = h5py.File(self.__filename__, 'r')
    
        for filekey in list(f.keys()):
            self.logger.info('key: %s'%filekey)
    
            dset = f[filekey]
            self.logger.info(' file shape: %s \n file type: %s'%(dset.shape, dset.dtype))
            self.logger.info(dset[100, 100])
    
        self.logger.info('exit')
    
