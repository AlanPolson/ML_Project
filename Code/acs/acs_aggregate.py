#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import pandas as pd
import sys
import zipfile


def getFiles(folder, format, full=True, filtr=None):
    for f in os.listdir(folder):
        if f.endswith(format):
            if filtr is None or filtr not in f:
                if full:
                    yield os.path.join(folder, f)
                else:
                    yield f


def estimates(f):
    return 'e' + f.replace('.zip', '.txt')

cols = [
    'FILEID',
    'FILETYPE',
    'STUSAB',
    'CHARITER',
    'SEQUENCE',
    'LOGRECNO',
]


def getTable(fname, cols=cols, logFilter=None):
	'''
	get table and parse it
	cols = column default names
	logfilter - LOGRECNO id's to keep, if none - does not filter
	'''
	zf = zipfile.ZipFile(fname)
	df = pd.read_csv(zf.open(estimates(fname.split('/')[-1])),
    				 header=None, low_memory=False)

	seq = df.iloc[1, 4]  # sequence id

	df.columns = cols + ['%d_%d' % (seq, i + 1)
						 for i in xrange(df.shape[1] - 6)]

	if logFilter:  # filter by logreno id
		df = df[df.LOGRECNO.isin(logFilter)]

	return df.iloc[:, 5:].set_index('LOGRECNO')


def aggTables(folder, lf):
	'''
	aggregate all tables in folder
	'''
	tables = (getTable(f, logfilter=lf) for f in getFiles(folder, '.zip'))
	return pd.concat(tables, 1)


def main(path, fpath=None):
	
    aggTables(path, lf)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
