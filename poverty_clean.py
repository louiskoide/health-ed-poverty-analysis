import pandas as pd

FILE = "data/poverty_data.csv"

df = pd.read_csv(FILE)
# df["Poverty Rate"] = df["S1702_C02_001E"]
# df = df.drop("S1702_C02_001E", axis=1)

#create dataset with relevant columns
# df = df[["S1702_C02_001E", "NAME"]] 
# df[["County", "State"]] = df["NAME"].str.split(", ", expand=True)
# df = df.drop("NAME", axis=1)

# print(df)
# #clear out names for merging
# suffixes = [
#     " County",
#     " city",
#     " Municipio",
#     " Parish",
#     " Planning Region",
#     " Borough",
#     " Municipality"
# ]
# for suffix in suffixes:
#     df["County"] = df["County"].str.replace(suffix, "", regex=False)

df["County"] = df["County"].str.lower()

print(df)
#convert to csv to make it reusable
df.to_csv(FILE, index=False)