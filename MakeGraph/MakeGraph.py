#%%
from importlib.resources import path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image 
import shutil, sys  

path =  os.getcwd() + "\\Data"
fileList =  os.listdir(path)
fileName = path + "\\" + fileList[0]
fileNameW = path + "\\csm.tmp"

fP = open(fileName, 'r', encoding='utf-8')
fPw = open(fileNameW, 'w', encoding='utf-8')

trigger = False
for line in fP:
    if trigger == False:
        tmpbuf = line.split('\t')
        if (tmpbuf[0] == "Roll") or (tmpbuf[0] == "OutRoll"):
            trigger = True
            fPw.write(line)
    else:
        fPw.write(line)
fP.close()
fPw.close()

data=pd.read_csv(fileNameW, sep="\t")
# data.head()

for col in data.columns.array:
    if (col != "TEST_ON_TIME") and (col != "Roll"):
        #print(col)
        plt.figure(figsize=(50,7))
        plt.ylim([0,5])
        plt.title(label=col)
        plt.margins(x=None,y=None,tight=True)
        plt.plot(data["{}".format(col)][data.index])        
        plt.savefig("tmp.png")
        img = Image.open("tmp.png")
        cropImg = img.crop((590,45,4550,660))
        cropImg.save('Data/{}.png'.format(col))

if os.path.exists("tmp.png"):
    os.remove("tmp.png") 

if os.path.exists("Data/csm.tmp"):
    os.remove("Data/csm.tmp") 

#%%