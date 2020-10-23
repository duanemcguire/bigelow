import csv
with open('organs.csv') as csvfile:
    myreader = csv.reader(csvfile)
    for row in myreader:
        if row[0] > "":
            f = open(str(row[0]) + '-specs.md','w')
            f.write('---\n')
            f.write("opus: " + row[0] + "\n")
            f.write("year: " + row[1] + "\n")
            f.write("# owner is a comma separated list for multiple row display" + "\n")
            f.write("owner: [" + row[2] + "]" + "\n")
            f.write("location: " + row[3] + "\n")
            f.write("manuals: " + row[4]  + "\n")
            f.write("voices: " + row[5] + "\n")
            f.write("ranks: " + row[6] + "\n")
            f.write('---\n')
            f.close
