import pandas as pd
FILE = "data/health_data.csv"

df = pd.read_csv(FILE)
print(df)

#state map to convert for merging
# state_map = {
#     "AL": "Alabama",
#     "AK": "Alaska",
#     "AZ": "Arizona",
#     "AR": "Arkansas",
#     "CA": "California",
#     "CO": "Colorado",
#     "CT": "Connecticut",
#     "DE": "Delaware",
#     "FL": "Florida",
#     "GA": "Georgia",
#     "HI": "Hawaii",
#     "ID": "Idaho",
#     "IL": "Illinois",
#     "IN": "Indiana",
#     "IA": "Iowa",
#     "KS": "Kansas",
#     "KY": "Kentucky",
#     "LA": "Louisiana",
#     "ME": "Maine",
#     "MD": "Maryland",
#     "MA": "Massachusetts",
#     "MI": "Michigan",
#     "MN": "Minnesota",
#     "MS": "Mississippi",
#     "MO": "Missouri",
#     "MT": "Montana",
#     "NE": "Nebraska",
#     "NV": "Nevada",
#     "NH": "New Hampshire",
#     "NJ": "New Jersey",
#     "NM": "New Mexico",
#     "NY": "New York",
#     "NC": "North Carolina",
#     "ND": "North Dakota",
#     "OH": "Ohio",
#     "OK": "Oklahoma",
#     "OR": "Oregon",
#     "PA": "Pennsylvania",
#     "RI": "Rhode Island",
#     "SC": "South Carolina",
#     "SD": "South Dakota",
#     "TN": "Tennessee",
#     "TX": "Texas",
#     "UT": "Utah",
#     "VT": "Vermont",
#     "VA": "Virginia",
#     "WA": "Washington",
#     "WV": "West Virginia",
#     "WI": "Wisconsin",
#     "WY": "Wyoming",
#     "DC": "District of Columbia"
# }
# df["State"] = df["State"].map(state_map)

#take data needed
df = df[["City/Town", "State", "Score"]]
df = df[df["Score"] != "Not Available"]
df["City/Town"] = df["City/Town"].str.lower()

print(df.to_string())

# #convert the dataframe back into the csv and replace current csv
df.to_csv(FILE, index=False)
