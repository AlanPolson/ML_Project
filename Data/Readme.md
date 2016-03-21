As far as possible, lets try to connect data *restfully*, to aid reproducability.

The code to read the data restfully can be seen [here](../Code/Restful_Data_Read.ipynb).

For development, we can use data locally, and house our data in this folder, so that the code does not have to be altered.

But the cell with the code block that reads-in the local data can be commented out finally. 

The .gitignore file instructs git not to track any changes in this folder, so you can add your data here and even add the same path to your notebook and 'git add --all' without worry.
