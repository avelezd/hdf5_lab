#------------------------------------------------------------------------------
# Script name:  gifgenerator.py
# Description:  Set format to frames and creates an animated gif 
# Creation date:30/04/2020
# Last Update:  18/05/2020
# Author:       avelezd
#------------------------------------------------------------------------------
from os import walk, path
from PIL import Image
import imageio

def cropimages(inpath, outpath):
    
    for (dirpath, dirnames, filenames) in walk(inpath):
        for dirname in dirnames:
            path.join(dirpath,dirname)
        for filename in filenames:
            file_path = "%s/%s"%(dirpath,filename)

            im = Image.open(file_path)
    
            # im.crop((left, top, right, bottom))
            region = im.crop((620, 80, 1290, 880))
            region.save("%s/%s"%(outpath,filename))

def animateframes(inpath, outpath, nuchannel, gifname):
    frames = []

    for frameidx in range(0,288):
        frames.append(imageio.imread('%s/%s_%s.png'%(inpath, frameidx, nuchannel)))
    
    imageio.mimsave('%s/%s.gif'%(outpath, gifname), frames)

