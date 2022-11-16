### Import packages

import pandas as pd

### Set display options to not overload computer

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

### Read files: Use thee proteinGroups.txt file

df_MQ = pd.read_csv('proteinGroups_GN.txt', "\t")

### What columns to analyse : this will make riBAQ for the samples you define

column_list = ['iBAQ', 'iBAQ R1', 'iBAQ R2', 'iBAQ R3','iBAQ SR1', 'iBAQ SR2', 'iBAQ SR3', 'iBAQ SH1', 'iBAQ SH2', 'iBAQ SH3','iBAQ H1', 'iBAQ H2','iBAQ H3']

### function to remove reverse hits and contaminants along with making relative abundance

def filtandribaq():
    #Removes rev
    df_filt_REV = df_MQ[(df_MQ['Protein IDs'].str.contains('REV__') == False)]

    df_filt_REV_CON = df_filt_REV[(df_filt_REV['Protein IDs'].str.contains('CON__') == False)]

    df_filt_REV_CON_WP = df_filt_REV_CON[df_filt_REV_CON["Fasta headers"].str.contains('WP_')==False]
    ##############
    count = 0
    for header in column_list:
        count += 1
        summed = []  # list with all the values
        ribaq1 = df_filt_REV_CON_WP[header]  # the column we iterate through
        sumribaq1 = sum(ribaq1)  # the variable with the sum

        ########3#

        for iBAQ in ribaq1:
            summed.append(iBAQ / sumribaq1 * 100)
            column_values = pd.Series(summed)
            # print(column_values)
            new_word = header[:0] + "ri" + header[1:]

        df_filt_REV_CON_WP.insert(loc=50 + count, column=new_word, value=column_values)

### output file:
    df_filt_REV_CON_WP.to_csv('protein_Groups_RCI.txt', "\t", index=False)  # REV CONTAMINANTS iBAQ


filtandribaq()

