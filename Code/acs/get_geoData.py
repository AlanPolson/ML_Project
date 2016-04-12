#!/usr/bin/env python
#-*- coding: utf-8 -*-
import pandas as pd
import glob
import sys

# PUMA : gh 795
# Census Block: gh ...


def getData(folder, gf):
	allFiles = glob.glob(folder + "/*.csv")
	return pd.concat((read_filter(x, gf=gf) for x in allFiles))


def read_filter(file_, gf=795):
	df = pd.read_csv(file_, anyindex_col=None, header=None)
	return df.loc[df[2] == gf]  # only specific geographical level


def main(path, gf, outpath=None):
	'''
	saves table of particular geogrpaphical units from ACS
	path = folder with general data
	gf = geographical level (type) code
	oputpath (optional) = place to save data. if None,
	saves in the root under 'gf.csv'
	'''
	df = getData(path, gf)
	if not outpath:
		outpath = '%d.csv' % gf

	df.to_csv(outpath)
	print 'Saved data to:\n%s' % outpath

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2], sys.argv[3])
