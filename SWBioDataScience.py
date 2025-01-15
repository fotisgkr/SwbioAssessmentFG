#IMPORTANT: Ensure the following libraries are installed prior to running the code
import pandas as pd
import numpy as np
import scipy.stats as stats
import pingouin as pg


#access dataset from github repository
TEM2024github = XXX
data = pd.read_csv(TEM2024github")

#First look into the setup of the dataset. 
print("The Dataset:\n")
print(data.head())

#summary of dataset
print("\nSummary:\n")
print(data.info())
#All replicates from the 3 treatments are in one table as that is the processing output.

#check for missing values in dataset
print("\nMissing values Check\n")
print(data.isnull().sum())

#If all looks good, moving to calculating interaction ratios for individual points

data['Total'] = (data['Interaction'] + data['NoInteraction']) # Calculating the sum of points (interactions and no interactions)
data['Interaction_Ratio'] = (data['Interaction'] / data['Total'])# Calculating th interaction ratio, as a proportion of the total

print("\nInteraction Ratios:\n")
print(data)

#At this point it is obvious there would be lot of 0 values which would massively skew the data. 
#Grouping into sums would prevent this while keeping the data representative

#grouping data by treatment
grouped = data.groupby('Sample').agg(
    {'Interaction': 'sum', 'NoInteraction': 'sum'}
)

# Calculate the interaction ratios for the groups
grouped['Ratio'] = grouped['Interaction'] / (grouped['Interaction'] + grouped['NoInteraction'])


# New column with the treatment (A, B, C) and the repeat number (1, 2, 3) 
grouped['Treatment'] = grouped.index.str[0]  # Finding Treatment 
grouped['Repeat'] = grouped.index.str[1].astype(int)  # Finding repeat

# Table 
pivoted = grouped.pivot(index='Repeat', columns='Treatment', values='Ratio')

print("\nSum of Interaction Ratios\n")
print(pivoted)

#Assuming unequal variance, running a non-parametric Welch's ANOVA test
grouped_data = [grouped[grouped['Treatment'] == Treatment]['Ratio'] for Treatment in ['A', 'B', 'C']]

anova_data = grouped[['Treatment', 'Ratio']].reset_index()

#Welch's ANOVA using pingouin
welch_anova = pg.welch_anova(dv='Ratio', between='Treatment', data=anova_data)

# Output Welch's ANOVA results
print("\nWelch's ANOVA Results:\n")
print(welch_anova)