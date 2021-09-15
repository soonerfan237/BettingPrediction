import csv
import pandas as pd

def get_bettinglines_df(input_file):
    return pd.read_csv(input_file)

def get_bettinglines(input_file):
    bettinglines = []
    with open(input_file, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for row in csvreader:
            bettinglines.append(
                {
                    'hometeambeatspread': int((float(row[3])-float(row[4]))>float(row[16])),
                    'date': row[0],
                    'hometeam': row[1],
                    'awayteam': row[2],
                    'homemargin': float(row[3])-float(row[4]),
                    'homelineclose': float(row[16])
                }
            )
    return bettinglines[1:]