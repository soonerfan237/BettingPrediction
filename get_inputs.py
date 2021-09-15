import csv

def get_bettinglines():
    bettinglines = []
    with open('nfl_bettinglines.csv', newline='') as csvfile:
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