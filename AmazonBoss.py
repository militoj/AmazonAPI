infile = open("source_file.csv", "r")
outfile = open("amazon_output.csv", "w")

#To preserve headers
aline = infile.readline()
items = aline.split(",")
dataline = items[0] + "," + items[1] + "," + items[2]
outfile.write(dataline + "\n")
aline = infile.readline()

while aline:
    items = aline.split(",")
    dataline = items[0] + "," + items[1] + "," + "$" + items[2]
    outfile.write(dataline +"\n")
    aline = infile.readline()

infile.close()
