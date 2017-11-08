
from bs4 import BeautifulSoup as bs
import requests

# Find address
addr = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
# set up "soup"
resp = requests.get(addr)
html = resp.content
# save and parse it
soup = bs(html, "html.parser")
# Grab all of the instances
item = soup.find_all("tr", "election_item")

# From each row:
for i in item:
# grap the ids and corresponding years
    y = int(i.find("td", "year first").contents[0])
    n = int(i.get("id")[-5:])
# finally print out the file
    print(y,n,file=open("ELECTION_ID", "a"))
