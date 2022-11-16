rom Bio import SeqIO
import pandas as pd
import numpy as np

### import data from previous step

ms_data = pd.read_csv("protein_Groups_RCI.txt", "\t")

### Depends on what you look for. For my master thesis I looked at these.


overview = ms_data [['Fasta headers', 'Gene names', 'Unique peptides', 'Sequence coverage [%]', 'Unique sequence coverage [%]', 'Mol. weight [kDa]', 'Score', 'rBAQ', 'rBAQ R1', 'rBAQ R2','rBAQ R3', 'rBAQ SH1', 'rBAQ SH2', 'rBAQ SH3', 'rBAQ SR1', 'rBAQ SR2','rBAQ SR3','rBAQ H1', 'rBAQ H2','rBAQ H3']]

### finding mean and standard deviation

R = overview.loc[:, "rBAQ R1":"rBAQ R3"]
overview ['riBAQ R mean'] = R.mean(axis=1)
overview ['riBAQ R std'] = R.std(axis=1)

SR = overview.loc[:, "rBAQ SR1":"rBAQ SR3"]
overview ['riBAQ SR mean'] = SR.mean(axis=1)
overview ['riBAQ SR std'] = SR.std(axis=1)

S= overview.loc[:, "rBAQ SH1":"rBAQ SH3"]
overview ['riBAQ SH mean'] = S.mean(axis=1)
overview ['riBAQ SH std'] = S.std(axis=1)

H= overview.loc[:, "rBAQ H1":"rBAQ H3"]
overview ['riBAQ H mean'] = H.mean(axis=1)
overview ['riBAQ H std'] = H.std(axis=1)

### filtering for Score > 40 and Unique pptides >=2

filtered_overview = (
     overview[['Fasta headers', 'Gene names','Unique peptides', 'Sequence coverage [%]', 'Unique sequence coverage [%]', 'Mol. weight [kDa]', 'Score', 'rBAQ', 'riBAQ R mean', 'riBAQ R std', 'riBAQ SH mean', 'riBAQ SH std', 'riBAQ SR mean','riBAQ H mean', 'riBAQ SR std']]
    .loc[overview['Score'] > 40]
    .loc[overview['Unique peptides'] >= 2]
    .round(2)
    .sort_values(by=['rBAQ'], ascending=False)
)


filtered_overview.to_csv('filt.csv', index=False)


def latex_table(df):
    with open(filename, 'w') as tf:  # change filename to something that makes sense to you
        tf.write(df.to_latex(multirow=bool,
                             label=True,  # Makes a label
                             caption=' '  # give a caption
                             , escape=False, index=False,  # removes the pandas index

                             header=['\\rotatebox{67.5}{' + c + '}' for c in
                                     df.columns]))  # rotates headers to they can fit on a page. can be removed


latex_table(df=filtered_overview)

# Look for high abundant and low abundant proteins

#will find the abundant proteins across streams

oneprocent = (
    filtered_overview
    .loc[(filtered_overview['rBAQ'] >= 1) | (filtered_overview['riBAQ SH mean'] >= 1) | (filtered_overview['riBAQ SR mean'] >= 1)]
)




