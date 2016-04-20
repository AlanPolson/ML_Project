import pandas as pd
import glob

# the following code reads in all CSV files in a particular directory and concatenates them into a DataFrame
path = r'/Users/Erwan/Documents/Code/Machine_Learning/project/1Y_geographies/1Y_geographies' # use your path
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=None)
    list_.append(df)
frame = pd.concat(list_)

# subset DataFrame by PUMAS
pumas = frame.loc[frame[2] == 795]

# output DataFrame
pumas.to_csv('pumas_only.csv')