#-----------------------------------------------------------------------------
# Script name: framecreator.py
# Description: Creates a frame based on a numpy array size 495 x 436.
# Creation date: 25/04/2020
# Author: avelezd
#------------------------------------------------------------------------------
import numpy
import matplotlib.pyplot as plt
import h5py
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

def plotframe(frame2plot,custcmap):
    
    plt.figure(figsize=(495,436))
    plt.imshow(frame2plot, cmap=custcmap)
    plt.axis('off')
    plt.show()
    breakpoint()
    try:
        plt.savefig('map_test.png', format='png')
    except:
        raise

def printarray(array2print, nublock, nuchannel):

    framearray = numpy.zeros([495, 436], dtype = int)

    # breakpoint()
    for rowidx in range(0, 494):
        for colidx in range(0,435):
            # print(array2print[0,3,0,rowidx,colidx,0], end ='')
            framearray[rowidx,colidx] = array2print[0,nublock,rowidx,colidx,nuchannel]
            print(array2print[0,100,rowidx,colidx,nuchannel], end ='')
        print('')

    return framearray


def getframematrix(h5content, startframe):
    channel = unknown = 2 
    for hidx in range(0, 494):
        # print('hidx: %s'%hidx)
        for widx in range (0,435):
            # print('widx: %s'%widx)
            print(h5content[0, startframe, hidx, widx, channel], end = '')
        print('')

def createcolormap(nuchannel):

    # ltcolors = ['#ffffff']
    ltcolors = []
    for colhex in range(0,253):

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
    
    # ltcolors.append('#ffffff')
    cmap = ListedColormap(ltcolors)
    return cmap
    # plot_examples([cmap])


if __name__ == "__main__":
    
    # print('start process')
    startframe = 0 # Frame que vamos a obtener, bloque de 5 mins en el dia

    inpath = '20180212_100m_bins.h5'

    f = h5py.File(inpath, 'r')
    # print('h5file loaded OK')
    keys = list(f.keys())
    # log.info('File load OK')

    a_group_key = list(f.keys())[0]
    data = list(f[a_group_key])
    data = [data[0:]]
    data = numpy.stack(data,axis=0)

    # print('new array created')
    framearray = numpy.zeros([495, 436], dtype = int)
    # framearray[10,] = 1
    # framearray[100, 20:300] = 1
    # framearray[240:245, 150:400] = 2

    # printarray(framearray)
    
    nublock = 180
    nuchannel = 0

    framearray = printarray(data, nublock, nuchannel)
    
    # print(data[0,100,100,1,1])
    # print('send array to print')
    # getframematrix(data, startframe)
    
    custcmap = createcolormap(nuchannel) 
    plotframe(framearray, custcmap)
