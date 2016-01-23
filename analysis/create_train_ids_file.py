TRAIN_IDS_PATH = "/home/jier/Documents/Leren/ThemaIII/ClusterAnalysis/WEBDA data/train_data.npy"

#TODO create csv file 
TRAIN_LABELS_PATH = ""

import numpy as np
import os
import csv

with open(TRAIN_LABELS_PATH,'r') as f:
    reader = csv.reader(f, delimiter=",")
    train_ids=[]
    for i,line in enumerate(reader):
        if i == 0: continue #skip header
        train_ids.append(int(line[0]))
        
train_ids = np.array(train_ids)
print "Saving %s" + str(TRAIN_IDS_PATH)
np.save(TRAIN_IDS_PATH,train_ids)