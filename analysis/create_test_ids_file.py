TEST_IDS_PATH = "/home/jier/Documents/Leren/ThemaIII/ClusterAnalysis/WEBDA data/test_data.npy"


import numpy as np
import glob
import os

filenames = glob.glob("/home/jier/Documents/Leren/ThemaIII/ClusterAnalysis/WEBDA data/test_data/*.png")
#TODO use regex to fix basename
test_ids = [int(os.path.basename(s).replace(".png","")) for s in filenames]
test_ids.sort()
test_ids = np.array(test_ids)
print "Saving %s" +str(TEST_IDS_PATH)
np.save(TEST_IDS_PATH,test_ids)