import os
import fileinput
import pathlib
from pathlib import Path
import csv

#filepath = r"C:\Users\Erick.Ellis\Dropbox (The Trade Desk)\Enterprise Team Files\Projects\VIQ\2018-05-29\TTD- IQD Sample.csv"
filepath = r"C:\Users\Erick\Dropbox (The Trade Desk)\Enterprise Team Files\Projects\VIQ\2018-05-29\TTD- IQD Sample.csv"
newHeaders = ["DATE","TDID","IMPRESSION_ID","PARTNER_ID","CONVERSION_TYPE","TRUE_CONVERSIONS"]

try:
    my_abs_path = os.path.abspath(filepath)
except FileNotFoundError:
    print("Source file " + filepath + " does not exist.")
else:
    if not os.path.isfile(my_abs_path):
        print("Source file " + my_abs_path + " not a file.")
    else:
        my_abs_dir = os.path.dirname(my_abs_path)
        print("source " + my_abs_path)
        print("source dir " + my_abs_dir)

        # make new directory for output
        # undone

        with open(my_abs_path, 'r') as infile:
            reader = csv.reader(infile ,delimiter='$')
            
            # skip the headers
            next(reader)

            with open(os.path.join(my_abs_dir,"out.txt"),'w+') as outfile:
                outfile.write(','.join(newHeaders) + '\n')
            
                for row in reader:
                    existingfields=row[0].split(",")
                    
                    parsefield = existingfields[1].split("|")
                    TDID = parsefield[0]
                    IMPRESSIONID = parsefield[1]
                    PARTNERID = parsefield[2]

                    newfields = [ 
                        existingfields[0], 
                        TDID, 
                        IMPRESSIONID, 
                        PARTNERID,
                        existingfields[2], 
                        existingfields[3]
                        ]

                    outfile.write(','.join(newfields) + '\n')

                
           

       
            
            
""" DATE,IMPRESSION_ID,CONVERSION_TYPE,TRUE_CONVERSIONS
5/24/2018,123e4567-e89b-12d3-a456-426655440000|123e4567-e89b-12d3-a456-426655440001|xjagv9i,KPI Type 1,10.25
5/24/2018,123e4567-e89b-12d3-a456-426655440000|123e4567-e89b-12d3-a456-426655440001|xjagv9i,KPI Type 2,5.75
5/24/2018,123e4567-e89b-12d3-a456-426655440000|123e4567-e89b-12d3-a456-426655440001|xjagv9i,KPI Type 3,30.45 """