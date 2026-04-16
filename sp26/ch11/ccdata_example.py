infile = open("ccdata.txt", "r")
outfile = open("emissiondata.txt", "w")

aline = infile.readline()
# outfile.write("Year \tEmmision\n")
while aline:
    if len(aline.strip()) != 0:
        items = aline.strip().split(",")
        dataline = items[0] + '\t' + items[1]
        outfile.write(dataline + '\n')
    aline = infile.readline()

infile.close()
outfile.close()
