import urllib2, cStringIO, zipfile
def download_restful(url,pth="", zp=False):
    """
    Used to download files directly from source into an adjacent 'Data' Folder.
    pass arguments 'url' (required)
    indicate zp = True for zip file
    if you want to further orgaize your date within the data folder, pass pth="folder_name/" and it will be appended to the path
    The following command should download the NY houshold puma data into a folder named 'trial' in your data folder
    files=download_restful(url,pth="trial/",zp=True)

    Returns file path for single file or list of file paths for zip archive

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
            print "unable to open zipfile"

    else:
        fil = path+url.split("/")[-1]
        response = urllib2.urlopen(url)
        with open(fil, 'w') as f: 
            f.write(response.read())
        return fil