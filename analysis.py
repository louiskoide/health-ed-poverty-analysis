import pandas as pd
import matplotlib.pyplot as plt

FILE1 = "data/poverty_data.csv"
FILE2 = "data/health_data.csv"


df_poverty = pd.read_csv(FILE1)
df_health = pd.read_csv(FILE2)


#group health and poverty by state
health_state = (
    df_health
    .groupby("State", as_index=False)
    .agg(
        hospital_count=("Score", "count"),
        avg_er_score=("Score", "mean")
    )
)



poverty_state = (
    df_poverty
    .groupby("State", as_index=False)
    .agg(
        avg_poverty_rate=("Poverty Rate", "mean")
    )
)

#merge data
df = health_state.merge(poverty_state, on="State")

#find line for poverty
median_poverty = df["avg_poverty_rate"].median()
df["poverty_group"] = df["avg_poverty_rate"].apply(
    lambda x: "Higher Poverty" if x >= median_poverty else "Lower Poverty"
)

#print results
print(df.to_string())
print(df.groupby("poverty_group")["avg_er_score"].mean())

#print final boxplot
df.boxplot(column="avg_er_score", by="poverty_group")
plt.title("Emergency Department Performance by State Poverty Level")
plt.suptitle("")
plt.xlabel("Poverty Group")
plt.ylabel("Average ER Score")
plt.show()


#print final scatter plot
plt.scatter(df["avg_poverty_rate"], df["avg_er_score"])
plt.xlabel("Poverty Rate (%)")
plt.ylabel("Average ED Performance Score")
plt.title("Poverty Rate vs Emergency Department Performance")
plt.show()

r = df["avg_poverty_rate"].corr(df["avg_er_score"])
print(r)