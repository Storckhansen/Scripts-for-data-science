def enzymefinder(df, enzyme_name, column, low, high):   #in its simplicity can be used to find any keyword
    locate =(
        df[df['Fasta headers'].str.contains(enzyme_name)==True]
        .sort_values(by=[column], ascending=False)
        .loc[(low <= df[column]) & (df[column] <= high)]
            )
    return locate