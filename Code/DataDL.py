import urllib2, cStringIO, zipfile
def download_source(url,pth="", zp=False):
    """
    Download data from source url to an adjacent 'Data' Folder.
    
    Args:
        
        url: (required) url from where data can be downloaded. can be zip archive or a single file.
        
        pth: (Default="") Path of directories within Data where files should be deposited.
        
        zp: (Default = False) Accepts True or False. indicates if file is Zip archve or not.
        Leave blank if you want the zipfiles to be downloaded zipped.
    
    Returns:
        
        Fie Path or List of file paths (for zip archives)
    
    Raises:
        
        'Unable to access zipfile' if url is wrong. Defaut python exeptions otherwise.
    
    
    Eg:
        The following command should download the 2013 NY Houshold PUM data 
        and its documentation into a folder named 'trial' in your data folder.
        
        url = "http://www2.census.gov/acs2013_1yr/pums/csv_hny.zip"
        files=download_source(url,pth="trial/",zp=True)

    """
    __author__='amp'
    path="../Data/"+pth
    files=[]
    if zp==True:
        try:
            remotezip = urllib2.urlopen(url)
            zipinmemory = cStringIO.StringIO(remotezip.read())
            zip = zipfile.ZipFile(zipinmemory)
            for fn in zip.namelist():
                fil=zip.extract(fn,path)
                files.append(fil)
            return files
        except urllib2.HTTPError:
            print "Unable to access zipfile"

    else:
        fil = path+url.split("/")[-1]
        response = urllib2.urlopen(url)
        with open(fil, 'w') as f: 
            f.write(response.read())
        return fil