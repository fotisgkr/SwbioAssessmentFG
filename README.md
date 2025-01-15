# SwbioAssessmentFG
 
Analysing ER-Mitochondrial Membrane Contact Sites (MERC) Transmission Electron Micrograph (TEM) data 

The Experimental Design

Mammalian cells were grown in 3 different categories (A,B,C), each with 3 biological repeats (1,2,3)
TEMs were collecetd by random uniform sampling
TEMSs were processed in FIJI (ImageJ), where a grid was placed over each image.
A point was drawn when the grid lines crossed over a mitochondrial membrane, and specifically marked if that point was a MERC (<15nm distance between ER and mitochondrion)
Data extracted all in one file

The Dataset
Consists of 9 categories (treatments A,B,C each with a biological repeat. e.g. A1,A2 etc.)
A: Normal control
B: Cells grown in galactose media (Control for C)
C: Cells grown in galactose media + addition of Antimycin A (Induces H2O2 generation at mitochondria)

Each row represent an image. NoInteraction are the points where the FIJI gridlines crossed a mitochondrial membrane, and Interaction are the points where gridlines crossed through a MERC
the proportion of interaction points to the total number of points represents the proportion of the mitochondrial membrane in contact with the ER in a sample

This script extracts data from the master file and groups them into repeats of treatments. it can be used even if the samples are out of order or codenamed in cases of wanting to remove bias. After summing up the interactions, nointeractions, it calculates the ratio of interactions:total and performs a Wilch's ANOVA (assuming unequal variance) to identify significant difference.

This code requires the following modules:

pandas
numpy
scipy.stats
pingouin

TO RUN:

Simply run the code, and the program will fetch the datset from this directory
