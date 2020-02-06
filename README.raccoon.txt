= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 

Name of the script: huan1441_Evaluate_Raccoon_Life.py

Author: Tao Huang (huan1441@purdue.edu), Purdue University

Created: Jan 31, 2020  (Version 1.0,  used in Python 3.6)

Purpose: Script to read and process the data file from a Raccoon behavior model, and create a new output file to show its status.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

The process of the script is as follows: 

1) open and read the data file "2008Male00006.txt" in the same driectory as the script.

2) organize and store the data into a dictionary with the Headers (key) and Data (list of values).

3) compute the basic parameters (mean, sum, distance) based on some lists of numerical data.

4) create a output file called "Georges_life.txt" in the same driectory as the script and write some formatted data into it.

Input (required) file: 2008Male00006.txt

Output (created) file: Georges_life.txt

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 