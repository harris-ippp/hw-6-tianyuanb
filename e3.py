import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in each csv and append them into a list.
df_election = []
for i in range(1924,2020,4):
    header = pd.read_csv("president_general_{}.csv".format(i), nrows=5).dropna(axis=1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv("president_general_{}.csv".format(i), index_col = 0, thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d)
    df.dropna(inplace = True, axis = 1)
    df["Year"] = i
    df_election.append(df.loc[:, ["Democratic", "Republican", "Total Votes Cast", "Year"]])

# Concat the list to a dataframe.
df_elections = pd.concat(df_election)

# Calculating the Republican vote share for the four counties/cities; plot and save the figures as PDF.
city = ["Accomack County", "Albemarle County", "Alexandria City", "Alleghany County"]
for i in city:
    df_city = df_elections.loc[df_elections.index.str.contains(i), : ].groupby("Year").sum()
    df_city["Republican Share"] = df_city["Republican"] / df_city["Total Votes Cast"]
    df_city["Year"] = df_city.index
    df_city.plot(x = "Year", y = "Republican Share")
    plt.ylabel("Republican Vote Share")
    plt.xlabel("Year")
    plt.yticks(np.arange(0.0, 1.2, 0.1))
    plt.xticks(range(1924, 2020, 4),rotation = 90)
    plt.grid(True)
    plt.title("Republican Vote Share of " + i)
    p_name = i.lower().replace(" ", "_") + ".pdf"
    plt.savefig(p_name)
