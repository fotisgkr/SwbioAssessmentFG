# SwbioAssessmentFG
 
Analysing ER-Mitochondrial Membrane Contact Sites (MERC) Transmission Electron Micrograph (TEM) data 

The Experimental Design

Mammalian cells were grown in 3 different categories (A,B,C), each with 3 biological repeats (1,2,3)
TEMs were collecetd by random uniform sampling
TEMSs were processed in FIJI (ImageJ), where a grid was placed over each image.
A point was drawn when the grid lines crossed over a mitochondrial membrane, and specifically marked if that point was a MERC (<15nm distance between ER and mitochondrion)
Data extracted all in one file

The Dataset
Consists of 9 categories (treatments A,B,C each with a biological repeat. e.g. A1,A2 etc.). more information about the setup can be found in the report and is ommited here for privacy.

Each row represent an image. NoInteraction are the points where the FIJI gridlines crossed a mitochondrial membrane, and Interaction are the points where gridlines crossed through a MERC
the proportion of interaction points to the total number of points represents the proportion of the mitochondrial membrane in contact with the ER in a sample

This script extracts data from the master file and groups them into repeats of treatments. it can be used even if the samples are out of order or codenamed in cases of wanting to remove bias. After summing up the interactions, nointeractions, it calculates the ratio of interactions:total and performs a Wilch's ANOVA (assuming unequal variance) to identify significant difference. The script will first generate information about the dataset to ensure it is looking ok. It will then add another collumn to the data showing the interaction ratio (interaction/(interaction+nointeraction)). Then it will sum up the data and calculate the overll ratios wchich will be presented in a table. Finally the Wilch's test output will also be visible.

This code requires the following modules:

pandas,
numpy,
scipy.stats,
pingouin,

TO RUN:

After downloading the required modules, simply run the code, and the program will fetch the datset from this directory and run
This project was developed with assistance from ChatGPT by OpenAI for coding guidance
