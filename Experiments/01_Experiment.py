# 01_Experiment.py
# Bree Cummins and Shaun Harker
# MIT LICENSE
# 2017-02-03 

from QueryExperiments import *

dbfile = "01_Experiment.db"
savefilename="01_Experiment.json"
gene = "S"
FP_OFF={"E2F":[0,0],"E2F_Rb":[1,1]} 
FP_ON={"E2F":[1,8],"E2F_Rb":[0,0]}
database = DSGRN.Database(dbfile)
QueryExperiment(database, gene, FP_OFF, FP_ON, savefilename)

