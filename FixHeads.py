import sys
import numpy as np
import os
import os.path
from astropy.io import fits as pf

include_path=os.environ['HOME']+'/common/python/include/'
sys.path.append(include_path)







def fixhead(filename,fileout=False,Verbose=False):
    im1 = pf.open(filename)[0].data
    hdr1 = pf.open(filename)[0].header
    hdr1.pop('CTYPE3'   , None)
    hdr1.pop('CUNIT3'   , None)
    hdr1.pop('CRPIX3'   , None)
    hdr1.pop('CRVAL3'   , None)
    hdr1.pop('CDELT3'   , None)
    hdr1.pop('RESTFREQ' , None)
    hdr1['BMAJ']=50E-3/3600.
    hdr1['BMIN']=50E-3/3600.
    hdr1['BPA']=0.
    im1=np.nan_to_num(im1)
    if (isinstance(fileout,str)):
        if Verbose:
            print(("PUNCH",fileout))
        pf.writeto(fileout,im1, hdr1, overwrite=True)

def fixhead_1(filename,fileout=False,Verbose=False):
    im1 = pf.open(filename)[0].data
    hdr1 = pf.open(filename)[0].header

    
    hdr1.pop(''        , None)
    hdr1.pop('PC3_1'   , None)
    hdr1.pop('PC4_1'   , None)
    hdr1.pop('PC3_2'   , None)
    hdr1.pop('PC4_2'   , None)
    hdr1.pop('PC1_3'   , None)
    hdr1.pop('PC2_3'   , None)
    hdr1.pop('PC3_3'   , None)
    hdr1.pop('PC4_3'   , None)
    hdr1.pop('PC1_4'   , None)
    hdr1.pop('PC2_4'   , None)
    hdr1.pop('PC3_4'   , None)
    hdr1.pop('PC4_4'   , None)
    hdr1.pop('CDELT3'  , None)
    hdr1.pop('CDELT4'  , None)
    hdr1.pop('COMMENT' , None)
    hdr1.pop('DATE'    , None)
    hdr1.pop('ORIGIN'  , None)
    
    im1=np.nan_to_num(im1)
    if (isinstance(fileout,str)):
        if Verbose:
            print(("PUNCH",fileout))
        pf.writeto(fileout,im1, hdr1, overwrite=True)


def fixhead_2(filename,fileout=False,Verbose=False):
    im1 = pf.open(filename)[0].data
    hdr1 = pf.open(filename)[0].header
    hdr1.pop('PC3_1', None)  
    hdr1.pop('PC4_1', None)  
    hdr1.pop('PC3_2', None)  
    hdr1.pop('PC4_2', None)  
    hdr1.pop('PC1_3', None)  
    hdr1.pop('PC2_3', None)  
    hdr1.pop('PC3_3', None)  
    hdr1.pop('PC4_3', None)  
    hdr1.pop('PC1_4', None)  
    hdr1.pop('PC2_4', None)  
    hdr1.pop('PC3_4', None)  
    hdr1.pop('PC4_4', None)
    hdr1.pop('PC03_01', None)
    hdr1.pop('PC04_01', None)
    hdr1.pop('PC03_02', None)
    hdr1.pop('PC04_02', None)
    hdr1.pop('PC01_03', None)
    hdr1.pop('PC02_03', None)
    hdr1.pop('PC03_03', None)
    hdr1.pop('PC04_03', None)
    hdr1.pop('PC01_04', None)
    hdr1.pop('PC02_04', None)
    hdr1.pop('PC03_04', None)
    hdr1.pop('PC04_04', None)
    hdr1.pop('CTYPE3', None) 
    hdr1.pop('CRVAL3', None) 
    hdr1.pop('CDELT3', None) 
    hdr1.pop('CRPIX3', None) 
    hdr1.pop('CUNIT3', None) 
    hdr1.pop('CTYPE4', None) 
    hdr1.pop('CRVAL4', None) 
    hdr1.pop('CDELT4', None) 
    hdr1.pop('CRPIX4', None) 
    hdr1.pop('CUNIT4', None) 
    hdr1.pop('OBJECT', None)
    hdr1.pop('PC01_01', None)
    hdr1.pop('PC02_01', None)
    hdr1.pop('PC01_02', None)
    hdr1.pop('PC02_02', None)
    hdr1.pop('HISTORY', None)
    hdr1.pop('COMMENT', None)
    
    im1=np.nan_to_num(im1)
    if (isinstance(fileout,str)):
        if Verbose:
            print(("PUNCH",fileout))
        pf.writeto(fileout,im1, hdr1, overwrite=True)

    return




