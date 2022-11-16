# Scripts-for-data-science
Small scripts to handle proteomics data from MaxQuant (https://www.maxquant.org/)
Uses packages such as Pandas, numpy and matplotlib

# Intial idea
The idea about the scripts are to remove most data handling of data in Excel, notepad etc. For reproducible science all code for graphs, tables and how data is transformed must be stored. 
This will also make sample to sample handling faster and will by time be made into an automatic workflow for handling several MS-samples for proteomics. 

# Automated workflow
The plan is to make an automated workflow where you can input Maxquant file (proteinGroups.txt) and have an filtered output of tables, figures etc. for fast analysis that can be used for articles. 

### 1_maxquant_cleaner.py

Script that handles removing contaminants and reverse hits. It also makes the initial iBAQ data to relative iBAQ (riBAQ). 

### 2_data_filtering.py

Filters the data based on Score > 40 and Unique peptides >=2. Note that this will remove a significant amount of protein candidates, but increase the chance of having a valid protein candidate. Through the initial data analysis a tendency has shown that protein candidates with low Score (<40) are periplasmic proteins which can be difficult to extract and isolate even with harsh detergents. 

The filtered overview will be made to a csv called "filt.csv". 

### Dataframe to Latex 

Takes any dataframe and makes it to a latex file for use in Latex based programs such as Overleaf 

