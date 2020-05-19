#-----------------------------------------------------------------------------
# Script name:  run.py
# Description:  run functions required to create a sample animated gif 
#               from hdf5 files.
# Creation date:17/05/2020
# Last update:  18/05/2020
# Author:       avelezd
#------------------------------------------------------------------------------
import numpy
import sys, getopt
from framecreator import extractmapcontent, createcolormap, createchannelmap
from gifgenerator import cropimages, animateframes


_inpath = 'input/datasets/B20180215_100m_bins.h5'
_frames_outpath = 'output/map_frames'
_cropped_frames_outpath = 'output/cropped_frames'
_animated_gif_outpath = 'output/gifs'

def __get_file_name__(inpath):
    filenamearray = inpath.split('/')
    filename = filenamearray[len(filenamearray) - 1]
    filename = filename.replace('.h5','')
    return filename

def converth52map(inpath, nuchannel):
    '''Main function to create a map pixel based  from a h5file'''
    
    ## generate the frames
    h5content = extractmapcontent(inpath)
    colormap = createcolormap(nuchannel)
    createchannelmap(h5content, colormap, nuchannel, _frames_outpath)
    
    # set format to images and creates gif
    gifname = __get_file_name__(_inpath)
    cropimages(_frames_outpath, _cropped_frames_outpath)
    animateframes(_cropped_frames_outpath, _animated_gif_outpath, nuchannel, gifname)

if __name__ == "__main__":

    inpath = nuchannel = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:c:",["inpath=", "channel="])
    except getopt.GetoptError:
        print('usage: run.py -i <input file> -c <channel>')

    for opt, arg in opts:
        if opt == '-h':
            print('usage: run.py -i <input file> -c <channel>')
            sys.exit()
        elif opt in ('-i','--inpath'):
            inpath = arg
        elif opt in ('-c','--channel'):
            nuchannel = int(arg)

    if not inpath or not nuchannel:
        # inpath = 'input/datasets/B20180215_100m_bins.h5'
        # nuchannel = '1'
        print('parameters required. try again.')
        sys.exit()
    
    converth52map(inpath, nuchannel)