def fixhead_3(filename,fileout=False,scale=1.,Verbose=False):
    im1 = pf.open(filename)[0].data
    hdr1 = pf.open(filename)[0].header
    hdr1.pop('PC3_1', None)  
    hdr1.pop('PC4_1', None)  
    hdr1.pop('PC3_2', None)  
    hdr1.pop('PC4_2', None)  
    hdr1.pop('PC1_3', None)  
    hdr1.pop('PC2_3', None)  
    hdr1.pop('PC3_3', None)  
    hdr1.pop('PC4_3', None)  
    hdr1.pop('PC1_4', None)  
    hdr1.pop('PC2_4', None)  
    hdr1.pop('PC3_4', None)  
    hdr1.pop('PC4_4', None)
    hdr1.pop('PC03_01', None)
    hdr1.pop('PC04_01', None)
    hdr1.pop('PC03_02', None)
    hdr1.pop('PC04_02', None)
    hdr1.pop('PC01_03', None)
    hdr1.pop('PC02_03', None)
    hdr1.pop('PC03_03', None)
    hdr1.pop('PC04_03', None)
    hdr1.pop('PC01_04', None)
    hdr1.pop('PC02_04', None)
    hdr1.pop('PC03_04', None)
    hdr1.pop('PC04_04', None)
    hdr1.pop('CTYPE3', None) 
    hdr1.pop('CRVAL3', None) 
    hdr1.pop('CDELT3', None) 
    hdr1.pop('CRPIX3', None) 
    hdr1.pop('CUNIT3', None) 
    hdr1.pop('CTYPE4', None) 
    hdr1.pop('CRVAL4', None) 
    hdr1.pop('CDELT4', None) 
    hdr1.pop('CRPIX4', None) 
    hdr1.pop('CUNIT4', None) 
    hdr1.pop('OBJECT', None)
    hdr1.pop('PC01_01', None)
    hdr1.pop('PC02_01', None)
    hdr1.pop('PC01_02', None)
    hdr1.pop('PC02_02', None)
    hdr1.pop('HISTORY', None)
    hdr1.pop('COMMENT', None)




    hdr1.pop('', None) 
    hdr1.pop('TELESCOP', None) 
    hdr1.pop('LONPOLE', None) 
    hdr1.pop('LATPOLE', None) 




    hdr1.pop('CDELT4' , None) 
    hdr1.pop('CRPIX4' , None) 
    hdr1.pop('CRVAL4' , None) 
    hdr1.pop('CTYPE4' , None) 
    hdr1.pop('CUNIT4' , None) 
    hdr1.pop('NAXIS4' , None) 

    hdr1.pop('PC1_1'  , None) 
    hdr1.pop('PC1_2'  , None) 
    hdr1.pop('PC2_1'  , None) 
    hdr1.pop('PC2_2'  , None) 
    hdr1.pop('ALTRPIX'  , None) 
    hdr1.pop('ALTRVAL'  , None) 
    hdr1.pop('PV2_1'  , None) 
    hdr1.pop('PV2_2'  , None) 
    hdr1.pop('VELREF'  , None) 


    hdr1.pop('OBSDEC' , None) 
    hdr1.pop('OBSRA' , None) 


    hdr1.pop('OBSGEO-X',None) 
    hdr1.pop('OBSGEO-Y',None)
    hdr1.pop('OBSGEO-Z', None)
    

    #for akey in ('BMAJ','BMIN','BPA','CDELT1','CDELT2','CRPIX1','CRPIX2','CRVAL1','CRVAL2','RESTFRQ'):
    #    hdr1[akey] ='%.5e'%(hdr1[akey])


    #import pprint()
    #pprint(.pprint(hdr1, width=1))



    
    im1=np.nan_to_num(im1)
    im1=im1*scale
    if (isinstance(fileout,str)):
        if Verbose:
            print(("PUNCH",fileout))
        pf.writeto(fileout,im1, hdr1, overwrite=True)

    return

