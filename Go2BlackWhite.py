import numpy as np
import cv2
import zipfile
from google.colab import files

def BlackWhite(Transfere):
  file_name = zipfile.ZipFile(Transfere, 'r')
  file_name.extractall()
  # all images are load in variable ww...
  FILE=Transfere
  img_name=[]
  xw=[]
  ww=[]

  with zipfile.ZipFile(FILE, "r") as f:
    for name in f.namelist():
      img_name.append(name)
      #xw.append(cv2.imread(name))
      xw.append(cv2.resize(cv2.imread(name),(Size,Size)))

  nrow=len(img_name)
  ncol=Size*Size
  pw=np.zeros((nrow,ncol))
  #pw=[]
  for i in range(nrow):
    ww.append(cv2.cvtColor(np.array(xw[i]), cv2.COLOR_BGR2GRAY))
    pw[i,:]=ww[i].ravel()
  return ww
