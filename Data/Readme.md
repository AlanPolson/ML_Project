As far as possible, lets try to connect data restfully, to aid reproducability.
The code to read the data restfully can be seen in the restful data read notebook in the code folder.
there is a commented out code block in that notebook that downloads the data and reads it in locally.
For development, we can use data locally, and house our data in this folder, so that the code does not have to be altered.
but the code block that reads-in the data to the variable can be done in a cell that will be commented out finally. 
I am also going to add a .gitignore file to this folder, so hopefully git will not add any new files in it.
