import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# start from an empty list
df_election = []
# read each election's csv (named every 4 years)
for i in range(1924,2020,4):
    header = pd.read_csv("president_general_{}.csv".format(i), nrows=5).dropna(axis=1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv("president_general_{}.csv".format(i), index_col = 0, thousands = ",", skiprows = [1])
# rename to democrat/republican
    df.rename(inplace = True, columns = d)
# drop empty columns
    df.dropna(inplace = True, axis = 1)
    df["Year"] = i
# add to the list
    df_election.append(df.loc[:, ["Democratic", "Republican", "Total Votes Cast", "Year"]])

# merge (by concat) the list to a dataframe.
df_elections = pd.concat(df_election)

# vote share for 4 cities
city = ["Accomack County", "Albemarle County", "Alexandria City", "Alleghany County"]
for i in city:
    df_city = df_elections.loc[df_elections.index.str.contains(i), : ].groupby("Year").sum()
    df_city["Republican Share"] = df_city["Republican"] / df_city["Total Votes Cast"]
    df_city["Year"] = df_city.index
# format the plot, axises, label, title, etc.
    df_city.plot(x = "Year", y = "Republican Share")
    plt.ylabel("Republican Vote Share")
    plt.xlabel("Year")
    plt.yticks(np.arange(0.0, 1.2, 0.1))
    plt.xticks(range(1924, 2020, 4),rotation = 90)
    plt.title("Republican Vote Share of " + i)
# save those plots as pdf, by each city name
    p_name = i.lower().replace(" ", "_") + ".pdf"
    plt.savefig(p_name)
