
import requests

# Loop over a file using the hint commend
for line in open("ELECTION_ID"):
# Download the csv
    addr = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(line[5:10])
    resp = requests.get(addr)
# Set the format of name groups, it will show up election by election in 4 years 
    file_name = "president_general_{}.csv".format(line[0:4])
    with open(file_name, "w") as out:
        out.write(resp.text)
