import sys
import numpy as np
from astropy.io import fits
from copy import deepcopy

def loadfits(namefile):

    hdus=fits.open(namefile)
    if (isinstance(hdus,list)):
        hdu=hdus[0]
    else:
        hdu=hdus
    datacube = hdu.data
    hdr = hdu.header
    
    return datacube, hdr

def trimhead(hdr1,DitchCRVAL3=True,Inplace=True):

    if Inplace:
        dumhdr1=hdr1
    else:
        dumhdr1=deepcopy(hdr1)

    dumhdr1.pop('NAXIS3', None)  
    dumhdr1.pop('NAXIS4', None)  
    dumhdr1['NAXIS']=2

    dumhdr1.pop('PC3_1', None)  
    dumhdr1.pop('PC4_1', None)  
    dumhdr1.pop('PC3_2', None)  
    dumhdr1.pop('PC4_2', None)  
    dumhdr1.pop('PC1_3', None)  
    dumhdr1.pop('PC2_3', None)  
    dumhdr1.pop('PC3_3', None)  
    dumhdr1.pop('PC4_3', None)  
    dumhdr1.pop('PC1_4', None)  
    dumhdr1.pop('PC2_4', None)  
    dumhdr1.pop('PC3_4', None)  
    dumhdr1.pop('PC4_4', None)
    dumhdr1.pop('PC03_01', None)
    dumhdr1.pop('PC04_01', None)
    dumhdr1.pop('PC03_02', None)
    dumhdr1.pop('PC04_02', None)
    dumhdr1.pop('PC01_03', None)
    dumhdr1.pop('PC02_03', None)
    dumhdr1.pop('PC03_03', None)
    dumhdr1.pop('PC04_03', None)
    dumhdr1.pop('PC01_04', None)
    dumhdr1.pop('PC02_04', None)
    dumhdr1.pop('PC03_04', None)
    dumhdr1.pop('PC04_04', None)
    
    if (DitchCRVAL3):
        dumhdr1.pop('CTYPE3', None) 
        dumhdr1.pop('CRVAL3', None) 
        dumhdr1.pop('CDELT3', None) 
        dumhdr1.pop('CRPIX3', None) 
        dumhdr1.pop('CUNIT3', None)
    
    dumhdr1.pop('CTYPE4', None) 
    dumhdr1.pop('CRVAL4', None) 
    dumhdr1.pop('CDELT4', None) 
    dumhdr1.pop('CRPIX4', None) 
    dumhdr1.pop('CUNIT4', None) 
    dumhdr1.pop('OBJECT', None)
    dumhdr1.pop('PC01_01', None)
    dumhdr1.pop('PC02_01', None)
    dumhdr1.pop('PC01_02', None)
    dumhdr1.pop('PC02_02', None)
    dumhdr1.pop('HISTORY', None)
    dumhdr1.pop('COMMENT', None)
    dumhdr1.pop('CROTA3', None)
    dumhdr1.pop('CROTA4', None)
    dumhdr1.pop('', None) 
    dumhdr1.pop('TELESCOP', None) 
    dumhdr1.pop('LONPOLE', None) 
    dumhdr1.pop('LATPOLE', None) 

    return dumhdr1

def slice0(indata,fileout=False,DitchCRVAL3=True,ReturnHDUList=False):
    if isinstance(indata,str):
        filename=indata
        dcube1, hdr1 = loadfits(filename)
    else:
        if (isinstance(indata,fits.hdu.image.PrimaryHDU)):
            hdu=indata
        elif (isinstance(indata,fits.hdu.hdulist.HDUList)):
            hdu=indata[0]

        dcube1 = hdu.data
        hdr1 = hdu.header

    hdr1=trimhead(hdr1,DitchCRVAL3=DitchCRVAL3)
 

    if (len(dcube1.shape) > 3):
        im1=dcube1[0,0,:,:]
    elif (len(dcube1.shape) > 2):
        im1=dcube1[0,:,:]
    else:
        im1=dcube1

    im1=np.nan_to_num(im1)

    if (isinstance(fileout,str)):
        fits.writeto(fileout,im1, hdr1, overwrite=True)

    hdu = fits.PrimaryHDU()
    hdu.data = im1
    hdu.header = hdr1
    if ReturnHDUList:
        hdu = fits.HDUList([hdu])
        
    return hdu


