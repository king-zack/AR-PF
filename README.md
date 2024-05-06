# AR-PF

UCONN IAC Power Factor Calculator
Written by -- Zachary King

This program is meant to automate the analysis of power factor analysis. An input CSV file is given as well as the rate per kVAR.
Its purpose was to make power factor analysis trivial, saving time and labor.

Pandas is the primary driving library behind this program. It allows for easy and efficient data manipulation as well as built in
functions for managing csv files.

For the final version of this program, matplotlib will be used to create grapics at every step in an effort to better visualize
the data processed.

How to Use:

The repository contains two additional csv files to the program. The PowerData.csv file must be edited. Opening the file in excel
shows three columns: Month, Power Factor, and Real Power. For each month, write the power factor (found on the bill) in the power
factor column and the power measured in kW in the Real Power column. Please note that if the power is denoted in kVAR. The
conversion to kW is:

kW = kVAR * PF

An additional note, any length of column will work for the program.

Upon running the program, the csv will be displayed. Please review these values and press ENTER to confirm.

Once the input csv values are confirmed, the program will ask for a kVAR rate. in USD. Please enter this number as a float value
(28.33, 17.12) etc. additional characters may cause an error in the program.

Once these numbers are submitted, the program will write its output to the PFSavings.csv file. This file can then be opened in 
excel for simple cost analysis

If bugs occur, contact: zachary.n.king@uconn.edu
This program is written under the GPL licence: Any modification to this code for commercial purposes or otherwise is permitted.
