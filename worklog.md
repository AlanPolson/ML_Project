# Predicting Internet access percentage on the block group level with ACS
**Work log**

## Data Aquisition
All data is collected through [official ACS website](https://www.census.gov/programs-surveys/acs/data/summary-file.2013.html)

#### 1. Download data
As we are interested in internet connections and block group level, we have to interpolate two summary datasets: 
- [2013 1 year ACS Summary table for all states](http://www2.census.gov/programs-surveys/acs/summary_file/2013/data/1_year_entire_sf/)
- [2013 5 years ACS Summary table for NY, tracts and block groups (as we are going to predict for NY only in this case)](http://www2.census.gov/programs-surveys/acs/summary_file/2013/data/5_year_by_state/)

All data is coded into Series of ANSWERS, one file per series per state, and series belongs to different questions/answers for 1y and 5y estimates. Therefore, we need to download lookup tabels:
- [2013 5Y lookup](http://www2.census.gov/programs-surveys/acs/summary_file/2013/documentation/user_tools/ACS_5yr_Seq_Table_Number_Lookup.txt)
- [2013 1Y lookup](ACS_1yr_Seq_Table_Number_Lookup.txt)

We can also download geographical lookup tables (each geounit described in each table with LOGRECNO column):
- [Geographical lookup tables](http://www2.census.gov/programs-surveys/acs/summary_file/2013/documentation/geography/)

#### 2. Join the datasets

- Join all 1 year summary files and drop every row but ones for PUMAS
- Join all 5 year summary files and drop every row but ones for Block Groups

#### 3. Data massage

At this point we have numerous of series, but we need to understand what are we predictiong and what features do we use

- Aggregate questions from two lookup tables. Save list of questuins that are in pumas, but not on the block level(ones we can predict).
- Filtering both datasets by our interconnection table, throwing away features with less than 50% cells filled and technical ones (impute flags, sample flags), split data into train (65%) and test (35%) parts (label column) both for predictors and dependent variables. 

#### 4. Machine learning

As we defined, we are trying 4 different models, training them on the training dataset, and then benchmark their accuracy using R2 measurement on the Test part.
Our models are:

- Random forest regression
- NeyroNetworks
- SVN regression
- Elastic Net


#### 5. Geographies

Now we need to attach our predicted values to each block level boundary in New York State
- get 2013 block group boundaries shapefiles [here](https://www.census.gov/geo/maps-data/data/cbf/cbf_blkgrp.html)
- or [here](https://www.census.gov/geo/maps-data/data/tiger-line.html)
- and take geographical documentation for New York [here](http://www2.census.gov/programs-surveys/acs/summary_file/2013/documentation/geography/)
- using documentation excel file as a bridge, and replacing '15000US' with '1500000US', we were able to merge data with geoBoundaries in  `5_Mapping_Predictions.ipynb`, which filters groups by Land Area > Water Area, and saves predictions as a geojson file

