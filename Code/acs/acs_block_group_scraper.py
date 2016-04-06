#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
import os
import StringIO

BASEURL = 'http://www2.census.gov/programs-surveys/acs/summary_file/2013/data/5_year_seq_by_state/{{state}}/Tracts_Block_Groups_Only/'

states = {'NewYork': 'ny'}


def genID(x):
    x = str(x)
    return '0' * (4 - len(x)) + x + '000'


def download_file(url, path):
    local_filename = path + '/' + url.split('/')[-1]

    # NOTE the stream=True parameter
    r = requests.get(url)
    if not r.status_code == requests.codes.ok:
    	print 'download corrupted'
    	print r.status_code
    else:
	    with open(local_filename, 'wb') as f:
			for chunk in r.iter_content(1024):
				f.write(chunk)


def downoadTablesForState(state, path):
    '''download all tables for chosen state'''
    global BASEURL

    path += '/' + state[0]

    if not os.path.exists(path):
        os.makedirs(path)

    url = BASEURL.replace('{{state}}', state[0])

    for x in xrange(1, 123):
        fileUrl = url + '20135%s%s.zip' % (state[1], genID(x))
        print x, '|', fileUrl.split('/')[-1]
    	download_file(fileUrl, path)


def downloadGeoDict(state, path):
	'''download geofile for chosen state'''
	global BASEURL

	path += '/' + state[0]
	if not os.path.exists(path):
		os.makedirs(path)

	fileUrl = BASEURL.replace('{{state}}', state[0]) + 'g20135%s.csv' % state[1]
	print fileUrl.split('/')[-1]
	download_file(fileUrl, path)


def main():
    for state in states.iteritems():
        print state
        # downoadTablesForState(state, '../../Data/ACS/states')
        downloadGeoDict(state, '../../Data/ACS/states')


if __name__ == '__main__':
    main()
