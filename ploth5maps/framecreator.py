#-----------------------------------------------------------------------------
# Script name:  framecreator.py
# Description:  Creates a frame based on a numpy array size 495 x 436.
# Creation date:25/04/2020
# Last update:  17/05/2020
# Author:       avelezd
#------------------------------------------------------------------------------
import numpy
import matplotlib.pyplot as plt
import h5py
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

def extractmapcontent(h5filepath):
    '''Extracts data from h5file and change format to numpy array'''
    h5file = h5py.File(h5filepath, 'r')
    keys = list(h5file.keys())
    a_group_key = list(h5file.keys())[0]
    
    h5data = list(h5file[a_group_key])
    h5data = [h5data[0:]]
    h5data = numpy.stack(h5data,axis=0)
    
    print('Data from HDF5 file extracted')
    return h5data

def createcolormap(nuchannel, startwhite=False):
    '''Creates a custom color map based on the channel selected'''
    if startwhite:
        ltcolors = ['#ffffff']
    else:
        ltcolors = []
    
    for colhex in range(0,255):

        hexstr = hex(colhex).replace('0x','')

        if len(hexstr) == 1:
            hexstr = '0%s'%hexstr
        
        if nuchannel == 0:
            rgbstr = '#%s0000'%hexstr # red
        elif nuchannel == 1:
              rgbstr = '#00%s00'%hexstr # green
        else:
            rgbstr = '#0000%s'%hexstr # blue

        ltcolors.append(rgbstr)
    
    cmap = ListedColormap(ltcolors)
    print('Color map created base on channel %s'%nuchannel)
    return cmap

def plotsaveframe(frame2plot, custcmap, nublock, nuchannel, outpath):
    '''Plot an image and pops up a window to show it, the image is saved after close de window'''    
    fig = plt.figure(figsize=(495,436))
    plt.imshow(frame2plot, cmap=custcmap)
    plt.axis('off')
    plt.title('Frame # %s'%nublock)

    plt.show()
    fig.savefig('%s/%s_%s.png'%(outpath, nublock, nuchannel))
    plt.close(fig)

def getblockarray(array2print, nublock, nuchannel):
    '''Get the numeric numpy array from a h5file by channel'''
    framearray = numpy.zeros([495, 436], dtype = int)

    # breakpoint()
    for rowidx in range(0,495):
        for colidx in range(0,436):
            framearray[rowidx,colidx] = array2print[0, nublock, rowidx, colidx, nuchannel]

    return framearray

def createchannelmap(h5content, colormap, nuchannel, outpath):
    '''print frames from hdf5files'''
    framearray = numpy.zeros([495, 436], dtype = int)
    
    # generates a frame for each time block
    for blockidx in range(0,288):
        print('Bloque: %s'%blockidx)
        framearray = getblockarray(h5content, blockidx, nuchannel)
        plotsaveframe(framearray, colormap, blockidx, nuchannel, outpath) 
 
