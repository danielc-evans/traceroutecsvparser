# TRACEROUTE TEXT LOG TO CSV PARSER PROGRAM

# CHANGE IN_FILE LINE PARAMETERS TO THE OUTPUT TXT FILE

# CHANGE OUT_FILE LINE PARAMETERS TO CHOSEN CSV FILE NAME

import csv

with open('log.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('log.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Hop Number', 'Domain', 'IP Address', 'Round-Trip-Time 1', 'Round-Trip-Time 2' 'Round-Trip-Time 3'))
        writer.writerows(lines)
