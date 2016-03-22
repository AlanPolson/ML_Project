This Folder is intentionally left blank, to aid faster updates, and to ensure data is fetched from the source. This will aid *reproducibility* and *fast backups*.

To this end, we have written [code](../Code/DataDL.py) which can be utilized [in this way](../Code/Restful_Data_Read.ipynb).

The code downloads the data to this data folder.

The [.gitignore file](../.gitignore) tells git to not update anything from the data folder.

The code and the gitignore file accomplish two things:

1) Reproducible work (we all have the same path in our notebooks, and the same data from the same source)

2) we can 'git add --all' without worry.
