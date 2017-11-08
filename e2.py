
import requests

# Loop over ELECTION_ID and download the president_general_year.csv.
for line in open("ELECTION_ID"):
    addr = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(line[5:10])
    resp = requests.get(addr)
    file_name = "president_general_{}.csv".format(line[0:4])
    with open(file_name, "w") as out:
        out.write(resp.text)
