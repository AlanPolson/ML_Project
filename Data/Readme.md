As far as possible, lets try to connect data restfully, to aid reproducability.

The code to read the data restfully can be seen in the restful data read notebook in the code folder.

There is a commented out code block in that notebook that downloads the data and reads it in locally.

For development, we can use data locally, and house our data in this folder, so that the code does not have to be altered.

But the code block that reads-in the data to the variable can be done in a cell that will be commented out finally. 

The .gitignore file instructs git not to track any changes in this folder, so you can add your data here and 'git add --all' without worry.
