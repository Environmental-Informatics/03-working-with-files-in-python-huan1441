# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Name: ABE65100 Lab03 Evaluate_Raccoon_Life.py
#
# Purpose: Script to read the data file 2008Male00006.txt, process the data,
#          and create a new output file called "Georges_life.txt".
#
# Author: Tao Huang (huan1441)
#
# Created: Jan 31, 2020
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import math

# Function to compute the mean of a list

def list_mean(ls):

    listmean = list_sum(ls)/len(ls)

    return listmean
    

# Function to compute the cumulative sum of a list

def list_sum(ls):

    listsum = 0

    for i in range(len(ls)):
        listsum = listsum + float(ls[i])

    return listsum

# Function to compute the the distance between two points provided as two lists

def list_dis(ls1,ls2):

    # create 1-D array for diatances with initial value -- 0
    
    listdis=[0]*len(ls1)

    for i in range(1,len(ls1)):
        ls1[i] = float(ls1[i])
        ls1[i-1] = float(ls1[i-1])
        ls2[i] = float(ls2[i])
        ls2[i-1] = float(ls2[i-1])

        # compute the distance between two points

        listdis[i] = math.sqrt((ls1[i]-ls1[i-1])**2+(ls2[i]-ls2[i-1])**2)

    return listdis


# # # open the data file "2008Male00006.txt" in the same driectory as the script

fo = open("2008Male00006.txt", "r")
lines = fo.readlines()

# close the file

fo.close()

n=len(lines)

# store the first line of the original data as Headers

Headers = lines[0].strip().split(",")

# creat a list -- Data to store the content of the original data

Data=[]
for line in lines[1:n]:
    if line.find(",") != -1:
        Data.append([n for n in line.strip().split(",")])

    # store the line without comma as the Status

    else:
        Status = line.strip()

# create a dictionary to store the Headers (key) and Data (list of values)

Data_dic = {}
for i in range(len(Headers)):
    Data_dic[Headers[i].strip()] = [row[i] for row in Data]

# create a list to store the distances and add it to the dictionary -- Data_dic

Distance = {}
Distance['Distance'] = list_dis(Data_dic['X'],Data_dic['Y'])
Data_dic = dict(Data_dic, **Distance)

# # # create a new output file called "Georges_life.txt"

fw = open("Georges_life.txt", "w")

# create a header block for the output file

raccoon_name = Headers[3]+Data_dic[Headers[3]][0]
x_ave = str(list_mean(Data_dic['X']))
y_ave = str(list_mean(Data_dic['Y']))
sum_dis = str(list_sum(Data_dic['Distance']))
ave_Engergy = str(list_mean(Data_dic['Energy Level']))

New_Headers = ["Raccoon name: "+ raccoon_name + "\n"
               "Average location: "+ x_ave + ", "+ y_ave + "\n"
               "Distance traveled: "+ sum_dis + "\n"
               "Average energy level: " + ave_Engergy+"\n"
               "Raccoon end state: "+ Status + "\n"]

# store the labels of the select contents with TAB delimited

New_Data_label = ["Date\tTime\tX\tY\tAsleep Flag\tBehavior Mode\tDistance Traveled\n"]


# store the select contents of data dictionary with TAB delimited

New_Data=[]
for i in range(len(Data)):
    New_Data.append(Data_dic['Day'][i] + "\t" + Data_dic['Time'][i] + "\t" +
                    str(Data_dic['X'][i]) + "\t" + str(Data_dic['Y'][i]) +
                    "\t" + Data_dic['Asleep'][i] + "\t"+ Data_dic['Behavior Mode'][i]
                    + "\t" + str(Data_dic['Distance'][i]) + "\n")

# write the labels of the select contents    

fw.writelines(New_Headers)

# create a blank line between the header block and the next data section

fw.writelines("\n")

# write the labels of the select contents

fw.writelines(New_Data_label)

# write the select contents of data dictionary

fw.writelines(New_Data)

# close the file

fw.close()
