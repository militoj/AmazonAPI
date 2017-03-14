infile = open("source_file.csv", "r")
outfile = open("amazon_output.csv", "w")

# stackoverflow article about python RESTful APIs here:
# http://stackoverflow.com/questions/17301938/making-a-request-to-a-restful-api-using-python

# amazon product API doc
# http://docs.aws.amazon.com/AWSECommerceService/latest/DG/CHAP_MakingRequestsandUnderstandingResponses.html


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
